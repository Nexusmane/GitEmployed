from http.client import UPGRADE_REQUIRED
from importlib import resources
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from .models import JobApp, Resource

# Create your views here.

def home(request):
  return render(request, 'home.html')

def apps_index(request):
  jobapps = JobApp.objects.all()
  return render(request, 'job_applications/index.html', { 'jobapps': jobapps })

def apps_detail(request, jobapp_id):
  jobapp = JobApp.objects.get(id=jobapp_id)
  return render(request, 'job_applications/detail.html', { 'jobapp': jobapp })

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('home')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)


class JobAppCreate(LoginRequiredMixin, CreateView):
  model = JobApp
  fields = ['company', 'job_title', 'submission_date', 'follow_up_date', 'job_post_url', 'description', 'notes', 'excitement_level', 'resume_url', 'cover_letter_url']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class JobAppUpdate(LoginRequiredMixin, UpdateView):
    model = JobApp
    fields = ['excitement_level', 'job_title', 'description', 'follow_up_date', 'job_post_url', 'notes', 'resume_url', 'cover_letter_url']

class JobAppDelete(LoginRequiredMixin, DeleteView):
    model = JobApp
    success_url = '/apps/index/'


def resources_index(request):
  resources = Resource.objects.all()
  return render(request, 'resources/index.html', { 'resources': resources })

def resources_detail(request, resource_id):
  resource = Resource.objects.get(id=resource_id)
  return render(request, 'resources/detail.html', { 'resource': resource })


class ResourceCreate(LoginRequiredMixin, CreateView):
    model = Resource
    fields = ['category', 'title', 'content', 'resource_url', 'replies']

    def form_valid(self, form):
      form.instance.user = self.request.user
      return super().form_valid(form)