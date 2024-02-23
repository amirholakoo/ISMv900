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


class Purchases(models.Model):
    """
    Model representing a purchase with various attributes related to the purchase details.
    """

    Date = models.DateTimeField(null=True)
    ReceiveDate = models.DateTimeField(null=True)
    SupplierID = models.ForeignKey('Supplier', on_delete=models.CASCADE, null=True)
    TruckID = models.ForeignKey('Truck', on_delete=models.CASCADE, null=True)
    MaterialID = models.ForeignKey('Material', on_delete=models.CASCADE, null=True)
    MaterialType = models.CharField(max_length=225, null=True)
    MaterialName = models.CharField(max_length=225, null=True)
    Unit = models.CharField(max_length=225, null=True)
    Quantity = models.IntegerField(null=True)
    Quality = models.CharField(max_length=225, null=True)
    Penalty = models.CharField(max_length=225, null=True)
    Weight1 = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    Weight2 = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    NetWeight = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    PricePerKG = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    VAT = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    TotalPrice = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    ExtraCost = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    InvoiceStatus = models.CharField(max_length=10, choices=[('Received', 'Received'), ('NA', 'Not Applicable')], default=None, null=True)
    Status = models.CharField(max_length=10, choices=[('Paid', 'Paid'), ('Terms', 'Terms'), ('Cancelled', 'Cancelled')], default=None, null=True)
    PaymentDetail = models.CharField(max_length=225, null=True)
    PaymentDate = models.DateTimeField(null=True)
    InvoiceNumber = models.CharField(max_length=225, null=True)
    DocumentInfo = models.TextField(null=True)
    Comments = models.TextField(null=True)
    CancellationReason = models.TextField(null=True)
    ShipmentID = models.ForeignKey('Shipment', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"Purchase {self.TruckID}"


class Consumption(models.Model):
    """
    Model representing a consumption record with various attributes related to the consumption details.
    """
    ReceiveDate = models.DateTimeField(null=True)
    SupplierID = models.IntegerField(null=True)  # Assuming SupplierID is not a foreign key
    SupplierName = models.CharField(max_length=225, null=True)
    MaterialType = models.CharField(max_length=225, null=True)
    MaterialName = models.CharField(max_length=225, null=True)
    Unit = models.CharField(max_length=225, null=True)
    RealNumber = models.CharField(max_length=225, null=True)
    ProofProfileName = models.CharField(max_length=225, null=True)
    Comments = models.TextField(null=True)
    Status = models.CharField(max_length=50, null=True)

    def __str__(self):
        return f"Consumption {self.id}"


class Sales(models.Model):
    """
    Model representing a sales record with various attributes related to the sales details.
    """
    Date = models.DateTimeField(null=True)
    CustomerID = models.ForeignKey('Customer', on_delete=models.CASCADE, null=True)
    TruckID = models.ForeignKey('Truck', on_delete=models.CASCADE, null=True)
    LicenseNumber = models.CharField(max_length=22555, null=True)
    ListOfReels = models.TextField(null=True)
    ProofProfileName = models.CharField(max_length=22555, null=True)
    Weight1 = models.DecimalField(max_digits=1100, decimal_places=22, null=True)
    Weight2 = models.DecimalField(max_digits=1100, decimal_places=22, null=True)
    NetWeight = models.DecimalField(max_digits=1100, decimal_places=22, null=True)
    PricePerKG = models.DecimalField(max_digits=1100, decimal_places=0, null=True)
    VAT = models.DecimalField(max_digits=1100, decimal_places=0, null=True)  # Assuming VAT is a decimal field with no decimal places
    TotalPrice = models.DecimalField(max_digits=1100, decimal_places=22, null=True)
    ExtraCost = models.DecimalField(max_digits=1100, decimal_places=22, null=True)
    InvoiceStatus = models.CharField(max_length=10, choices=[('Sent', 'Sent'), ('NA', 'Not Applicable')], default=None, null=True)
    InvoiceNumber = models.CharField(max_length=22555, null=True)
    Status = models.CharField(max_length=10, choices=[('Paid', 'Paid'), ('Terms', 'Terms'), ('Cancelled', 'Cancelled')], default=None, null=True)
    PaymentDetails = models.CharField(max_length=22555, null=True)
    PaymentDate = models.DateTimeField(null=True)
    DocumentInfo = models.TextField(null=True)
    Comments = models.TextField(null=True)
    CancellationReason = models.TextField(null=True)
    ShipmentID = models.ForeignKey('Shipment', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"Sale {self.id}"
