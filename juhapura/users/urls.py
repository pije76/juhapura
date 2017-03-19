# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^$',
        view=views.MatrimonialHomePageView.as_view(),
        name='index'
    ),
    url(
        regex=r'^~redirect/$',
        view=views.UserRedirectView.as_view(),
        name='redirect'
    ),
    url(
        regex=r'^(?P<username>[\w.@+-]+)/$',
        view=views.UserDetailView.as_view(),
        name='detail'
    ),
    url(
        regex=r'^~update/$',
        view=views.UserUpdateView.as_view(),
        name='update'
    ),

    url(
        regex=r'^~profile/$',
        view=views.UserBasicProfileUpdateForm.as_view(),
        name='profile_update'
    ),

    url(
        regex=r'^~about/$',
        view=views.UserAboutInformationForm.as_view(),
        name='personal_update'
    ),

    url(
        regex=r'^~imageupload/$',
        view=views.UserProfileImageUploadView.as_view(),
        name='profile_upload'
    ),

    url(
        regex=r'^~qualification/$',
        view=views.UserQualificationWorkInformationForm.as_view(),
        name='qualification_update'
    ),

    url(
        regex=r'^~religion/$',
        view=views.UserReligionInformationForm.as_view(),
        name='religion_update'
    ),

     url(
        regex=r'^~family/$',
        view=views.UserFamilyInformationForm.as_view(),
        name='family_update'
    ),
]
