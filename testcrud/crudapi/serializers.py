from django.db.models import fields
from rest_framework import serializers
from crudapi.models import Testdjango

class TestdjangoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Testdjango
        fields = ('id',
                  'username',
                  'password')