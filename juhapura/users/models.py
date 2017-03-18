# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from countries_plus.models import Country


@python_2_unicode_compatible
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

    reason_registration_list = [
        (1, 'I\'m registring to find myself a partner'),
        (2, 'I\'m registring to find my friend a partner'),
        (3, 'I\'m registring to find my son a partner'),
        (4, 'I\'m registring to find my daughter a partner'),
        (5, 'I\'m registring to find my brother a partner'),
        (6, 'I\'m registring to find my sister a partner')
        ]

    income_list = [
        (0,'Prefer not to say'),
        (1,'Under Rs 50,000'),
        (2,'Rs 50,000 - Rs 1,00,000'),
        (3,'Rs 1,00,000 - Rs 3,00,000'),
        (4,'Rs 3,00,000 - Rs 5,00,000'),
         (4,'Rs 5,00,000 - Rs 10,00,000'),
        (6,'Above Rs 10,00,000'),
        ]

    occupation_list =[
    (0,'')
    ]

    qualification_list =[
    (0,'')]

    yes_no_list = [
    (1,'Yes'),
    (0,'No')
    ]

    name = models.CharField(_('Name of User'), 
        blank=True, 
        max_length=255)

    surname = models.CharField(_('Name of User'), 
        blank=True, 
        max_length=255)

    dob = models.DateField(_('Date of Birth'), 
        null=True)

    gender = models.CharField(choices=gender_list, default = 'M', null = True, max_length=1)

    location = models.CharField(_('Location'), 
        blank=True, 
        max_length=255)

    marital_status = models.IntegerField(choices=marital_status_list, 
        null = True)

    address_line1 = models.CharField(_('Address Line 1'), 
        blank = True, 
        max_length=255)

    address_line2 = models.CharField(_('Address Line 2'), 
        blank = True, 
        max_length=255)

    address_line3 = models.CharField(_('Address Line 3'), 
        blank = True, 
        max_length=255)

    city = models.ForeignKey(Cities)

    country = models.ForeignKey(Country,to_field="name", 
        db_constraint=False, on_delete=models.CASCADE, 
        default = "India")

    about_me = models.TextField(null=True)

    looking_for = models.TextField(null=True)

    reason_registration = models.IntegerField(choices=reason_registration_list, 
        null=True
        )

    #qualification & work

    qualification = models.IntegerField(choices=qualification_list, 
        null=True
        )

    qualification_summary = models.TextField(null=True)

    occupation = models.IntegerField(choices=occupation_list, 
        null=True
        )

    occupation_summary = models.TextField(null=True)

    income = models.IntegerField(choices=income_list, 
        null=True
        )

    #religion
    hijab = models.IntegerField(choices=yes_no_list, 
        null=True
        )

    beard  = models.IntegerField(choices=yes_no_list, 
        null=True
        )

    sect = models.CharField(_('Sect'), 
        blank = True, 
        max_length=255)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})


@python_2_unicode_compatible
class ProfileImage(models.Model):
    profile_image = models.FileField(upload_to='profile_images', blank=True, null=True)
    user = models.ForeignKey(User)    

    @property
    def userid(self):
        return self.user.username
    # def get_username(self):
    #     return self.username

