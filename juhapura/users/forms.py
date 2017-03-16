# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import


from django import forms
from django.core.exceptions import ValidationError

from .models import User

class UserBasicProfileUpdateForm(forms.ModelForm):


    gender_list = [('','Gender'), ('M','Male'), ('F','Female')]

    name = forms.CharField()

    dob = forms.DateField()

    gender = forms.ChoiceField(choices=gender_list, 
    	widget=forms.Select(attrs={'class': 'ui search dropdown'}))

    location = forms.CharField()

    marital_status = forms.ChoiceField(choices = User.marital_status_list, 
    	widget=forms.Select(attrs={'class': 'ui search dropdown'}))

    # city = forms.ChoiceField(forms.Select(attrs={'class': 'ui search dropdown'}))
    
    class Meta:
        model = User
        fields = [
        'name'
        ,'dob'
        ,'gender'
        ,'location'
        ,'marital_status'
        ,'address_line1'
        ,'address_line2'
        ,'address_line3' 
        ,'city'
        ,'country'
        ]

    def __init__(self, *args, **kwargs):

        if kwargs.get('instance'):
            name = kwargs['instance'].name
            # kwargs.setdefault('initial', {})['confirm_email'] = email
            # dob'].widget.format = '%d/%m/%Y'
            widgets = {
            # 'dob': forms.DateInput(attrs={'class':'myDateClass', 
            #                                 'placeholder':'Select a date'})
            'city':forms.Select(attrs={'class':'ui search dropdown'})
        	}
            # self.fields['city'].widget = ListTextWidget(class='test')
        return super(UserBasicProfileUpdateForm, self).__init__(*args, **kwargs)


class UserContactInformationForm(forms.ModelForm):


    Address = [(0,'Male'), (1,'Female')]

    name = forms.CharField()

    dob = forms.DateField(
    	 # input_formats=('%d-%m-%Y')
    	)


    address_line1 = forms.CharField()

    location = forms.CharField()

    marital_status = forms.ChoiceField(choices = User.marital_status_list)

    class Meta:
        model = User
        fields = ['name'
        ,'dob'
        ,'gender'
        ,'location'
        ,'marital_status'
        , 'city'
        # ,'country'
        ]

    def __init__(self, *args, **kwargs):

        if kwargs.get('instance'):
            name = kwargs['instance'].name
            # kwargs.setdefault('initial', {})['confirm_email'] = email
            # dob'].widget.format = '%d/%m/%Y'
            widgets = {
            'dob': forms.DateInput(#format=('%d-%m-%Y'), 

                                             attrs={'class':'myDateClass', 
                                            'placeholder':'Select a date'})
        }

        return super(UserBasicProfileUpdateForm, self).__init__(*args, **kwargs)