from django.db.models import fields
from rest_framework import serializers
from boardapi.models import Board, Member

class BoardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Board
        fields = (
                'title',
                'desc',
                'writer')



class MemberSerializer(serializers.ModelSerializer):

    class Meta:
        model = Member
        fields = (
                'userid',
                'password')