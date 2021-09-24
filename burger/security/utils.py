# -*- coding: utf-8 -*-
#########################################################################
#
# Copyright (C) 2018 OSGeo
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
#########################################################################
from lxml import etree

import json
import logging
import traceback
import requests
from . import models

from requests.auth import HTTPBasicAuth
from django.conf import settings
from django.db.models import Q
from django.contrib.auth import get_user_model
# from django.contrib.gis.geos import GEOSGeometry
from django.contrib.contenttypes.models import ContentType
# from django.contrib.auth import login
from django.contrib.auth.models import Group, Permission
from django.core.exceptions import ObjectDoesNotExist
from guardian.utils import get_user_obj_perms_model
from guardian.shortcuts import assign_perm
from burger.groups.models import GroupProfile

logger = logging.getLogger("burger.security.utils")


def get_visible_resources(queryset,
                          user,
                          admin_approval_required=False,
                          unpublished_not_visible=False,
                          private_groups_not_visibile=False):
    is_admin = False
    is_manager = False
    if user:
        is_admin = user.is_superuser if user else False
        try:
            is_manager = user.groupmember_set.all().filter(role='manager').exists()
        except Exception:
            is_manager = False

    # Get the list of objects the user has access to
    anonymous_group = None
    public_groups = GroupProfile.objects.exclude(access="private").values('group')
    groups = []
    group_list_all = []
    manager_groups = []
    try:
        group_list_all = user.group_list_all().values('group')
    except Exception:
        pass
    try:
        manager_groups = Group.objects.filter(
            name__in=user.groupmember_set.filter(role="manager").values_list("group__slug", flat=True))
    except Exception:
        pass
    try:
        anonymous_group = Group.objects.get(name='anonymous')
        if anonymous_group and anonymous_group not in groups:
            groups.append(anonymous_group)
    except Exception:
        pass

    filter_set = queryset

    if admin_approval_required:
        if not is_admin:
            if is_manager:
                filter_set = filter_set.filter(
                    Q(is_published=True) |
                    Q(group__in=groups) |
                    Q(group__in=manager_groups) |
                    Q(group__in=group_list_all) |
                    Q(group__in=public_groups) |
                    Q(owner__username__iexact=str(user)))
            elif user:
                filter_set = filter_set.filter(
                    Q(is_published=True) |
                    Q(group__in=groups) |
                    Q(group__in=group_list_all) |
                    Q(group__in=public_groups) |
                    Q(owner__username__iexact=str(user)))
            else:
                filter_set = filter_set.filter(
                    Q(is_published=True) |
                    Q(group__in=public_groups) |
                    Q(group__in=groups))

    if unpublished_not_visible:
        if not is_admin:
            if user:
                filter_set = filter_set.exclude(
                    Q(is_published=False) & ~(
                        Q(owner__username__iexact=str(user)) | Q(group__in=group_list_all)))
            else:
                filter_set = filter_set.exclude(Q(is_published=False))

    if private_groups_not_visibile:
        if not is_admin:
            private_groups = GroupProfile.objects.filter(access="private").values('group')
            if user:
                filter_set = filter_set.exclude(
                    Q(group__in=private_groups) & ~(
                        Q(owner__username__iexact=str(user)) | Q(group__in=group_list_all)))
            else:
                filter_set = filter_set.exclude(group__in=private_groups)

    # Hide Dirty State Resources
    if not is_admin:
        if user:
            filter_set = filter_set.exclude(
                Q(dirty_state=True) & ~(
                    Q(owner__username__iexact=str(user)) | Q(group__in=group_list_all)))
        else:
            filter_set = filter_set.exclude(Q(dirty_state=True))
    return filter_set


def get_users_with_perms(obj):
    """
    Override of the Guardian get_users_with_perms
    """
    ctype = ContentType.objects.get_for_model(obj)
    permissions = {}
    PERMISSIONS_TO_FETCH = models.VIEW_PERMISSIONS + models.ADMIN_PERMISSIONS

    for perm in Permission.objects.filter(codename__in=PERMISSIONS_TO_FETCH, content_type_id=ctype.id):
        permissions[perm.id] = perm.codename

    user_model = get_user_obj_perms_model(obj)
    users_with_perms = user_model.objects.filter(object_pk=obj.pk,
                                                 content_type_id=ctype.id,
                                                 permission_id__in=permissions).values('user_id', 'permission_id')

    users = {}
    for item in users_with_perms:
        if item['user_id'] in users:
            users[item['user_id']].append(permissions[item['permission_id']])
        else:
            users[item['user_id']] = [permissions[item['permission_id']], ]

    profiles = {}
    for profile in get_user_model().objects.filter(id__in=list(users.keys())):
        profiles[profile] = users[profile.id]

    return profiles


