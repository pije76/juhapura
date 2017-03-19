# Create your views here.
from __future__ import absolute_import, unicode_literals

from django.core.urlresolvers import reverse
from django.views.generic import DetailView, ListView, RedirectView, UpdateView, TemplateView, FormView, CreateView

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Profile, ProfileImage
from .forms import ProfileImageUploadForm \
                    ,BasicProfileUpdateForm \
                    ,AboutMeProfileForm \
                    ,QualificationWorkProfileForm \
                    ,ReligionProfileForm \
                    ,FamilyProfileForm

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from django.contrib import messages

from juhapura.users.models import User
from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader


class ProfileActivateView(LoginRequiredMixin,CreateView):
    model = Profile
    # fields = ['user']
    template_name = 'matrimonial/index.html'
    form_class = BasicProfileUpdateForm

    # def form_valid(self, form):
    #     user = self.request.user.id
    #     Profile.objects.create()
    #     return super(ProfileActivateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('matrimonial:index', 
            kwargs={'profile': Profile.objects.filter(user=self.request.user.id)})
       
    def post(self, form):
        # import pdb
        # pdb.set_trace()
        user = User.objects.get(pk=self.request.user.id)
        # template_name = 'matrimonial/index.html'
        template = loader.get_template('matrimonial/index.html')
        profile = Profile.objects.filter(user=user)
        if not profile:
            Profile.objects.create(user=user)

        context = {
        'profile': profile,
        }

        return HttpResponse(template.render(context, self.request))

        

    def get_object(self):
        # Only get the User record for the user making the request
        return Profile.objects.get(user=self.request.user.id)

class ProfileImageUploadView(LoginRequiredMixin, FormView):
    template_name = 'matrimonial/upload_profile.html'
    form_class = ProfileImageUploadForm
    success_url = 'matrimonial/~imageupload/'

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


        return super(ProfileImageUploadView, self).form_valid(form)

    def get_success_url(self):
        return reverse('users:detail',
                       kwargs={'username': self.request.user.username, 
                              'images': ProfileImage.objects.filter(user=self.request.user)})

    def get_object(self):
        # Only get the User record for the user making the request
        return ProfileImage.objects.get(user=self.request.user.username)

# class BasicProfileUpdateView(LoginRequiredMixin, UpdateView):

    # fields = ['firstname', 'surname', 'location', 'dob' ,'gender']

    # # we already imported User in the view code above, remember?
    # model = Profile

    # # send the user back to their own page after a successful update
    # def get_success_url(self):
    #     return reverse('users:detail',
    #                    kwargs={'username': self.request.user.username})

    # def get_object(self):
    #     # Only get the User record for the user making the request
    #     return User.objects.get(username=self.request.user.username)

class MatrimonialHomePageView(LoginRequiredMixin,TemplateView):
    model = Profile
    # These next two lines tell the view to index lookups by username
    template_name = 'matrimonial/index.html'

    def get_object(self):
        # Only get the User record for the user making the request
        return Profile.objects.get(user=self.request.user.id)

    def get_context_data(self, **kwargs):
        context = super(MatrimonialHomePageView, self).get_context_data(**kwargs)
        context['profile'] = self.get_object()
        return context

class BasicProfileUpdateView(LoginRequiredMixin, UpdateView):
    # slug_field = 'username'
    # slug_url_kwarg = 'username'
    model = Profile
    template_name = 'matrimonial/basic_profile.html'
    form_class = BasicProfileUpdateForm

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse('matrimonial:profile_update')

    def get_object(self):
        # Only get the User record for the user making the request
        return Profile.objects.get(user=self.request.user.id)

class AboutMeProfileView(LoginRequiredMixin, UpdateView):
    slug_field = 'username'
    slug_url_kwarg = 'username'
    model = Profile
    template_name = 'matrimonial/aboutme_profile.html'
    form_class = AboutMeProfileForm

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse('users:detail',
                       kwargs={'username': self.request.user.username})

    def get_object(self):
        # Only get the User record for the user making the request
        return User.objects.get(username=self.request.user.username)

class QualificationWorkProfileView(LoginRequiredMixin, UpdateView):
    slug_field = 'username'
    slug_url_kwarg = 'username'
    model = Profile
    template_name = 'matrimonial/qualification_profile.html'
    form_class = QualificationWorkProfileForm

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse('users:detail',
                       kwargs={'username': self.request.user.username})

    def get_object(self):
        # Only get the User record for the user making the request
        return User.objects.get(username=self.request.user.username)

class ReligionProfileView(LoginRequiredMixin, UpdateView):
    slug_field = 'username'
    slug_url_kwarg = 'username'
    model = Profile
    template_name = 'matrimonial/religion_profile.html'
    form_class = ReligionProfileForm

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse('users:detail',
                       kwargs={'username': self.request.user.username})

    def get_object(self):
        # Only get the User record for the user making the request
        return User.objects.get(username=self.request.user.username)

class FamilyProfileView(LoginRequiredMixin, UpdateView):
    slug_field = 'username'
    slug_url_kwarg = 'username'
    model = Profile
    template_name = 'matrimonial/family_profile.html'
    form_class = FamilyProfileForm  

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse('users:detail',
                       kwargs={'username': self.request.user.username})

    def get_object(self):
        # Only get the User record for the user making the request
        return User.objects.get(username=self.request.user.username)