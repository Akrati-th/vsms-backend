# serializers.py
from rest_framework import serializers
from .models import Component, Vehicle, Issue

class ComponentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Component
        fields = ['id', 'name', 'description', 'purchase_price', 'repair_price', 'stock_quantity']


class VehicleSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['issues'] = IssueSerializer(instance.issues.all(), many=True).data
        return data

    class Meta:
        model = Vehicle
        fields = '__all__'


class IssueSerializer(serializers.ModelSerializer):
    vehicle = serializers.PrimaryKeyRelatedField(queryset=Vehicle.objects.all())
    component = serializers.PrimaryKeyRelatedField(queryset=Component.objects.all(), allow_null=True)

    class Meta:
        model = Issue
        fields = '__all__'

