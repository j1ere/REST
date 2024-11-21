from django.urls import path
from . import views

urlpatterns = [
    path("", views.api_view),
    path("models/", views.model_api),
    path("models_serialized/", views.model_api_serialized),
]