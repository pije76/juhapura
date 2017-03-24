# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url
from django.conf import settings

from . import views

urlpatterns = [
    url(
        regex=r'^$',
        view=views.MatrimonialHomePageView.as_view(),
        name='index'
    ),
   

    url(
        regex=r'^~profile/$',
        view=views.BasicProfileUpdateView.as_view(),
        name='profile_update'
    ),

    url(
        regex=r'^~about/$',
        view=views.AboutMeProfileView.as_view(),
        name='personal_update'
    ),

    url(
        regex=r'^~imageupload/$',
        view=views.ProfileImageUploadView.as_view(),
        name='image_upload'
    ),

    url(
        regex=r'^~qualification/$',
        view=views.QualificationWorkProfileView.as_view(),
        name='qualification_update'
    ),

    url(
        regex=r'^~religion/$',
        view=views.ReligionProfileView.as_view(),
        name='religion_update'
    ),

     url(
        regex=r'^~family/$',
        view=views.FamilyProfileView.as_view(),
        name='family_update'
    ),

      url(
        regex=r'^~activate/$',
        view=views.ProfileActivateView.as_view(),
        name='activate'
    ),

      url(
        regex=r'^~user_profile/$',
        view=views.UserProfileView.as_view(),
        name='profile'
    ),
    url(
        regex=r'^~delete_image/(?P<pk>\d+)/$', 
        view= views.ProfileImageDeleteView.as_view(),
        name='delete_profileimage',
      ),
        url(
        regex=r'^(?P<username>[\w.@+-]+)/$',
        view=views.UserProfileView.as_view(),
        name='detail'
    ),
]
