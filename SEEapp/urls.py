from django.conf.urls import patterns, include, url
from django.contrib import admin
from SEEapp import views


urlpatterns = [

            url(r'^$', views.root, name='root'),
            url(r'^aboutus$', views.about, name='about'),
            url(r'^videos$', views.videos, name='videos'),
            url(r'^getinvolved$', views.getinvolved, name='getinvolved'),
            url(r'^team$', views.team, name='team'),
            url(r'^single$', views.single, name='single')
]
