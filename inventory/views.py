# views.py
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Component, Vehicle, Issue
from .serializers import ComponentSerializer, VehicleSerializer, IssueSerializer

class ComponentViewSet(viewsets.ModelViewSet):
    queryset = Component.objects.all()
    serializer_class = ComponentSerializer


class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer


class IssueViewSet(viewsets.ModelViewSet):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer

    def create(self, request, *args, **kwargs):
        vehicle_id = self.kwargs.get('vehicle_id')

        if not vehicle_id:
            return Response({"error": "Vehicle ID is required."}, status=status.HTTP_400_BAD_REQUEST)

        data = request.data.copy()
        data['vehicle'] = vehicle_id

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

