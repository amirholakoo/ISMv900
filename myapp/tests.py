from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from datetime import datetime
from django.utils import timezone
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


class CustomerModelTest(TestCase):
    """
    Test case for the Customer model.
    """

    def setUp(self):
        """
        Set up the test environment.
        """
        # Create a Customer instance
        self.customer = Customer.objects.create(
            customer_name='Test Customer',
            address='123 Test Street',
            phone='123-456-7890',
            status='Active',
            comments='Test Comments'
        )

    def test_create_customer(self):
        """
        Test creating a Customer instance.
        """
        self.assertIsInstance(self.customer, Customer)
        self.assertEqual(self.customer.__str__(), 'Test Customer')

    def test_update_customer(self):
        """
        Test updating a Customer instance.
        """
        self.customer.status = 'Inactive'
        self.customer.save()

        customer_updated = Customer.objects.get(id=self.customer.customer_id)
        self.assertEqual(customer_updated.status, 'Inactive')

    def test_delete_customer(self):
        """
        Test deleting a Customer instance.
        """
        self.customer.delete()
        with self.assertRaises(Customer.DoesNotExist):
            Customer.objects.get(id=self.customer.customer_id)

    def test_customer_str_representation(self):
        """
        Test the string representation of a Customer instance.
        """
        self.assertEqual(str(self.customer), 'Test Customer')


class RawMaterialModelTest(TestCase):
    """
    Test case for the RawMaterial model.
    """

    def setUp(self):
        """
        Set up the test environment.
        """
        # Create a supplier instance
        self.supplier = Supplier.objects.create(name='Test Supplier')

        # Create a RawMaterial instance
        self.raw_material = RawMaterial.objects.create(
            supplier=self.supplier,
            material_type='Cotton',
            material_name='Pima Cotton',
            status='Available',
            comments='High-quality cotton'
        )

    def test_create_raw_material(self):
        """
        Test creating a RawMaterial instance.
        """
        self.assertIsInstance(self.raw_material, RawMaterial)
        self.assertEqual(self.raw_material.__str__(), 'Pima Cotton (ID: 1)')

    def test_update_raw_material(self):
        """
        Test updating a RawMaterial instance.
        """
        self.raw_material.status = 'Low Stock'
        self.raw_material.save()

        self.raw_material.refresh_from_db()
        self.assertEqual(self.raw_material.status, 'Low Stock')

    def test_delete_raw_material(self):
        """
        Test deleting a RawMaterial instance.
        """
        self.raw_material.delete()
        with self.assertRaises(RawMaterial.DoesNotExist):
            RawMaterial.objects.get(id=self.raw_material.id)

    def test_get_raw_material(self):
        """
        Test retrieving a RawMaterial instance.
        """
        retrieved_material = RawMaterial.objects.get(id=self.raw_material.id)
        self.assertEqual(retrieved_material, self.raw_material)

    def test_raw_material_str(self):
        """
        Test the __str__ method of the RawMaterial model.
        """
        self.assertEqual(str(self.raw_material), 'Pima Cotton (ID: 1)')
