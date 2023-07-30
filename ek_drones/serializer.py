from rest_framework import serializers
from .models import InfoRequest


class InfoRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfoRequest
        exclude = ['created_at']
