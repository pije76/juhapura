from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, FormView, DeleteView, UpdateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse
from juhapura.users.models import User

from .models import Scholarship, Document
from .forms import ScholarshipForm, DocumentUploadForm
from datetime import datetime
from django.contrib import messages

# Create your views here.
class IndexView(TemplateView):
    model = Scholarship
    # These next two lines tell the view to index lookups by username
    template_name = 'scholarship/index.html'

    def get_object(self):
        # Only get the User record for the user making the request
        return Scholarship.objects.filter(user=self.request.user.id)

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['Scholarship'] = self.get_object()
        return context


class ScholarshipFormView(LoginRequiredMixin, UpdateView):
    model = Scholarship
    template_name = 'scholarship/apply.html'
    form_class = ScholarshipForm

    def get_success_url(self):
        return reverse('scholarship:document_upload')

    def form_valid(self, form):
        user = User.objects.get(pk=self.request.user.id)
        form.instance.user = user
        return super(ScholarshipFormView, self).form_valid(form)

    def get_object(self):
        try:
            scholarship_obj = Scholarship.objects.get(user=self.request.user)
            # if scholarship_obj.date_submitted:
            #     messages.error(self.request, "We already your application, we will be in touch.")
            #     return reverse('scholarship:view')

        except Scholarship.DoesNotExist:
            scholarship_obj = Scholarship.objects.create(user=self.request.user)

        return scholarship_obj


class DocumentUploadFormView(LoginRequiredMixin, FormView):
    model = Document
    template_name = 'scholarship/document_upload.html'
    form_class = DocumentUploadForm

    def get_success_url(self):
        if 'submit' in self.request.POST:
            messages.error(self.request, "We have your application, we will be in touch.")
            return reverse('scholarship:view')
        else:
            return reverse('scholarship:document_upload')


    def get_context_data(self, **kwargs):
        scholarship = Scholarship.objects.get(user=self.request.user)
        context = super(DocumentUploadFormView, self).get_context_data(**kwargs)
        context['documents'] = Document.objects.filter(scholarship=scholarship)
        return context

    def form_valid(self, form):

        user = User.objects.get(pk=self.request.user.id)
        scholarship = Scholarship.objects.get(user=user)
        for each in form.cleaned_data['document']:
            if (Document.objects.filter(scholarship=scholarship).count() < 5):
                Document.objects.create(document=each,scholarship=scholarship)
            else:
                messages.error(self.request, "Only five supporting document allowed per application")

        documents = Document.objects.filter(scholarship=scholarship)

        return super(DocumentUploadFormView, self).form_valid(form)

    def post(self, request, *args, **kwargs):
        if 'submit' in request.POST:
            user = User.objects.get(pk=self.request.user.id)
            scholarship = Scholarship.objects.get(user=user)
            scholarship.date_submitted = datetime.now()
            scholarship.save()
        return super(DocumentUploadFormView, self).post(request, *args, **kwargs)



class DocumentDeleteView(LoginRequiredMixin, DeleteView):
    model = Document
    success_url = '/scholarship/upload/'


class ScholarshipView(LoginRequiredMixin, TemplateView):
    template_name = 'scholarship/view.html'

    def get_context_data(self, **kwargs):
        context = super(ScholarshipView, self).get_context_data(**kwargs)
        context["scholarship"] = Scholarship.objects.get(user= self.request.user.id)
        context["documents"] = Document.objects.filter(scholarship= context["scholarship"])
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return self.render_to_response(context)
