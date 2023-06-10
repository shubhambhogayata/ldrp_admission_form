from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("page2/", views.page2, name="page2"),
    path("page3/", views.page3, name="page3"),
    path("page4/", views.page4, name="page4"),
    path("pdf/", views.pdf, name="pdf"),
    path("imageUpload/", views.imageUpload, name="imageUpload"),
]