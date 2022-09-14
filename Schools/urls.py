from django.urls import path

from . import views

urlpatterns = [
    # path("", views.index, name="index"),
    path("school/<str:pk_school>/", views.school_index, name="school_index"),
]