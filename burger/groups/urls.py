# -*- coding: utf-8 -*-
#
#
# Copyright (C) 2017 OSGeo
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
#

from django.urls import path
from django.views.generic import TemplateView

from .views import GroupDetailView, GroupActivityView
from . import views

urlpatterns = [  # 'geonode.groups.views',
    path(r'^$', TemplateView.as_view(
        template_name='groups/group_list.html'), name="group_list"),

    path(r'^categories/$',
        TemplateView.as_view(
            template_name="groups/category_list.html"),
        name="group_category_list"),
    path(r'^categories/_create/$', views.group_category_create,
        name="group_category_create"),
    path(r'^categories/(?P<slug>[-\w]+)/$',
        views.group_category_detail, name="group_category_detail"),
    path(r'^categories/(?P<slug>[-\w]+)/update/$', views.group_category_update,
        name="group_category_update"),

    path(r'^create/$', views.group_create, name="group_create"),
    path(r'^group/(?P<slug>[-\w]+)/$',
        GroupDetailView.as_view(), name='group_detail'),
    path(r'^group/(?P<slug>[-\w]+)/update/$',
        views.group_update, name='group_update'),
    path(r'^group/(?P<slug>[-\w]+)/members/$',
        views.group_members, name='group_members'),
    path(r'^group/(?P<slug>[-\w]+)/members_add/$',
        views.group_members_add, name='group_members_add'),
    path(r'^group/(?P<slug>[-\w]+)/member_remove/(?P<username>.+)$', views.group_member_remove,
        name='group_member_remove'),
    path(r'^group/(?P<slug>[-\w]+)/member_promote/(?P<username>.+)$',
        views.group_member_promote, name='group_member_promote'),
    path(r'^group/(?P<slug>[-\w]+)/member_demote/(?P<username>.+)$',
        views.group_member_demote, name='group_member_demote'),
    path(r'^group/(?P<slug>[-\w]+)/remove/$',
        views.group_remove, name='group_remove'),
    path(r'^group/(?P<slug>[-\w]+)/join/$',
        views.group_join, name='group_join'),
    path(r'^group/(?P<slug>[-\w]+)/activity/$',
        GroupActivityView.as_view(), name='group_activity'),
    path(r'^autocomplete/$',
        views.GroupProfileAutocomplete.as_view(), name='autocomplete_groups'),
    path(r'^autocomplete_category/$',
        views.GroupCategoryAutocomplete.as_view(), name='autocomplete_category'),
]