def get_geofence_rules(page=0, entries=1, count=False):
    """Get the number of available GeoFence Cache Rules"""
    try:
        url = settings.OGC_SERVER['default']['LOCATION']
        user = settings.OGC_SERVER['default']['USER']
        passwd = settings.OGC_SERVER['default']['PASSWORD']

        _url = ''
        _headers = {'Content-type': 'application/json'}
        if count:
            """
            curl -X GET -u admin:geoserver \
                http://<host>:<port>/geoserver/rest/geofence/rules/count.json
            """
            _url = url + 'rest/geofence/rules/count.json'
        elif page or entries:
            """
            curl -X GET -u admin:geoserver \
                http://<host>:<port>/geoserver/rest/geofence/rules.json?page={page}&entries={entries}
            """
            _url = url + 'rest/geofence/rules.json?page={}&entries={}'.format(page, entries)
        r = requests.get(_url,
                         headers=_headers,
                         auth=HTTPBasicAuth(user, passwd),
                         timeout=10,
                         verify=False)
        if (r.status_code < 200 or r.status_code > 201):
            logger.debug("Could not retrieve GeoFence Rules count.")

        rules_objs = json.loads(r.text)
        return rules_objs
    except Exception:
        tb = traceback.format_exc()
        logger.debug(tb)
        return {'count': -1}


def get_geofence_rules_count():
    """Get the number of available GeoFence Cache Rules"""
    rules_objs = get_geofence_rules(count=True)
    rules_count = rules_objs['count']
    return rules_count


def get_highest_priority():
    """Get the highest Rules priority"""
    try:
        rules_count = get_geofence_rules_count()
        rules_objs = get_geofence_rules(rules_count - 1)
        if len(rules_objs['rules']) > 0:
            highest_priority = rules_objs['rules'][0]['priority']
        else:
            highest_priority = 0
        return int(highest_priority)
    except Exception:
        tb = traceback.format_exc()
        logger.debug(tb)
        return -1



def set_geofence_invalidate_cache():
    """invalidate GeoFence Cache Rules"""
    if settings.OGC_SERVER['default']['GEOFENCE_SECURITY_ENABLED']:
        try:
            url = settings.OGC_SERVER['default']['LOCATION']
            user = settings.OGC_SERVER['default']['USER']
            passwd = settings.OGC_SERVER['default']['PASSWORD']
            """
            curl -X GET -u admin:geoserver \
                  http://<host>:<port>/geoserver/rest/ruleCache/invalidate
            """
            r = requests.put(url + 'rest/ruleCache/invalidate',
                             auth=HTTPBasicAuth(user, passwd))

            if (r.status_code < 200 or r.status_code > 201):
                logger.debug("Could not Invalidate GeoFence Rules.")
                return False
            return True
        except Exception:
            tb = traceback.format_exc()
            logger.debug(tb)
            return False



def set_owner_permissions(resource):
    """assign all admin permissions to the owner"""
    if resource.polymorphic_ctype:
        # Set the GeoFence Owner Rule
        admin_perms = models.VIEW_PERMISSIONS + models.ADMIN_PERMISSIONS
        if resource.polymorphic_ctype.name == 'layer':
            for perm in models.LAYER_ADMIN_PERMISSIONS:
                assign_perm(perm, resource.owner, resource.layer)
        for perm in admin_perms:
            assign_perm(perm, resource.owner, resource.get_self_resource())


