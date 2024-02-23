import uuid

from django.db import models

# Create your models here.
from django.db import models
import uuid

class Shipment(models.Model):
    """
    Model representing a shipment with various attributes related to its status, location, and associated entities.
    """
    # Enum choices definition
    SHIPMENT_TYPE_CHOICES = [
        ('Incoming','Incoming'),
        ('Outgoing','Outgoing')
    ]
    STATUS_CHOICES = [
        ('Registered', 'Registered'),
        ('LoadingUnloading', 'Loading/Unloading'),
        ('LoadedUnloaded', 'Loaded/Unloaded'),
        ('Office', 'Office'),
        ('Delivered','Delivered'),
        ('Canceled', 'Canceled')
    ]
    LOCATION_CHOICES = [
        ('Entrance', 'Entrance'),
        ('Weight1', 'Weight1'),
        ('Weight2', 'Weight2'),
        ('Office', 'Office'),
        ('Delivered','Delivered'),
    ]
    INVOICE_STATUS_CHOICES = [
        ('NA', 'Not Applicable'),
        ('Sent', 'Sent'),
        ('Received', 'Received'),
    ]
    PAYMENT_STATUS_CHOICES = [
        ('Terms', 'Terms'),
        ('Paid', 'Paid'),
    ]
    shipment_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    shipment_type = models.CharField(max_length=10, choices=SHIPMENT_TYPE_CHOICES, default=None, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=None, null=True)
    location = models.CharField(max_length=10, choices=LOCATION_CHOICES, default=None, null=True)
    truck_id = models.IntegerField(null=True) #Assuming Truck is another model
    license_number = models.CharField(max_length=225, null=True)
    receive_date = models.DateTimeField(null=True)
    entry_time = models.DateTimeField(auto_now_add=True)
    customer_name = models.CharField(max_length=225, null=True) #Assuming Customer is another model
    supplier_name = models.CharField(max_length=225, null=True) #Assuming Supplier is another model
    weight1 = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    weight1_time = models.DateTimeField(null=True)
    unload_location = models.CharField(max_length=225, null=True)
    unit = models.CharField(max_length=225, null=True)
    quantity = models.IntegerField(null=True)
    penalty = models.CharField(max_length=225, null=True)
    weight2 = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    weight2_time = models.DateTimeField(null=True)
    net_weight = models.CharField(max_length=10, null=True)
    list_of_reels = models.TextField(null=True)
    profile_name = models.CharField(max_length=225, null=True)
    sales_id = models.IntegerField(null=True)
    price_per_kg = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    extra_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    supplier_id = models.IntegerField(null=True) # Corrected typo
    material_id = models.IntegerField(null=True)
    material_type = models.CharField(max_length=225, null=True)
    material_name = models.CharField(max_length=225, null=True)
    purchase_id = models.IntegerField(null=True)
    vat = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    invoice_status = models.CharField(max_length=10, choices=INVOICE_STATUS_CHOICES, default='NA', null=True)
    payment_status = models.CharField(max_length=10, choices=PAYMENT_STATUS_CHOICES, default=None, null=True)
    exit_time = models.DateTimeField(null=True)
    document_info = models.TextField(null=True)
    comments = models.TextField(null=True)
    cancellation_reason = models.TextField(null=True)

    def __str__(self):
        return self.license_number

