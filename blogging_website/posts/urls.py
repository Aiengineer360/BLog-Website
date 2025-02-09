from django.urls import path
from . import views # i have Imported the views module

urlpatterns = [
    path('', views.home, name='home'), # i have Added a URL pattern for the home view
    path('post/<int:pk>/', views.post_detail, name='post_detail'), # i have Added a URL pattern for the post_detail view
    path('post/new/', views.post_create, name='post_create'), # i have Added a URL pattern for the post_create view
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'), # i have Added a URL pattern for the post_edit view
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'), # i have Added a URL pattern for the post_delete view
]