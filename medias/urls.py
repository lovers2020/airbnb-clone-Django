from django.urls import path

from medias.views import PhotoDetail, GetUploadURL


urlpatterns = [
    path("photos/<int:pk>", PhotoDetail.as_view()),
    path("photos/get-url", GetUploadURL.as_view()),
]
