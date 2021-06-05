from django.contrib import admin
from django.urls import include, path
from baseapp import views

app_name = 'baseapp'

urlpatterns = [
    path('relative/', views.relative, name = 'relative'),
    path('other/', views.other, name = 'other'),
    path('base/', views.base, name='base'),
]
