
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('accounts/signup/', views.signup, name='signup'),
    path('apps/create/', views.JobAppCreate.as_view(), name='apps_create'),
    path('apps/index/', views.apps_index, name="apps_index"),
    path('apps/<int:jobapp_id>/', views.apps_detail, name="apps_detail"),
]