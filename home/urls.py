from django.urls import path
from django.conf.urls import handler404
from .views import *

urlpatterns = [
    
]

handler404 = views.error_404