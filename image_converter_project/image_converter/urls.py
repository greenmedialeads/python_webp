from django.urls import path
from . import views

urlpatterns = [
    path('', views.image_upload_view, name='upload'),
    path('success/', views.image_upload_view, name='success'),
]
