import datetime

from django.db import models


# Create your models here.
class UploadPic(models.Model):
  file = models.FileField(upload_to="uploads")

