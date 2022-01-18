
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('apps/create/', views.JobAppCreate.as_view(), name='jobapps_create'),
    path('apps/index/', views.apps_index, name='jobapps_index'),
    path('apps/<int:jobapp_id>/detail', views.apps_detail, name='jobapps_detail'),
    path('apps/<int:pk>/udpate', views.JobAppUpdate.as_view(), name='jobapps_update'),
    path('apps/<int:pk>/delete', views.JobAppDelete.as_view(), name='jobapps_delete'),
    path('resources/create/', views.ResourceCreate.as_view(), name='resources_create'),
    path('resources/index/', views.resources_index, name='resources_index'),
    path('resources/<int:resource_id>/detail/', views.resources_detail, name='resources_detail'),
    path('resources/<int:pk>/udpate', views.ResourceUpdate.as_view(), name='resources_update'),
    path('resources/<int:pk>/delete', views.ResourceDelete.as_view(), name='resources_delete'),
    path('resources/<int:resource_id>/detail/add_comment', views.add_comment, name='add_comment'),
    path('favorites/index', views.favorites_index, name='favorites_index'),
    path('favorites/<int:resource_id>/', views.assoc_resource, name='assoc_resource'),
    path('favorites/<int:favorite_id>/delete', views.favorites_delete, name='favorites_delete'),
]