"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
from blog1 import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.basic, name='basic'),
    url(r'^home/', views.home, name='home'),
    path('blog/', include("blog1.urls")),
    url(r'^about/', views.info, name='info'),
    url(r'^feedback/', views.feedback, name='feedback'),
    url(r'^contect/', views.us, name='us'),
    url(r'search/', views.search, name='search'),
    path('admin/', admin.site.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
