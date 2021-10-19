from django.core.mail import send_mail
from rest_framework import serializers
from .models import User 



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id' , 'email', 'last_name', 'first_name' , 'gender' , 'avatar' , 'likes']
        
class CrateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id' , 'email','password','last_name', 'first_name' , 'gender' , 'avatar']
        extra_kwargs ={
            'password':{'write_only':True}
        }
        
    def create(self, validated_data):
            user = User(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            gender=validated_data['gender'],
            avatar=validated_data['avatar'],
            


        )
            user.set_password(validated_data['password'])

            user.save()
            return user
        