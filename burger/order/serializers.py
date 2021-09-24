from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.Serializer):
    id = serializers.DecimalField()
    code = serializers.CharField()
    name = serializers.CharField()
    description = serializers.CharField()
    price = serializers.CharField()
    discount = serializers.DecimalField()
    weight = serializers.CharField()
    energetic_value = serializers.CharField()
    point = serializers.DecimalField()
    available = serializers.BooleanField()
    image_file = serializers.CharField()
    hash_id = serializers.CharField()
    quantity = serializers.IntegerField()

  def create(self, validated_data):
    return Order(**validated_data)

class OrderItemSerializer(serializers.Serializer):
  order = OrderSerializer()
  quantity = serializers.IntegerField()
  final_price = serializers.DecimalField(max_digits=10, decimal_places=2)

  def create(self, validated_data):
    return OrderItem(**validated_data)