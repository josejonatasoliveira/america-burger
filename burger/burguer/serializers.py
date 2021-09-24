from rest_framework import serializers
from .models import Burguer

class BurguerSerializer(serializers.Serializer):
    id = serializers.DecimalField(max_digits=10, decimal_places=2)
    code = serializers.CharField()
    name = serializers.CharField()
    description = serializers.CharField()
    price = serializers.CharField()
    discount = serializers.DecimalField(max_digits=10, decimal_places=2)
    weight = serializers.CharField()
    energetic_value = serializers.CharField()
    point = serializers.DecimalField(max_digits=10, decimal_places=2)
    available = serializers.BooleanField()
    image_file = serializers.CharField()
    hash_id = serializers.CharField()
    quantity = serializers.IntegerField()

    def create(self, validated_data):
      return Burguer(**validated_data)