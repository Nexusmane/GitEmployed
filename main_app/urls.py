
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('apps/create/', views.JobAppCreate.as_view(), name='jobapps_create'),
    path('apps/index/', views.apps_index, name='jobapps_index'),
    path('apps/<int:jobapp_id>/', views.apps_detail, name='jobapps_detail'),
    path('apps/<int:pk>/udpate', views.JobAppUpdate.as_view(), name='jobapps_update'),
    path('apps/<int:pk>/delete', views.JobAppDelete.as_view(), name='jobapps_delete'),
    path('resources/create/', views.ResourceCreate.as_view(), name='resources_create'),
    path('resources/index/', views.resources_index, name='resources_index')
]