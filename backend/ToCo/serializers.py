from rest_framework import serializers
from .models import MainContent
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile

class MainContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainContent
        fields = '__all__'

        def getImage(self, MainContent):
            if MainContent.image:
                return MainContent.image.url
            return None



class ProjectListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainContent
        fields = '__all__'

    def to_internal_value(self, data):
        file_data = data.get('image')

        if file_data:
            file_name = file_data.name
            image = self.resize_image(file_data)
            file_data = self.create_uploaded_file(image, file_name)
            data['image'] = file_data

        return super().to_internal_value(data)

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