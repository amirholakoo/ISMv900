from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from datetime import datetime
from .models import *

class TruckTest(TestCase):

    def test_create_and_retrieve_truck(self):
        truck = Truck.objects.create(
            license_number="ABC123",
            driver_name="John Doe",
            phone="123-456-7890",
            status="Free",
            location="Warehouse",
        )

        retrieved_truck = Truck.objects.get(license_number="ABC123")

        self.assertEqual(truck, retrieved_truck)
        self.assertEqual(truck.license_number, "ABC123")
        self.assertEqual(truck.driver_name, "John Doe")
        self.assertEqual(truck.phone, "123-456-7890")
        self.assertEqual(truck.status, "Free")
        self.assertEqual(truck.location, "Warehouse")

        # Add more assertions for other fields and functionalities as needed


class SupplierTest(TestCase):

    def test_create_supplier(self):
        supplier = Supplier.objects.create(
            supplier_name="Test Supplier",
            address="123 Main Street, Anytown, USA",
            phone="555-555-1234",
            status="Active",
            comments="This is a test supplier."
        )

        self.assertEqual(supplier.supplier_name, "Test Supplier")
        self.assertEqual(supplier.address, "123 Main Street, Anytown, USA")
        self.assertEqual(supplier.phone, "555-555-1234")
        self.assertEqual(supplier.status, "Active")
        self.assertEqual(supplier.comments, "This is a test supplier.")

        # Add more assertions for other fields as needed


class ShipmentModelTest(TestCase):

    def setUp(self):
        self.truck = Truck.objects.create(license_number="ABC123")  # Assuming Truck model exists
        self.customer = Customer.objects.create(name="John Doe")  # Assuming Customer model exists
        self.supplier = Supplier.objects.create(name="Acme Company")  # Assuming Supplier model exists

    def test_create_shipment(self):
        shipment = Shipment.objects.create(
            shipment_type="Outgoing",
            status="Registered",
            location="Entrance",
            truck=self.truck,
            license_number="ABC123",
            receive_date=datetime.now(),
            entry_time=datetime.now(),
            customer=self.customer,
            customer_name="John Doe",
            quantity=100,
            material_type="Cotton",
            material_name="Raw Cotton",
            purchase_id=1,
            vat=10.0,
            invoice_status="Sent",
            payment_status="Terms",
        )

        self.assertEqual(shipment.shipment_type, "Outgoing")
        self.assertEqual(shipment.status, "Registered")
        self.assertEqual(shipment.location, "Entrance")
        self.assertEqual(shipment.truck, self.truck)
        self.assertEqual(shipment.license_number, "ABC123")
        self.assertEqual(shipment.receive_date.date(), datetime.now().date())
        self.assertTrue(shipment.entry_time)
        self.assertEqual(shipment.customer, self.customer)
        self.assertEqual(shipment.customer_name, "John Doe")
        self.assertEqual(shipment.quantity, 100)
        self.assertEqual(shipment.material_type, "Cotton")
        self.assertEqual(shipment.material_name, "Raw Cotton")
        self.assertEqual(shipment.purchase_id, 1)
        self.assertEqual(shipment.vat, 10.0)
        self.assertEqual(shipment.invoice_status, "Sent")
        self.assertEqual(shipment.payment_status, "Terms")

    def test_invalid_shipment_type(self):
        with self.assertRaises(ValueError):
            Shipment.objects.create(shipment_type="Invalid Type")

    def test_invalid_status(self):
        with self.assertRaises(ValueError):
            Shipment.objects.create(status="Invalid Status")

    def test_invalid_location(self):
        with self.assertRaises(ValueError):
            Shipment.objects.create(location="Invalid Location")

    def test_invalid_invoice_status(self):
        with self.assertRaises(ValueError):
            Shipment.objects.create(invoice_status="Invalid Invoice Status")

    def test_invalid_payment_status(self):
        with self.assertRaises(ValueError):
            Shipment.objects.create(payment_status="Invalid Payment Status")


from django.test import TestCase
from django.utils import timezone
from .models import Products

class ProductsModelTest(TestCase):
    """
    Test case for the Products model.
    """

    def setUp(self):
        """
        Set up the test environment.
        """
        # Create a Products instance
        self.product = Products.objects.create(
            reel_number='RN123',
            width=25,
            gsm=80,
            length=100,
            grade='A',
            breaks='None',
            comments='Test Comments',
            qr_code='Test QR Code',
            location='Anbar_Salon_Tolid',
            status='In-stock',
            receive_date=timezone.now(),
            last_date=timezone.now(),
            profile_name='Test Profile'
        )

    def test_create_product(self):
        """
        Test creating a Products instance.
        """
        self.assertIsInstance(self.product, Products)
        self.assertEqual(self.product.__str__(), 'Product (Reel Number: RN123, Status: In-stock)')

    def test_update_product(self):
        """
        Test updating a Products instance.
        """
        self.product.status = 'Sold'
        self.product.save()

        self.product.refresh_from_db()
        self.assertEqual(self.product.status, 'Sold')

    def test_delete_product(self):
        """
        Test deleting a Products instance.
        """
        self.product.delete()
        with self.assertRaises(Products.DoesNotExist):
            Products.objects.get(reel_number='RN123')

    def test_product_status_choices(self):
        """
        Test that the status field only accepts valid choices.
        """
        with self.assertRaises(ValueError):
            Products.objects.create(
                reel_number='RN456',
                width=25,
                gsm=80,
                length=100,
                grade='A',
                breaks='None',
                comments='Test Comments',
                qr_code='Test QR Code',
                location='Anbar_Salon_Tolid',
                status='InvalidStatus', # This should raise a ValueError
                receive_date=timezone.now(),
                last_date=timezone.now(),
                profile_name='Test Profile'
            )
