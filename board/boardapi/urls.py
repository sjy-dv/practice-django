from boardapi import views
from django.conf.urls import url

urlpatterns = [
    url(r'^api/user/sign$', views.sign),
    url(r'^api/user/login$', views.login),
    url(r'^api/user/auth$', views.auth),
    url(r'^api/board/write', views.boardwrite),
    url(r'^api/board/update', views.boardupdate),
    url(r'^api/board/detail', views.boarddetail),
    url(r'^api/board/delete', views.boarddelete),
]