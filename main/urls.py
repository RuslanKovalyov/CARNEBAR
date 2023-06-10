from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('404/', views.page_404, name='404'), # 404 page for testing. Hendler404 in restaurant_carnebar/url.py
]