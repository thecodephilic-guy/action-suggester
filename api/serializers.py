from rest_framework import serializers
from .models import QueryLog

class AnalyzeRequestSerializer(serializers.Serializer):
    query = serializers.CharField()

class QueryLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = QueryLog
        fields = '__all__'