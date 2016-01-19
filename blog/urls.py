"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView

from content import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.BlogView.as_view()),
    url(r'^newpost/', views.NewPost.as_view()),
    url(r'^signup/', views.Signup.as_view()),
    url(r'^(?P<pk>[0-9]+)/edit_profile/', views.EditProfile.as_view(), name='edit_profile'),
    url(r'^login/', views.Login.as_view()),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/login'}),
    url(r'^(?P<user_id>[0-9]+)/signup_details/', views.MakeProfile.as_view(), name='signup_details'),
    url(r'^(?P<pk>[0-9]+)/profile/', views.ViewProfile.as_view(), name='profile'),
    url(r'^post/(?P<pk>\d+)/', views.PostDetail.as_view()),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^xmas/', views.XmasForm.as_view()),
    url(r'^bugs/', views.BugForm.as_view()),
]
