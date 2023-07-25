from rest_framework import serializers
from .models import InfoRequest


class InfoRequestSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('__all__')
        model = InfoRequest
