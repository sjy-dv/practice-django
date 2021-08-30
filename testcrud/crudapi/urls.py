from django.conf.urls import url
from crudapi import views

urlpatterns = [
    url(r'^api/test$', views.testlist),
    url(r'^api/detail$', views.testdetail),
    url(r'^api/test_create$', views.testcreate),
    url(r'^api/test_update$', views.testupdate),
    url(r'^api/test_delete$', views.testdelete),
]
