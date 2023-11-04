from django.contrib import admin
from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from .apiviews import *
# from .apiviews import PollViewSet

router = DefaultRouter()


urlpatterns = [
	
    path("users/", UserList.as_view(), name="patient"),
    path("sms/",views.sms, name="sms"),
    path("stanbic/",views.stanbic, name="stanbic"),

]

urlpatterns += router.urls
