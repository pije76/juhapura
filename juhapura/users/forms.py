# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import


from django import forms
from django.core.exceptions import ValidationError
from multiupload.fields import MultiImageField

from .models import User
from captcha.fields import ReCaptchaField

class UserBasicProfileUpdateForm(forms.ModelForm):


    # gender_list = [('','Gender'), ('M','Male'), ('F','Female')]

    name = forms.CharField()

    # dob = forms.DateField()

    # gender = forms.ChoiceField(choices=gender_list,
    # 	widget=forms.Select(attrs={'class': 'ui search dropdown'}))

    # location = forms.CharField()

    # marital_status = forms.ChoiceField(choices = User.marital_status_list,
    # 	widget=forms.Select(attrs={'class': 'ui search dropdown'}))

    # # city = forms.ChoiceField(forms.Select(attrs={'class': 'ui search dropdown'}))
    # reason_registration = forms.ChoiceField(choices = User.reason_registration_list,
    # 	widget=forms.Select(attrs={'class': 'ui search dropdown'}))


    class Meta:
        model = User
        fields = [
        'name'
        # ,'surname'
        # ,'dob'
        # ,'gender'
        # ,'location'
        # ,'marital_status'
        # ,'address_line1'
        # ,'address_line2'
        # ,'address_line3'
        # ,'city'
        # ,'country'
        # ,'reason_registration'
        ]

    def __init__(self, *args, **kwargs):

        if kwargs.get('instance'):
            name = kwargs['instance'].name
            # kwargs.setdefault('initial', {})['confirm_email'] = email
            # dob'].widget.format = '%d/%m/%Y'
         #    widgets = {
         #    # 'dob': forms.DateInput(attrs={'class':'myDateClass',
         #    #                                 'placeholder':'Select a date'})
         #    'city':forms.Select(attrs={'class':'ui search dropdown'})
        	# }
            # self.fields['city'].widget = ListTextWidget(class='test')
        return super(UserBasicProfileUpdateForm, self).__init__(*args, **kwargs)

class AllauthSignupForm(forms.Form):

    captcha = ReCaptchaField()

    def signup(self, request, user):
        """ Required, or else it throws deprecation warnings """
        pass
