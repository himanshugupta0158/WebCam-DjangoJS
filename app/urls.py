from django.urls import path

from .views import HomePage, SaveCamImages, getImage

urlpatterns = [
    path("saveimage", SaveCamImages.as_view(), name="saveimage"),
    path("", getImage, name="getImage"),
]
