"""healthsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.contrib import admin
from healthsite.core import views as core_views


urlpatterns = [
    url(r'^$', include('homeapp.urls')),
    url(r'^profile/', core_views.profile, name='profile'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^signup/$', core_views.signup, name='signup'),
    url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^contact/$', core_views.contact, name='contact'),
    url(r'^addExercise/$', core_views.addExercise, name='addExercise'),
    url(r'^viewExercises/$', core_views.viewExercises, name='viewExercises'),
    url(r'^viewExercise/$', core_views.viewExercise, name='viewExercise'),
#    url(r'^editprofile/$', core_views.editprofile, name='Exercise'),
   # url(r'^view/$', core_views.viewExercises, name='view'),
  ##


    
    
]
