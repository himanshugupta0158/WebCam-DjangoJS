import base64

import cv2 as cv
import numpy as np
from django.core.files import File, images
from django.core.files.base import ContentFile
from django.shortcuts import render
from django.views import View
from PIL import Image

from .models import Cam_Image

# Create your views here.

# def save(encoded_data, filename):
#     nparr = np.fromstring(encoded_data.decode('base64'), np.uint8)
#     img = cv.imdecode(nparr, cv.IMREAD_ANYCOLOR)
#     return cv.imwrite(filename, img)


class HomePage(View):
    template_name = "index.html"

    def get(self, request):
        return render(
            request,
            "index.html",
            {"msg": "Click Save Picture Button to Save Cam Image."},
        )


class SaveCamImages(View):
    template_name = "index.html"

    def post(self, request):
        # getting data from post HTTP method.
        img = request.POST["image"]
        # print(img)

        # saving image base64 encoded data into database
        cam = Cam_Image.objects.create(image=img)
        cam.save()

        # image_file_like = ContentFile(base64.b64decode(img))
        print("works")
        return render(request, "index.html", {"msg": "Image Saved Successfully"})


def getImage(request):
    response = Cam_Image.objects.all().order_by("-id")
    if len(response) > 12:
        response = response[0:12]
    elif len(response) < 1:
        response = []
    imgs = []
    for i in response:
        imgs.append(i.image)
    return render(request, "index.html", {"imgs": imgs})
