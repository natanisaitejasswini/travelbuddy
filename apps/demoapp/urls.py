from django.conf.urls import url 
from . import views
urlpatterns = [
    url(r'^travels/add$', views.showUser),
    url(r'^addtrip$', views.user),
    url(r'^travels/destination/(?P<id>\d+)$', views.showdestination),
    url(r'^(?P<id>\d+)$', views.join)

]