from rest_framework import serializers
from .models import MainContent
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile

class MainContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainContent
        fields = '__all__'


class ProjectListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainContent
        fields = '__all__'

    def resize_image(self, image):
        pil_image = Image.open(image)

        resized_image = pil_image.resize((250, 250)) 

        output = BytesIO()
        resized_image.save(output, format='JPEG') 
        output.seek(0)

        return output

    def create_uploaded_file(self, file, filename):
        uploaded_file = InMemoryUploadedFile(
            file, 
            None, 
            filename,  
            'image/jpeg', 
            file.getbuffer().nbytes,  
            None 
        )

        return uploaded_file