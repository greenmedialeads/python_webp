from django.shortcuts import render, redirect
from .models import UploadedImage
from PIL import Image as PILImage
import os

def image_upload_view(request):
    if request.method == 'POST':
        files = request.FILES.getlist('uploaded_images')  # Retrieve multiple files
        for file in files:
            # Save the original image
            uploaded_image = UploadedImage.objects.create(original_image=file)

            # Convert to WebP
            webp_path = convert_to_webp(uploaded_image.original_image.path)
            
            # Delete the original image after conversion
            os.remove(uploaded_image.original_image.path)
            
            uploaded_image.converted_image = webp_path
            uploaded_image.save()

        return redirect('success')  # Redirect to a success page
    return render(request, 'upload.html')

def convert_to_webp(image_path):
    """
    Converts the uploaded image to WebP format and returns the new path.
    """
    webp_path = image_path.rsplit('.', 1)[0] + '.webp'
    with PILImage.open(image_path) as img:
        img.convert('RGB').save(webp_path, 'webp')
    return webp_path
