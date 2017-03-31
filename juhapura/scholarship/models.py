from django.db import models
from django.utils.translation import ugettext_lazy as _

from juhapura.users.models import User
from juhapura.utils.models import ChoiceLists

from datetime import datetime

class Scholarship(models.Model):

    user = models.ForeignKey(User)

    first_name = models.CharField(_('First name'), blank=True, max_length=255)

    surname = models.CharField(_('Surname'), blank=True, max_length=255)

    dob = models.DateField(_('Date of Birth'), null=True)

    contact_number = models.CharField(_('Contact Number'), blank=True,  max_length=15, null=True)

    gender = models.CharField(choices=ChoiceLists.gender_list, default='M', null=True, max_length=1)

    address = models.TextField(_('Address'), blank=True, max_length=255)

    ahd_resident = models.IntegerField(choices=ChoiceLists.yes_no_list, null=True)

    education_history = models.TextField(null=True)

    grant_before = models.IntegerField(choices=ChoiceLists.yes_no_list, null=True)

    statement = models.TextField(null=True)

    # document = models.FileField(upload_to='scholarship', blank=True, null=True)

    date_submitted = models.DateField(_('Submitted on'), null=True)


class Document(models.Model):
    document = models.FileField(upload_to='scholarship/%s'%datetime.now().year, blank=True, null=True)
    scholarship = models.ForeignKey(Scholarship)
