import os
import re
import json

from math import atan, exp, log, pi, sin, tan, floor
from django.conf import settings
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied
from django.db import models
from django.utils.translation import gettext_lazy as _



def resolve_object(request, model, query, permission='base.view_resourcebase',
                   permission_required=True, permission_msg=None):
                   
    obj = get_object_or_404(model, **query)
    obj_to_check = obj.get_self_resource()

    from guardian.shortcuts import assign_perm, get_groups_with_perms
    from geonode.groups.models import GroupProfile

    groups = get_groups_with_perms(obj_to_check,
                                   attach_perms=True)

    if obj_to_check.group and obj_to_check.group not in groups:
        groups[obj_to_check.group] = obj_to_check.group

    obj_group_managers = []
    obj_group_members = []
    if groups:
        for group in groups:
            try:
                group_profile = GroupProfile.objects.get(slug=group.name)
                managers = group_profile.get_managers()
                if managers:
                    for manager in managers:
                        if manager not in obj_group_managers and not manager.is_superuser:
                            obj_group_managers.append(manager)
                if group_profile.user_is_member(
                        request.user) and request.user not in obj_group_members:
                    obj_group_members.append(request.user)
            except GroupProfile.DoesNotExist:
                pass

    if settings.RESOURCE_PUBLISHING or settings.ADMIN_MODERATE_UPLOADS:
        is_admin = False
        is_manager = False
        is_owner = True if request.user == obj_to_check.owner else False
        if request.user:
            is_admin = request.user.is_superuser if request.user else False
            try:
                is_manager = request.user.groupmember_set.all().filter(role='manager').exists()
            except Exception:
                is_manager = False
        if (not obj_to_check.is_published):
            if not is_admin:
                if is_owner or (
                        is_manager and request.user in obj_group_managers):
                    if (not request.user.has_perm('publish_resourcebase', obj_to_check)) and (
                        not request.user.has_perm('view_resourcebase', obj_to_check)) and (
                            not request.user.has_perm('change_resourcebase_metadata', obj_to_check)) and (
                                not is_owner and not settings.ADMIN_MODERATE_UPLOADS):
                        raise Http404
                    else:
                        assign_perm(
                            'view_resourcebase', request.user, obj_to_check)
                        assign_perm(
                            'publish_resourcebase',
                            request.user,
                            obj_to_check)
                        assign_perm(
                            'change_resourcebase_metadata',
                            request.user,
                            obj_to_check)
                        assign_perm(
                            'download_resourcebase',
                            request.user,
                            obj_to_check)

                        if is_owner:
                            assign_perm(
                                'change_resourcebase', request.user, obj_to_check)
                            assign_perm(
                                'delete_resourcebase', request.user, obj_to_check)
                            assign_perm(
                                'change_resourcebase_permissions',
                                request.user,
                                obj_to_check)
                else:
                    if request.user in obj_group_members:
                        if (not request.user.has_perm('publish_resourcebase', obj_to_check)) and (
                            not request.user.has_perm('view_resourcebase', obj_to_check)) and (
                                not request.user.has_perm('change_resourcebase_metadata', obj_to_check)):
                            raise Http404
                    else:
                        raise Http404

    allowed = True
    if permission.split('.')[-1] in ['change_layer_data',
                                     'change_layer_style']:
        if obj.__class__.__name__ == 'Layer':
            obj_to_check = obj
    if permission:
        if permission_required or request.method != 'GET':
            if request.user in obj_group_managers:
                allowed = True
            else:
                allowed = request.user.has_perm(
                    permission,
                    obj_to_check)
    if not allowed:
        mesg = permission_msg or _('Permission Denied')
        raise PermissionDenied(mesg)
    return obj