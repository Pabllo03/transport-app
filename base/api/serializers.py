from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from base.models import Car, TestTube, CollectionPoint

class CarSerializer(ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'

class TestTubeSerializer(ModelSerializer):
    class Meta:
        model = TestTube
        fields = '__all__'

class CollectionPointSerializer(ModelSerializer):
    class Meta:
        model = CollectionPoint
        fields = '__all__'
