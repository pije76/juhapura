# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^$',
        view=views.IndexView.as_view(),
        name='index'
    ),
    url(
        regex=r'^apply/$',
        view=views.ScholarshipFormView.as_view(),
        name='apply'
    ),
    url(
        regex=r'^upload/$',
        view=views.DocumentUploadFormView.as_view(),
        name='document_upload'
        ),
    url(
        regex=r'^delete_document/(?P<pk>\d+)/$',
        view=views.DocumentDeleteView.as_view(),
        name='delete_document',
    ),
    ]
