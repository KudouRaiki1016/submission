from django.urls import path

from . import views

urlpatterns = [
    path('', views.top_view, name="top-page"),
]