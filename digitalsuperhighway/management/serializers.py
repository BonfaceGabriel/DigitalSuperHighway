from rest_framework import serializers
from .models import DigitalRoad

class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = DigitalRoad
        fields = '__all__'
        
