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
from .models import JobApp, Resource, Favorite, Comment
from .forms import CommentForm
from datetime import date, datetime
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver



def home(request):
  return render(request, 'home.html')

def apps_index(request):
  jobapps = JobApp.objects.filter(user_id=request.user.id)
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
  comment_form = CommentForm()
  favorite = Favorite.objects.filter(user=request.user).values_list('resource_id', flat=True)
  # if favorite is True:
  favorite_id = Favorite.objects.filter(resource_id=resource_id).first()
  return render(request, 'resources/detail.html', { 'resource': resource, 'comment_form': comment_form, 'favorite': favorite, 'favorite_id': favorite_id })


def add_comment(request, resource_id):
  form = CommentForm(request.POST)
  if form.is_valid(): 
    new_comment = form.save(commit=False)
    new_comment.resource_id = resource_id
    new_comment.comment_date = datetime.now()
    new_comment.user = request.user
    new_comment.save()
  return redirect('resources_detail', resource_id=resource_id)

def delete_comment(request, resource_id, comment_id):
  Comment.objects.get(id=comment_id).delete()
  return redirect('resources_detail', resource_id=resource_id)

class ResourceCreate(LoginRequiredMixin, CreateView):
    model = Resource
    fields = ['category', 'title', 'content', 'resource_url']

    def form_valid(self, form):
      form.instance.user = self.request.user
      return super().form_valid(form)


class ResourceUpdate(LoginRequiredMixin, UpdateView):
  model = Resource
  fields = ['category', 'title', 'content', 'resource_url']

class ResourceDelete(LoginRequiredMixin, DeleteView):
  model = Resource
  success_url = '/resources/index/'

@login_required
def favorites_index(request):
  user_favorites = Favorite.objects.filter(user=request.user)
  return render(request, 'favorites/index.html', {'favorites': user_favorites})

def favorites_delete(request, favorite_id):
  Favorite.objects.filter(id=favorite_id).delete()
  return redirect('favorites_index')

@login_required
def assoc_resource(request, resource_id):
  Favorite.objects.create(user_id=request.user.id, resource_id=resource_id)
  return redirect('favorites_index')
