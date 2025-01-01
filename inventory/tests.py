# tests.py
from django.test import TestCase
from .models import Component, Vehicle, Issue

class ComponentModelTest(TestCase):
    def setUp(self):
        self.component = Component.objects.create(
            name="Brake Pad",
            description="High-quality brake pad",
            purchase_price=50.00,
            repair_price=20.00,
            stock_quantity=10
        )

    def test_component_creation(self):
        self.assertEqual(self.component.name, "Brake Pad")
        self.assertEqual(self.component.description, "High-quality brake pad")
        self.assertEqual(self.component.purchase_price, 50.00)
        self.assertEqual(self.component.repair_price, 20.00)
        self.assertEqual(self.component.stock_quantity, 10)

    def test_component_string_representation(self):
        self.assertEqual(str(self.component), "Brake Pad")


class VehicleModelTest(TestCase):
    def setUp(self):
        self.vehicle = Vehicle.objects.create(
            vin="1HGCM82633A123456",
            model="Honda Accord",
            year=2022,
            payment_status=False
        )

    def test_vehicle_creation(self):
        self.assertEqual(self.vehicle.vin, "1HGCM82633A123456")
        self.assertEqual(self.vehicle.model, "Honda Accord")
        self.assertEqual(self.vehicle.year, 2022)
        self.assertFalse(self.vehicle.payment_status)

    def test_vehicle_string_representation(self):
        self.assertEqual(str(self.vehicle), "Honda Accord (1HGCM82633A123456)")


class IssueModelTest(TestCase):
    def setUp(self):
        self.vehicle = Vehicle.objects.create(
            vin="1HGCM82633A123456",
            model="Honda Accord",
            year=2022
        )
        self.component = Component.objects.create(
            name="Brake Pad",
            description="High-quality brake pad",
            purchase_price=50.00,
            repair_price=20.00,
            stock_quantity=10
        )
        self.issue = Issue.objects.create(
            vehicle=self.vehicle,
            description="Brake issue",
            component_choice='new',
            component=self.component
        )

    def test_issue_creation(self):
        self.assertEqual(self.issue.vehicle, self.vehicle)
        self.assertEqual(self.issue.description, "Brake issue")
        self.assertEqual(self.issue.component_choice, 'new')
        self.assertEqual(self.issue.component, self.component)

    def test_issue_string_representation(self):
        self.assertEqual(str(self.issue), f"Issue for {self.vehicle.vin}: Brake issue")
