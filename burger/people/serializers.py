from django.contrib.auth import get_user_model
from rest_framework import serializers

UserModel = get_user_model()

class ProfileSignInSerializer(serializers.Serializer):
  first_name = serializers.CharField(write_only=True)
  last_name = serializers.CharField(write_only=True)
  username = serializers.CharField(write_only=True)
  email = serializers.CharField(write_only=True)
  birthday = serializers.DateTimeField(write_only=True, format="%d-%m-%Y")
  phone_number = serializers.CharField(write_only=True)
  password = serializers.CharField(write_only=True)

  def create(self, validated_data):
    user = UserModel.objects.create(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            username=validated_data['username'],
            email=validated_data['email'],
            birthday=validated_data['birthday'],
            phone_number=validated_data['phone_number'],
        )
    user.set_password(validated_data['password'])
    user.save()
    return user