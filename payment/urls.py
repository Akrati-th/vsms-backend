# urls.py
from django.urls import path
from .views import ServiceList, CalculateFinalPrice, ProcessPayment, RevenueAnalysis

urlpatterns = [
    path('services/', ServiceList.as_view(), name='service-list'),
    path('calculate/<int:vehicle_id>/', CalculateFinalPrice.as_view(), name='calculate_price'),
    path('process_payment/<int:vehicle_id>/', ProcessPayment.as_view()),
    path('analysis/', RevenueAnalysis.as_view(), name='revenue_analysis'),

]
