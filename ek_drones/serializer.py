from rest_framework import serializers
from .models import InfoRequest


class InfoRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfoRequest
        exclude = ['created_at']
        fields = ['name', 'company', 'email', 'phone', 'message']
        name = serializers.CharField(allow_blank=True)
        company = serializers.CharField(allow_blank=True)
        email = serializers.CharField(allow_blank=True)
        phone = serializers.CharField(allow_blank=True)
        message = serializers.CharField(allow_blank=True)
