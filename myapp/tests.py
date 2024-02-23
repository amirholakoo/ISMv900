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

#
# class PurchaseTest(TestCase):
#
#     def test_create_purchase(self):
#         supplier = Supplier.objects.create(supplier_name="Test Supplier")
#         truck = Truck.objects.create(license_number="ABC123")
#         material = Material.objects.create(material_type="Cotton", material_name="Raw Cotton")
#         shipment = Shipment.objects.create(status="Incoming")
#
#         purchase = Purchases.objects.create(
#             Date=datetime.now(),
#             ReceiveDate=datetime.now(),
#             SupplierID=supplier,
#             TruckID=truck,
#             MaterialID=material,
#             MaterialType="Cotton",
#             MaterialName="Raw Cotton",
#             Unit="Bale",
#             Quantity=100,
#             Weight1=1000,
#             Weight2=990,
#             NetWeight=990,
#             PricePerKG=10,
#             TotalPrice=9900,
#             InvoiceStatus="Received",
#             PaymentStatus="Paid",
#             ShipmentID=shipment,
#         )
#
#         self.assertEqual(purchase.SupplierID, supplier)
#         self.assertEqual(purchase.TruckID, truck)
#         self.assertEqual(purchase.MaterialID, material)
#         self.assertEqual(purchase.Quantity, 100)
#         self.assertEqual(purchase.NetWeight, 990)
#         self.assertEqual(purchase.TotalPrice, 9900)
#         self.assertEqual(purchase.InvoiceStatus, "Received")
#         self.assertEqual(purchase.PaymentStatus, "Paid")
#         self.assertEqual(purchase.ShipmentID, shipment)
#
#         # Add more assertions for other fields and relationships as needed
