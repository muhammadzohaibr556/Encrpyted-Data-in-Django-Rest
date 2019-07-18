from rest_framework import serializers
from ..models import Personal

class PersonalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personal
        fields = '__all__'
        extra_kwargs = {'user_profile' : {'read_only':True}}