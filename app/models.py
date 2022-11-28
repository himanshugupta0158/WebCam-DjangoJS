from django.db import models

# Create your models here.


class Cam_Image(models.Model):
    image = models.ImageField(upload_to="images/")
