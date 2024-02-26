from django.urls import path
from .views import *

urlpatterns = [
    path("api/<str:api>", apiHandler),
]
