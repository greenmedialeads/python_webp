from django.db import models

class UploadedImage(models.Model):
    original_image = models.ImageField(upload_to='uploaded_images/')
    converted_image = models.ImageField(upload_to='converted_images/', null=True, blank=True)

    def __str__(self):
        return f"Original: {self.original_image.name}"
