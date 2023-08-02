from rest_framework import serializers
from .models import InfoRequest


class InfoRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfoRequest
        fields = ['name', 'company', 'email', 'phone', 'message']
        name = serializers.CharField(required=False, allow_blank=True)
        company = serializers.CharField(required=False, allow_blank=True)
        email = serializers.CharField(required=False, allow_blank=True)
        phone = serializers.CharField(required=False, allow_blank=True)
        message = serializers.CharField(required=False, allow_blank=True)
