from django.contrib import admin
from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from .apiviews import *
# from .apiviews import PollViewSet

router = DefaultRouter()


urlpatterns = [
	
    path("users/", UserList.as_view(), name="patient"),

]

urlpatterns += router.urls
