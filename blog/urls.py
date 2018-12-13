from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'post_list'),
    path('base/', views.base_template, name = 'base'),
    path('about/', views.about, name = 'about'),
]