def remove_object_permissions(instance):
    """Remove object permissions on given resource.

    If is a layer removes the layer specific permissions then the
    resourcebase permissions

    """
    from guardian.models import UserObjectPermission, GroupObjectPermission
    resource = instance.get_self_resource()
    try:
        if hasattr(resource, "layer"):
            UserObjectPermission.objects.filter(
                content_type=ContentType.objects.get_for_model(resource.layer),
                object_pk=instance.id
            ).delete()
            GroupObjectPermission.objects.filter(
                content_type=ContentType.objects.get_for_model(resource.layer),
                object_pk=instance.id
            ).delete()
            if settings.OGC_SERVER['default']['GEOFENCE_SECURITY_ENABLED']:
                if not getattr(settings, 'DELAYED_SECURITY_SIGNALS', False):
                    purge_geofence_layer_rules(resource)
                    set_geofence_invalidate_cache()
            else:
                resource.set_dirty_state()
    except (ObjectDoesNotExist, RuntimeError):
        pass  # This layer is not manageable by geofence
    except Exception:
        tb = traceback.format_exc()
        logger.debug(tb)
    UserObjectPermission.objects.filter(content_type=ContentType.objects.get_for_model(resource),
                                        object_pk=instance.id).delete()
    GroupObjectPermission.objects.filter(content_type=ContentType.objects.get_for_model(resource),
                                         object_pk=instance.id).delete()


def _get_geofence_payload(layer, layer_name, workspace, access, user=None, group=None,
                          service=None, geo_limit=None):
    highest_priority = get_highest_priority()
    root_el = etree.Element("Rule")
    username_el = etree.SubElement(root_el, "userName")
    if user is not None:
        username_el.text = user
    else:
        username_el.text = ''
    priority_el = etree.SubElement(root_el, "priority")
    priority_el.text = str(highest_priority if highest_priority >= 0 else 0)
    if group is not None:
        role_el = etree.SubElement(root_el, "roleName")
        role_el.text = "ROLE_{}".format(group.upper())
    workspace_el = etree.SubElement(root_el, "workspace")
    workspace_el.text = workspace
    layer_el = etree.SubElement(root_el, "layer")
    layer_el.text = layer_name
    if service is not None and service != "*":
        service_el = etree.SubElement(root_el, "service")
        service_el.text = service
    if service and service == "*" and geo_limit is not None and geo_limit != "":
        # if getattr(layer, 'storeType', None) == 'coverageStore' and getattr(layer, 'srid', None):
        #     native_crs = layer.srid
        #     if native_crs != 'EPSG:4326':
        #         try:
        #             _native_srid = int(native_crs[5:])
        #             _wkt_wgs84 = geo_limit.split(';')[1]
        #             _poly = GEOSGeometry(_wkt_wgs84, srid=4326)
        #             _poly.transform(_native_srid)
        #             geo_limit = _poly.ewkt
        #         except Exception as e:
        #             traceback.print_exc()
        #             logger.exception(e)
        access_el = etree.SubElement(root_el, "access")
        access_el.text = "LIMIT"
        limits = etree.SubElement(root_el, "limits")
        catalog_mode = etree.SubElement(limits, "catalogMode")
        catalog_mode.text = "MIXED"
        allowed_area = etree.SubElement(limits, "allowedArea")
        allowed_area.text = geo_limit
    else:
        access_el = etree.SubElement(root_el, "access")
        access_el.text = access
    return etree.tostring(root_el)


def _update_geofence_rule(layer, layer_name, workspace, service, user=None, group=None, geo_limit=None):
    payload = _get_geofence_payload(
        layer=layer,
        layer_name=layer_name,
        workspace=workspace,
        access="ALLOW",
        user=user,
        group=group,
        service=service,
        geo_limit=geo_limit
    )
    logger.debug("request data: {}".format(payload))
    response = requests.post(
        "{base_url}rest/geofence/rules".format(
            base_url=settings.OGC_SERVER['default']['LOCATION']),
        data=payload,
        headers={
            'Content-type': 'application/xml'
        },
        auth=HTTPBasicAuth(
            username=settings.OGC_SERVER['default']['USER'],
            password=settings.OGC_SERVER['default']['PASSWORD']
        )
    )
    logger.debug("response status_code: {}".format(response.status_code))
    if response.status_code not in (200, 201):
        msg = ("Could not ADD GeoServer User {!r} Rule for "
               "Layer {!r}: '{!r}'".format(user, layer, response.text))
        if 'Duplicate Rule' in response.text:
            logger.debug(msg)
        else:
            raise RuntimeError(msg)


