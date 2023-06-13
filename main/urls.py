from django.urls import path
from . import views

urlpatterns = [
    path('', views.dev, name='dev'),
    path('home/', views.index, name='home'),
    path('contacts', views.contacts, name='contacts'),
    path('404/', views.page_404, name='404'), # 404 page for testing. Hendler404 in restaurant_carnebar/url.py
]