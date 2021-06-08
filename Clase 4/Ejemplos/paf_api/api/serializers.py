from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from api.models import UserModel, TuitModel


class TuitSerializer(serializers.ModelSerializer):
    '''
    Tuit serializer.
    '''
    
    class Meta:
        model = TuitModel
        fields = [
            'id',
            'content',
            'author',
            'created_on',
        ]
        extra_kwargs = {
            'id': {
                'read_only': True,
            },
            'author': {
                'allow_null': True,
            },
            'created_on': {
                'read_only': True,
            },
        }


class UserSerializer(serializers.ModelSerializer):
    '''
    User serializer.
    '''
    tuits = TuitSerializer(many=True, read_only=True)

    class Meta:
        model = UserModel
        fields = [
            'id',
            'username',
            'password',
            'tuits',
            'created_on',
            'updated_on',
        ]
        extra_kwargs = {
            'id': {
                'read_only': True,
            },
            'password': {
                'write_only': True,
            },
            'created_on': {
                'read_only': True,
            },
            'updated_on': {
                'read_only': True,
            },
        }

    def validate_password(self, value):
        validate_password(value)
        return value

    def create(self, validated_data):
        user = get_user_model()(**validated_data)

        user.set_password(validated_data['password'])
        user.save()

        return user
