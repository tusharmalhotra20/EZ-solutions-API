""" Serializer class is used to convert your data into JSON"""

from rest_framework import serializers
from . models import users

class UsersSerializers(serializers.ModelSerializer):
    class Meta:
        model = users
        fields = (
            'username',
            'first_name',
            'last_name',
            'email', 
            'password'
        )
#fields = '__all__'