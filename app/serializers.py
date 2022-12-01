from rest_framework import serializers
from .models import User,Car,BookingRequest

class UserSerializer(serializers.ModelSerializer):
    password2=serializers.CharField(style={'input_type':'password'},write_only=True)
    class Meta:
        model=User
        fields=['username','email','user_type','password','password2']
        extra_kwargs={
            'password':{'write_only':True}
            }
    def validate(self, data):
        password=data.get('password')
        password2=data.get('password2')
        if password!=password2:
            raise serializers.ValidationError('password and confirm password has not matched')
        return data
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class UserLoginSerializer(serializers.ModelSerializer):
    username=serializers.CharField(max_length=30)
    class Meta:
        model = User
        fields = ['username','password']


class UserProfileSeriallizer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields="__all__"

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model=Car
        fields=["id","car_model","colour","fuel_type",'price_per_hour',"car_images","is_available"]


class BookingRequestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=BookingRequest


