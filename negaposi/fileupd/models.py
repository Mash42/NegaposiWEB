from django.db import models

# Create your models here.


class PostData(models.Model):
    name = models.TextField()
    email = models.TextField()
    content_message = models.TextField()
    file_path = models.TextField()
    file_name = models.TextField()
