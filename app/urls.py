from django.urls import path
from .views import SaveCamImages, HomePage, getImage

urlpatterns = [
    # path('',HomePage.as_view(), name="HomePage"),
    path('saveimage',SaveCamImages.as_view(), name="saveimage"),
    path('',getImage, name="getImage"),
]
