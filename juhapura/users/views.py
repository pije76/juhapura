# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.core.urlresolvers import reverse
from django.views.generic import DetailView, ListView, RedirectView, UpdateView, TemplateView, FormView

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import User, ProfileImage
from .forms import UserBasicProfileUpdateForm \
                    ,UserAboutInformationForm \
                    ,UserQualificationWorkInformationForm \
                    ,UserReligionInformationForm \
                    ,UserProfileImageUploadForm \
                    ,UserFamilyInformationForm

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from django.contrib import messages



class UserProfileImageUploadView(LoginRequiredMixin, FormView):
    template_name = 'users/upload_profile.html'
    form_class = UserProfileImageUploadForm
    success_url = '/matrimonial/~imageupload/'

    model = ProfileImage
    slug_field = 'user'
    slug_url_kwarg = 'user'

    def form_valid(self, form):
       
        user = self.request.user

        # form.valid_check(user=user)

        for each in form.cleaned_data['profile_image']:
            if (ProfileImage.objects.filter(user=user).count() < 3):
                ProfileImage.objects.create(profile_image=each,user=user)
            else:
                messages.error(self.request, "Only 3 pictures allowed per profile")
        
        images = ProfileImage.objects.filter(user=user)


        return super(UserProfileImageUploadView, self).form_valid(form)

    def get_success_url(self):
        return reverse('users:detail',
                       kwargs={'username': self.request.user.username, 
                              'images': ProfileImage.objects.filter(user=self.request.user)})

    def get_object(self):
        # Only get the User record for the user making the request
        return ProfileImage.objects.get(user=self.request.user.username)

class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = 'username'
    slug_url_kwarg = 'username'


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse('users:detail',
                       kwargs={'username': self.request.user.username})


class UserUpdateView(LoginRequiredMixin, UpdateView):

    fields = ['name', 'surname', 'location', 'dob' ,'gender']

    # we already imported User in the view code above, remember?
    model = User

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse('users:detail',
                       kwargs={'username': self.request.user.username})

    def get_object(self):
        # Only get the User record for the user making the request
        return User.objects.get(username=self.request.user.username)


class UserListView(LoginRequiredMixin, ListView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = 'username'
    slug_url_kwarg = 'username'


class MatrimonialHomePageView(LoginRequiredMixin,TemplateView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = 'username'
    slug_url_kwarg = 'username'    
    template_name = 'users/matrimonial.html'


class UserBasicProfileUpdateForm(LoginRequiredMixin, UpdateView):
    slug_field = 'username'
    slug_url_kwarg = 'username'
    model = User
    template_name = 'users/basic_profile.html'
    form_class = UserBasicProfileUpdateForm

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse('users:detail',
                       kwargs={'username': self.request.user.username})

    def get_object(self):
        # Only get the User record for the user making the request
        return User.objects.get(username=self.request.user.username)


class UserAboutInformationForm(LoginRequiredMixin, UpdateView):
    slug_field = 'username'
    slug_url_kwarg = 'username'
    model = User
    template_name = 'users/personal_profile.html'
    form_class = UserAboutInformationForm

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse('users:detail',
                       kwargs={'username': self.request.user.username})

    def get_object(self):
        # Only get the User record for the user making the request
        return User.objects.get(username=self.request.user.username)


class UserQualificationWorkInformationForm(LoginRequiredMixin, UpdateView):
    slug_field = 'username'
    slug_url_kwarg = 'username'
    model = User
    template_name = 'users/qualification_profile.html'
    form_class = UserQualificationWorkInformationForm

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse('users:detail',
                       kwargs={'username': self.request.user.username})

    def get_object(self):
        # Only get the User record for the user making the request
        return User.objects.get(username=self.request.user.username)


class UserReligionInformationForm(LoginRequiredMixin, UpdateView):
    slug_field = 'username'
    slug_url_kwarg = 'username'
    model = User
    template_name = 'users/religion_profile.html'
    form_class = UserReligionInformationForm

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse('users:detail',
                       kwargs={'username': self.request.user.username})

    def get_object(self):
        # Only get the User record for the user making the request
        return User.objects.get(username=self.request.user.username)


class UserFamilyInformationForm(LoginRequiredMixin, UpdateView):
    slug_field = 'username'
    slug_url_kwarg = 'username'
    model = User
    template_name = 'users/family_profile.html'
    form_class = UserFamilyInformationForm  

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse('users:detail',
                       kwargs={'username': self.request.user.username})

    def get_object(self):
        # Only get the User record for the user making the request
        return User.objects.get(username=self.request.user.username)
