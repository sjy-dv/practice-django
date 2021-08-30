from boardapi import views
from django.conf.urls import url

urlpatterns = [
    url(r'^api/user/sign$', views.sign),
    url(r'^api/user/login$', views.login),
]