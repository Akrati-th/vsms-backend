# serializers.py
from rest_framework import serializers
from .models import Revenue

class RevenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Revenue
        fields = ['date', 'amount']
