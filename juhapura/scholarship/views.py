from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, FormView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse
from juhapura.users.models import User

from .models import Scholarship, Document
from .forms import ScholarshipForm, DocumentUploadForm
from datetime import datetime

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
        # form.instance.date_submitted = datetime.now()
        return super(ScholarshipFormView, self).form_valid(form)

    def get_object(self):
        # Only get the User record for the user making the request
        return Scholarship.objects.get(user=self.request.user.id)


class DocumentUploadFormView(LoginRequiredMixin, FormView):
    model = Document
    template_name = 'scholarship/document_upload.html'
    form_class = DocumentUploadForm

    def get_success_url(self):
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
        # import pdb
        # pdb.set_trace()
        if 'submit' in request.POST:
            user = User.objects.get(pk=self.request.user.id)
            scholarship = Scholarship.objects.get(user=user)
            scholarship.date_submitted = datetime.now()
            scholarship.save()
        return super(DocumentUploadFormView, self).post(request, *args, **kwargs)


class DocumentDeleteView(LoginRequiredMixin, DeleteView):
    model = Document
    success_url = '/scholarship/upload/'
