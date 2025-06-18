from rest_framework.serializers import ModelSerializer
from .models import *

class DestinationSerializer(ModelSerializer):
    class Meta:
        model = Destination
        fields = '__all__'
        
    def create(self, validated_data):
        validated_data.pop('images', None)
        destination = Destination.objects.create(**validated_data)
        
        images = self.context['request'].FILES.getlist('images')
        for img in images:
            Image.objects.create(destination=destination, image=img)
        return destination