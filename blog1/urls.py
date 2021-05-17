from django.contrib import admin
from django.urls import path
from blog1 import views
urlpatterns = [

    path('<str:Slug>', views.news, name='news'),

]