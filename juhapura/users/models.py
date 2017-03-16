# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from countries_plus.models import Country

class Cities(models.Model):
    city_id = models.AutoField(primary_key=True)
    city_name = models.CharField(max_length=100, blank=True, null=True)
    city_state = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cities'
        ordering = ['city_name']

    def __str__(self):
        return ' - '.join([self.city_name, self.city_state])

@python_2_unicode_compatible
class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    gender_list = [('M','Male'), ('F','Female')]

    marital_status_list = [
    (0, 'Unmarried'),
    (1, 'Divorcee'),
    (2, 'Seperated'),
    (3, 'Widow/Widower')
    ]

    name = models.CharField(_('Name of User'), blank=True, max_length=255)

    dob = models.DateField(_('Date of Birth'), null=True)

    gender = models.CharField(choices=gender_list, default = 'M', null = True, max_length=1)

    location = models.CharField(_('Location'), blank=True, max_length=255)

    marital_status = models.IntegerField(choices=marital_status_list, null = True)

    address_line1 = models.CharField(_('Address Line 1'), blank = True, max_length=255)

    address_line2 = models.CharField(_('Address Line 2'), blank = True, max_length=255)

    address_line3 = models.CharField(_('Address Line 3'), blank = True, max_length=255)

    city = models.ForeignKey(Cities)

    country = models.ForeignKey(Country,to_field="name", db_constraint=False, on_delete=models.CASCADE, default = "India")

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})



