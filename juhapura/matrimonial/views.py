# Create your views here.
from __future__ import absolute_import, unicode_literals

from django.core.urlresolvers import reverse
from django.views.generic import DetailView, ListView, RedirectView, UpdateView, TemplateView, FormView, CreateView, DeleteView

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
        return Profile.objects.filter(user=self.request.user.id)

class ProfileImageDeleteView(LoginRequiredMixin, DeleteView):
     model = ProfileImage
     success_url = '/matrimonial/image_upload/'

class ProfileImageUploadView(LoginRequiredMixin, FormView):
    template_name = 'matrimonial/upload_profile.html'
    form_class = ProfileImageUploadForm
    success_url = 'matrimonial/image_upload/'

    model = ProfileImage
   

    def get_context_data(self, **kwargs):
        profile = Profile.objects.get(user_id=self.request.user.id)
        context = super(ProfileImageUploadView, self).get_context_data(**kwargs)
        context['profile_images'] = ProfileImage.objects.filter(profile=profile)
        return context


    def form_valid(self, form):
       
        user = self.request.user
        # form.valid_check(user=user)
       
        user = User.objects.get(pk=self.request.user.id)
        profile = Profile.objects.get(user=user)
        for each in form.cleaned_data['profile_image']:

            if (ProfileImage.objects.filter(profile=profile).count() < 3):
               
                ProfileImage.objects.create(profile_image=each,profile=profile)
            else:
                messages.error(self.request, "Only 3 pictures allowed per profile")
        
        images = ProfileImage.objects.filter(profile=profile)


        return super(ProfileImageUploadView, self).form_valid(form)

    def get_success_url(self):
        return reverse('matrimonial:image_upload')

    def get_object(self):
        # Only get the User record for the user making the request
        user = User.objects.get(pk=self.request.user)
        profile = Profile.objects.get(user=user)
        return ProfileImage.objects.get(profile=profile)

class MatrimonialHomePageView(TemplateView):
    model = Profile
    # These next two lines tell the view to index lookups by username
    template_name = 'matrimonial/index.html'

    def get_object(self):
        # Only get the User record for the user making the request
        return Profile.objects.filter(user=self.request.user.id)

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
        return reverse('matrimonial:personal_update')

    def get_object(self):
        # Only get the User record for the user making the request
        return Profile.objects.get(user=self.request.user.id)

class AboutMeProfileView(LoginRequiredMixin, UpdateView):

    model = Profile
    template_name = 'matrimonial/aboutme_profile.html'
    form_class = AboutMeProfileForm

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse('matrimonial:qualification_update')

    def get_object(self):
        # Only get the User record for the user making the request
        return Profile.objects.get(user=self.request.user.id)

class QualificationWorkProfileView(LoginRequiredMixin, UpdateView):
    slug_field = 'username'
    slug_url_kwarg = 'username'
    model = Profile
    template_name = 'matrimonial/qualification_profile.html'
    form_class = QualificationWorkProfileForm

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse('matrimonial:religion_update')

    def get_object(self):
        # Only get the User record for the user making the request
        return Profile.objects.get(user=self.request.user.id)


class ReligionProfileView(LoginRequiredMixin, UpdateView):
    slug_field = 'username'
    slug_url_kwarg = 'username'
    model = Profile
    template_name = 'matrimonial/religion_profile.html'
    form_class = ReligionProfileForm

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse('matrimonial:family_update')

    def get_object(self):
        # Only get the User record for the user making the request
        return Profile.objects.get(user_id=self.request.user.id)


class FamilyProfileView(LoginRequiredMixin, UpdateView):
    slug_field = 'username'
    slug_url_kwarg = 'username'
    model = Profile
    template_name = 'matrimonial/family_profile.html'
    form_class = FamilyProfileForm  

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse('matrimonial:image_upload')

    def get_object(self):
        # Only get the User record for the user making the request
        return Profile.objects.get(user=self.request.user.id)


class UserProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'matrimonial/profile.html'

    def get_context_data(self, **kwargs):
        context = super(UserProfileView, self).get_context_data(**kwargs)
        context["profile"] = Profile.objects.get(user= self.request.user.id)
        context["profile_images"] = ProfileImage.objects.filter(profile= context["profile"])
        context["martial_status"] = dict(Profile.marital_status_list).get(context["profile"].marital_status)
        context["mother_tongue"] = dict(Profile.mother_tongue_list).get(context["profile"].mother_tongue)
        context["qualification"] = dict(Profile.qualification_list).get(context["profile"].qualification)
        context["occupation"] = dict(Profile.occupation_list).get(context["profile"].occupation)
        context["income"] = dict(Profile.income_list).get(context["profile"].income)
        return context


    def get(self, request, *args, **kwargs):
       context = self.get_context_data()
       return self.render_to_response(context)


    # def get_queryset(self):
    #     current_user = User.objects.get(pk=self.request.user.id)

    #     # Must filter by author to prevent making everyone's notes public
    #     queryset = Profile.objects.filter(user=current_user)

    #     return queryset


    # def get_object(self):
        
    #     return Profile.objects.get(user = self.request.user)       

    # def get_profile_images(self):
    #     return ProfileImage.objects.get(user_id = self.request.user.id)