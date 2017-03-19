# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import


from django import forms
from django.core.exceptions import ValidationError
from multiupload.fields import MultiImageField

from .models import Profile, ProfileImage

class BasicProfileUpdateForm(forms.ModelForm):


    gender_list = [('','Gender'), ('M','Male'), ('F','Female')]

    # first_name = forms.CharField()

    dob = forms.DateField()

    gender = forms.ChoiceField(choices=gender_list, 
    	widget=forms.Select(attrs={'class': 'ui search dropdown'}))

    location = forms.CharField()

    marital_status = forms.ChoiceField(choices = Profile.marital_status_list, 
    	widget=forms.Select(attrs={'class': 'ui search dropdown'}))

    # city = forms.ChoiceField(forms.Select(attrs={'class': 'ui search dropdown'}))
    reason_registration = forms.ChoiceField(choices = Profile.reason_registration_list,
    	widget=forms.Select(attrs={'class': 'ui search dropdown'}))


    class Meta:
        model = Profile
        fields = [
        'first_name'
        ,'surname'
        ,'dob'
        ,'gender'
        ,'location'
        ,'marital_status'
        ,'address_line1'
        ,'address_line2'
        ,'address_line3' 
        ,'city'
        ,'country'
        ,'reason_registration'
        ]

    def __init__(self, *args, **kwargs):

        if kwargs.get('instance'):
            # name = kwargs['instance'].name
            # kwargs.setdefault('initial', {})['confirm_email'] = email
            # dob'].widget.format = '%d/%m/%Y'
            widgets = {
            # 'dob': forms.DateInput(attrs={'class':'myDateClass', 
            #                                 'placeholder':'Select a date'})
            'city':forms.Select(attrs={'class':'ui search dropdown'})
        	}
            # self.fields['city'].widget = ListTextWidget(class='test')
        return super(BasicProfileUpdateForm, self).__init__(*args, **kwargs)

class AboutMeProfileForm(forms.ModelForm):   

    about_me = forms.CharField(widget=forms.Textarea)

    looking_for = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Profile
        fields = [
        'about_me'
        ,'looking_for'
        ]

    # def __init__(self, *args, **kwargs):

    #     if kwargs.get('instance'):
    #         name = kwargs['instance'].name
    #         # self.fields['about_me'].widget.attrs = { 'placeholder':'About me', 'rows':'10'}
    #         # self.fields['looking_for'].widget.attrs = { 'placeholder':'What I Am Looking For?', 'rows':'10'}


    #     return super(AboutMeProfileForm, self).__init__(*args, **kwargs)

class QualificationWorkProfileForm(forms.ModelForm):   

    qualification = forms.ChoiceField(choices = Profile.qualification_list, 
        widget=forms.Select(attrs={'class': 'ui search dropdown'}))

    qualification_summary = forms.CharField(widget=forms.Textarea)

    occupation = forms.ChoiceField(choices = Profile.occupation_list, 
        widget=forms.Select(attrs={'class': 'ui search dropdown'}))

    occupation_summary = forms.CharField(widget=forms.Textarea)

    income = forms.ChoiceField(choices = Profile.income_list, 
        widget=forms.Select(attrs={'class': 'ui search dropdown'}))

    class Meta:
        model = Profile
        fields = [
        'qualification'
        ,'qualification_summary'
        ,'occupation'
        ,'occupation_summary'
        ,'income'
        ]

    # def __init__(self, *args, **kwargs):

    #     if kwargs.get('instance'):
    #         name = kwargs['instance'].name
    #         # self.fields['about_me'].widget.attrs = { 'placeholder':'About me', 'rows':'10'}
    #         # self.fields['looking_for'].widget.attrs = { 'placeholder':'What I Am Looking For?', 'rows':'10'}


    #     return super(QualificationWorkProfileForm, self).__init__(*args, **kwargs)

class ReligionProfileForm(forms.ModelForm):   

    sect = forms.CharField()

    hijab = forms.ChoiceField(choices = Profile.yes_no_list, 
        widget=forms.Select(attrs={'class': 'ui search dropdown'}))

    beard = forms.ChoiceField(choices = Profile.yes_no_list, 
        widget=forms.Select(attrs={'class': 'ui search dropdown'}))

    class Meta:
        model = Profile
        fields = [
        'sect',
        'hijab'
        ,'beard'
        ]

    # def __init__(self, *args, **kwargs):

    #     if kwargs.get('instance'):
    #         name = kwargs['instance'].name
          
    #     return super(UserReligionInformationForm, self).__init__(*args, **kwargs)

class ProfileImageUploadForm(forms.Form):
    # For images (requires Pillow for validation 2MB):
    profile_image = MultiImageField(min_num=1, max_num=3, max_file_size=1024*1024*2)

    class Meta:
        model = ProfileImage

    def __init__(self, *args, **kwargs):
        
        if kwargs.get('instance'):
            user = kwargs['instance'].user
        
            instance = ProfileImage.objects.filter(user=self.request.user.id)

        return super(ProfileImageUploadForm, self).__init__(*args, **kwargs)

class FamilyProfileForm(forms.ModelForm): 
    
    father_name = forms.CharField()

    mother_name = forms.CharField()

    parent_contact_no = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'One of your parent contact detail'}))

    family_summary = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Please briefly describe about your sibling information and family history'}))

    class Meta:
        model = Profile
        fields = [
        'father_name'
        ,'mother_name'
        ,'parent_contact_no'
        ,'family_summary'
        ]
