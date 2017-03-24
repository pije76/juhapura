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


    contact_no = forms.IntegerField(widget=forms.TextInput(
            attrs={'placeholder': 'Please provide contact number where one can get in touch with proposal'}
            ))

    mobile_no = forms.IntegerField(widget=forms.TextInput())

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

    about_me = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Briefy describe about yourself', 'rows':'10'}))

    looking_for = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Please brief your expectation regarding partner', 'rows':'10'}))

    complexion = forms.ChoiceField(choices = Profile.complexion_list, 
        widget=forms.Select(attrs={'class': 'ui search dropdown'}))

    body_type = forms.ChoiceField(choices = Profile.body_type_list, 
        widget=forms.Select(attrs={'class': 'ui search dropdown'}))

    mother_tongue = forms.ChoiceField(choices = Profile.mother_tongue_list, 
        widget=forms.Select(attrs={'class': 'ui search dropdown'}))

    height = forms.ChoiceField(choices = Profile.height_list,
        widget=forms.Select(attrs={'class': 'ui search dropdown'}))

    weight = forms.ChoiceField(choices = Profile.weight_list,
        widget=forms.Select(attrs={'class': 'ui search dropdown'}))

    class Meta:
        model = Profile
        fields = [
        'height',
        'weight',
        'body_type',
        'complexion',
        'mother_tongue',
        'about_me',
        'looking_for'
        ]
      

    def __init__(self, *args, **kwargs):

            super(AboutMeProfileForm, self).__init__(*args, **kwargs)
            # self.fields['height'].widget.attrs['placeholder'] = '5ft 10inch'
            # self.fields['weight'].widget.attrs['placeholder'] = '65 kgs'
      
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

    cast = forms.CharField()

    sub_cast = forms.CharField()

    hijab = forms.ChoiceField(choices = Profile.yes_no_list, 
        widget=forms.Select(attrs={'class': 'ui search dropdown'}))

    beard = forms.ChoiceField(choices = Profile.yes_no_list, 
        widget=forms.Select(attrs={'class': 'ui search dropdown'}))

    class Meta:
        model = Profile
        fields = [
        'cast',
        'sub_cast',
        'hijab'
        ,'beard'
        ]

    # def __init__(self, *args, **kwargs):

    #     if kwargs.get('instance'):
    #         name = kwargs['instance'].name
          
    #     return super(UserReligionInformationForm, self).__init__(*args, **kwargs)

class ProfileImageUploadForm(forms.Form):
    # For images (requires Pillow for validation 2MB):
    profile_image = MultiImageField(min_num=1, max_num=3, max_file_size=1024*1024*2, required=False)

    class Meta:
        model = ProfileImage

    def __init__(self, *args, **kwargs):
        
        if kwargs.get('instance'):
            # user = kwargs['instance'].user
        
            instance = ProfileImage.objects.filter(user_id=self.request.user.id)

        return super(ProfileImageUploadForm, self).__init__(*args, **kwargs)

class FamilyProfileForm(forms.ModelForm): 
    
    father_name = forms.CharField(widget=forms.TextInput(
            attrs={'placeholder': 'Father/Guardian Name'}
            ))

    mother_name = forms.CharField(widget=forms.TextInput(
            attrs={'placeholder': 'Mother/Sister Name'}
            ))

    family_summary = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Briefly describe about your sibling information and family history'}))

    class Meta:
        model = Profile
        fields = [
        'father_name'
        ,'mother_name'
        ,'family_summary'
        ]
