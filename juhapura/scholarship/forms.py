from __future__ import unicode_literals, absolute_import

from django import forms
from multiupload.fields import MultiFileField
from juhapura.utils.models import ChoiceLists

from .models import Scholarship, Document



class ScholarshipForm(forms.ModelForm):
    error_css_class = 'ui red message'
    required_css_class = 'red'

    document = MultiFileField(min_num=1, max_num=5, max_file_size=1024 * 1024 * 2, required=False)

    gender = forms.ChoiceField(choices=ChoiceLists.gender_list,
                              widget=forms.Select(attrs={'class': 'ui search dropdown'}))

    ahd_resident = forms.ChoiceField(choices=ChoiceLists.yes_no_list,
                               widget=forms.Select(attrs={'class': 'ui search dropdown'}))

    grant_before = forms.ChoiceField(choices=ChoiceLists.yes_no_list,
                               widget=forms.Select(attrs={'class': 'ui search dropdown'}))

    class Meta:
        model = Scholarship
        fields=[
            'first_name',
            'surname',
            'contact_number',
            'dob',
            'gender',
            'address',
            'ahd_resident',
            'education_history',
            'grant_before',
            'statement'
        ]


class DocumentUploadForm(forms.Form):

    document = MultiFileField(min_num=1, max_num=5, max_file_size=1024 * 1024 * 2, required=False)

    class Meta:
        model = Document
        fields=[
           'document'
        ]

    def __init__(self, *args, **kwargs):

        if kwargs.get('instance'):
            # user = kwargs['instance'].user
            scholarship = Scholarship.objects.get(user= self.request.user)
            instance = Document.objects.filter(scholarship= scholarship)

        return super(DocumentUploadForm, self).__init__(*args, **kwargs)
