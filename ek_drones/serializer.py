from rest_framework import serializers
from .models import InfoRequest


class InfoRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfoRequest
        fields = ['name', 'company', 'email', 'phone', 'message']
        phone = serializers.CharField(required=False, allow_blank=True, allow_null=True)
        message = serializers.CharField(required=False, allow_blank=True, allow_null=True)
