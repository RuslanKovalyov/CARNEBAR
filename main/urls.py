from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('contacts', views.contacts, name='contacts'),
    path('gallery', views.gallery, name='gallery'),
    path('dev', views.dev, name='dev'),
    path('404/', views.page_404, name='404'), # 404 page for testing. Hendler404 in restaurant_carnebar/url.py
]