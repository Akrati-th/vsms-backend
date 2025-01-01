from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from collections import defaultdict
from django.db.models import Sum
from django.utils import timezone
from datetime import timedelta
from .services import SERVICES
from .models import Revenue
from inventory.models import Vehicle

class ServiceList(APIView):
    def get(self, request):
        return Response(SERVICES, status=status.HTTP_200_OK)


class CalculateFinalPrice(APIView):
    def get(self, request, vehicle_id):
        vehicle = Vehicle.objects.get(pk=vehicle_id)
        total_price = 0
        for service in vehicle.issues.all():
            if service.component_choice == 'new':
                total_price += service.component.purchase_price if service.component else 0
            elif service.component_choice == 'repair':
                total_price += service.component.repair_price if service.component else 0

        # Adding charges for Additional Services
        for other_services in request.data.get('services', []):
            total_price += SERVICES.get(other_services).get("approx_charges")
        return Response({'total_price': total_price}, status=status.HTTP_200_OK)
    
class ProcessPayment(APIView):
    def post(self, request, vehicle_id):
        vehicle = Vehicle.objects.get(pk=vehicle_id)
        # Add a Payment History to the Revenue Model
        payment = Revenue.objects.create(amount=request.data.get('amount'), vehicle=vehicle)

        # Update Payment Status of the Vehicle
        vehicle.payment_status = True
        vehicle.save()
        return Response("Payment Successful!", status=status.HTTP_200_OK)
    

class RevenueAnalysis(APIView):
    def get(self, request, *args, **kwargs):
        today = timezone.now().date()
        daily_revenue = Revenue.objects.values('date').annotate(revenue=Sum('amount')).order_by('date')
        
        weekly_revenue = Revenue.objects.filter(date__gte=today - timedelta(days=30))
        weekly_revenue_data = defaultdict(float)
        for revenue in weekly_revenue:
            week_number = (revenue.date - today).days // 7 + 1
            weekly_revenue_data[week_number] += revenue.amount
        
        monthly_revenue = Revenue.objects.filter(date__gte=today.replace(day=1)).values('date__month').annotate(revenue=Sum('amount')).order_by('date__month')
        
        return Response({
            'daily_revenue': daily_revenue,
            'weekly_revenue': [{"week": f"Week {week}", "revenue": revenue} for week, revenue in weekly_revenue_data.items()],
            'monthly_revenue': monthly_revenue
        })
