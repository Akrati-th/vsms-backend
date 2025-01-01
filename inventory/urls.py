# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ComponentViewSet, VehicleViewSet, IssueViewSet

router = DefaultRouter()
router.register(r'components', ComponentViewSet)
router.register(r'vehicles', VehicleViewSet)
router.register(r'issues', IssueViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('vehicles/<int:vehicle_id>/issues/', IssueViewSet.as_view({'post': 'create'})),
]