from django.urls import path

from .views import *

urlpatterns = [
    path('', TestAPIListCreate.as_view(), name="api_settings_list_create"),
]