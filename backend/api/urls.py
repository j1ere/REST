from django.urls import path
from . import views

urlpatterns = [
    path("", views.custom_api_view),
    path("models/", views.model_api),
    path("models_serialized/", views.model_api_serialized),
    path("drf_response/", views.model_api_drf),
    path("books/", views.BookListCreateAPIView.as_view()),
    path("mybooks/", views.MyBookListCreateAPIView.as_view()),
]