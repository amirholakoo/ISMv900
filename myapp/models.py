import uuid

from django.db import models
from datetime import datetime


# Create your models here.
from django.db import models
import uuid


class Truck(models.Model):
    """
    Represents a truck used for transportation purposes.

    Attributes:
        truck_id (int): Auto-incrementing primary key for the truck.
        license_number (str): Unique license number of the truck (max length 255).
        driver_name (str, optional): Name of the driver assigned to the truck (max length 255).
        driver_doc (str, optional): doc of the driver assigned to the truck (max length 255).
        phone (str, optional): Phone number of the driver (max length 20).
        status (str): Current status of the truck (choices: 'Free', 'Busy').
        location (str, optional): Current location of the truck (max length 255).
        comments (str, optional): Additional notes or information about the truck.
    """

    truck_id = models.AutoField(primary_key=True)
    license_number = models.CharField(max_length=255, unique=True)
    driver_name = models.CharField(max_length=255, blank=True)
    driver_doc = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    status = models.CharField(max_length=10, choices=[('Free', 'Free'), ('Busy', 'Busy')], default='Free')
    location = models.CharField(max_length=255, blank=True)
    comments = models.TextField(blank=True)

    def __str__(self):
        """
        Returns a human-readable representation of the Truck object.

        Format: "Truck {license_number} - {status}"
        """
        return f"Truck {self.license_number} - {self.status}"




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
    net_weight = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    list_of_reels = models.TextField(null=True)
    profile_name = models.CharField(max_length=225, null=True)
    sales_id = models.IntegerField(null=True)
    price_per_kg = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    extra_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    supplier_id = models.IntegerField(null=True)
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


class Supplier(models.Model):
    supplier_id = models.AutoField(primary_key=True)
    supplier_name = models.CharField(max_length=255, null=False)
    address = models.TextField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    status = models.CharField(max_length=255, blank=True)
    comments = models.TextField(blank=True)

    def __str__(self):
        return self.supplier_name


class Products(models.Model):
    """
    Represents a product record in the system.
    Each record includes details about a product, such as its dimensions, grade,
    and various attributes related to its physical properties and status.
    """
    # Reel number for the product, used as the primary key
    reel_number = models.CharField(max_length=255, primary_key=True)

    # Width of the product
    width = models.IntegerField()

    # GSM (Grams per Square Meter) of the product
    gsm = models.IntegerField()

    # Length of the product
    length = models.IntegerField()

    # Grade of the product
    grade = models.CharField(max_length=255)

    # Breaks of the product
    breaks = models.CharField(max_length=255)

    # Additional comments about the product
    comments = models.TextField(null=True, blank=True)

    # QR code associated with the product
    qr_code = models.TextField(null=True, blank=True)

    # Default location of the product
    location = models.CharField(max_length=255, default='Anbar_Salon_Tolid')

    # Status of the product
    STATUS_CHOICES = [
        ('In-stock', 'In-stock'),
        ('Sold', 'Sold'),
        ('Moved', 'Moved'),
        ('Delivered', 'Delivered'),
    ]
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)

    # Date and time when the product was received
    receive_date = models.DateTimeField()

    # Last date the product was updated
    last_date = models.DateTimeField()

    # Profile name for the product
    profile_name = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        """
        Metadata for the Products model.
        """
        db_table = 'Products'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return f"Product (Reel Number: {self.reel_number}, Status: {self.status})"


class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=255, null=False)
    address = models.TextField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    status = models.CharField(max_length=255, blank=True)
    comments = models.TextField(blank=True)

    def __str__(self):
        return self.customer_name


class RawMaterial(models.Model):
    """
    Represents a raw material used in production.

    Attributes:
        material_id (int): Auto-incrementing primary key for the raw material.
        supplier (ForeignKey): Foreign key to the Supplier model representing the raw material's source.
        material_type (str): Type of the raw material (e.g., cotton, wool, plastic).
        material_name (str): Name of the specific raw material (e.g., Pima cotton, Merino wool).
        description (str, optional): Optional description of the raw material and its properties.
        status (str): Current status of the raw material (e.g., available, low stock, discontinued).
        comments (str, optional): Additional comments or notes about the raw material.
    """

    material_id = models.AutoField(primary_key=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True, related_name='raw_materials')
    material_type = models.CharField(max_length=255)
    material_name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)
    status = models.CharField(max_length=255)
    comments = models.TextField(blank=True)

    def __str__(self):
        """
        Returns a human-readable representation of the RawMaterial object.

        Format: "{material_name} (ID: {material_id})"
        """
        return f"{self.material_name} (ID: {self.material_id})"


class Purchases(models.Model):
    """
    Model representing a purchase with various attributes related to the purchase details.
    """

    Date = models.DateTimeField(null=True)
    ReceiveDate = models.DateTimeField(null=True)
    SupplierID = models.ForeignKey(Supplier, on_delete=models.CASCADE, null=True)
    TruckID = models.ForeignKey(Truck, on_delete=models.CASCADE, null=True)
    MaterialID = models.ForeignKey(RawMaterial, on_delete=models.CASCADE, null=True)
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
    ShipmentID = models.ForeignKey(Shipment, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"Purchase {self.TruckID}"


class Sale(models.Model):
    sale_id = models.AutoField(primary_key=True)
    date = models.DateTimeField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    truck = models.ForeignKey(Truck, on_delete=models.CASCADE)
    license_number = models.CharField(max_length=255, blank=True)
    list_of_reels = models.TextField(blank=True)
    weight1 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    weight2 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    net_weight = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    shipping_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    vat = models.CharField(max_length=255, blank=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    invoice_status = models.CharField(
        max_length=10, choices=[('Sent', 'Sent'), ('NA', 'NA')]
    )
    payment_status = models.CharField(
        max_length=10, choices=[('Paid', 'Paid'), ('Terms', 'Terms'),
                                 ('Unknown', 'Unknown'), ('Cancelled', 'Cancelled')]
    )
    invoice_number = models.CharField(max_length=255, blank=True)
    document_info = models.TextField(blank=True)
    comments = models.TextField(blank=True)
    shipment = models.ForeignKey(Shipment, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"Sale (ID: {self.sale_id}, Date: {self.date}, Customer: {self.customer})"


class AnbarGeneric(models.Model):
    """
    Abstract base model for generic anbar items.
    This model provides common fields and behaviors for all anbar items.
    """

    # Auto-incrementing primary key
    id = models.AutoField(primary_key=True)

    # Date and time when the record was received
    receive_date = models.DateTimeField(null=True, blank=True)

    # Reel number for the material
    reel_number = models.CharField(max_length=255, null=True, blank=True)

    # Foreign key to the Supplier model (assuming it exists)
    supplier_id = models.ForeignKey('Supplier', on_delete=models.SET_NULL, null=True, blank=True)

    # Name of the supplier
    supplier_name = models.CharField(max_length=255, null=True, blank=True)

    # Type of material
    material_type = models.CharField(max_length=255, null=True, blank=True)

    # Name of the material
    material_name = models.CharField(max_length=255, null=True, blank=True)

    # Description of the material
    description = models.TextField(null=True, blank=True)

    # Status of the material
    STATUS_CHOICES = [
        ('In-stock', 'In-stock'),
        ('Sold', 'Sold'),
        ('Moved', 'Moved'),
        ('Used', 'Used'),
        ('Canceled', 'Canceled'),
    ]
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, null=True, blank=True)

    # Location of the material
    location = models.CharField(max_length=255, null=True, blank=True)

    # Last date the material was updated
    last_date = models.DateTimeField(null=True, blank=True)

    # Width of the material
    width = models.IntegerField(null=True, blank=True)

    # GSM (Grams per Square Meter) of the material
    gsm = models.IntegerField(null=True, blank=True)

    # Length of the material
    length = models.IntegerField(null=True, blank=True)

    # Grade of the material
    grade = models.CharField(max_length=255, null=True, blank=True)

    # Breaks of the material
    breaks = models.CharField(max_length=255, null=True, blank=True)

    # Additional comments about the material
    comments = models.TextField(null=True, blank=True)

    # QR code associated with the material
    qr_code = models.TextField(null=True, blank=True)

    # Profile name for the material
    profile_name = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        abstract = True # Make this model abstract so it's not created in the DB


# Define the specific anbar models
class Anbar_Sangin(AnbarGeneric):
    """
    Model representing an anbar item in Sangin.
    Inherits from AnbarGeneric to reuse common fields and behaviors.
    """
    class Meta(AnbarGeneric.Meta):
        verbose_name_plural = "Anbar Sangin"

    def __str__(self):
        return f"{self.material_name} ({self.reel_number})"


class Anbar_Salon_Tolid(AnbarGeneric):
    """
    Model representing an anbar item in Salon Tolid.
    Inherits from AnbarGeneric to reuse common fields and behaviors.
    """
    class Meta(AnbarGeneric.Meta):
        verbose_name_plural = "Anbar Salon Tolid"

    def __str__(self):
        return f"{self.material_name} ({self.reel_number})"


class Anbar_Parvandeh(AnbarGeneric):
    """
    Model representing an anbar item in Parvandeh.
    Inherits from AnbarGeneric to reuse common fields and behaviors.
    """
    class Meta(AnbarGeneric.Meta):
        verbose_name_plural = "Anbar Parvandeh"

    def __str__(self):
        return f"{self.material_name} ({self.reel_number})"


class Anbar_Koochak(AnbarGeneric):
    """
    Model representing an anbar item in Koochak.
    Inherits from AnbarGeneric to reuse common fields and behaviors.
    """
    class Meta(AnbarGeneric.Meta):
        verbose_name_plural = "Anbar Koochak"

    def __str__(self):
        return f"{self.material_name} ({self.reel_number})"


class Anbar_Khamir_Ghadim(AnbarGeneric):
    """
    Model representing an anbar item in Khamir Ghadim.
    Inherits from AnbarGeneric to reuse common fields and behaviors.
    """
    class Meta(AnbarGeneric.Meta):
        verbose_name_plural = "Anbar Khamir Ghadim"

    def __str__(self):
        return f"{self.material_name} ({self.reel_number})"


class Anbar_Khamir_Kordan(AnbarGeneric):
    """
    Model representing an anbar item in Khamir Kordan.
    Inherits from AnbarGeneric to reuse common fields and behaviors.
    """
    class Meta(AnbarGeneric.Meta):
        verbose_name_plural = "Anbar Khamir Kordan"

    def __str__(self):
        return f"{self.material_name} ({self.reel_number})"


class Anbar_Muhvateh_Kardan(AnbarGeneric):
    """
    Model representing an anbar item in Muhvateh Kardan.
    Inherits from AnbarGeneric to reuse common fields and behaviors.
    """
    class Meta(AnbarGeneric.Meta):
        verbose_name_plural = "Anbar Muhvateh Kardan"

    def __str__(self):
        return f"{self.material_name} ({self.reel_number})"


class Anbar_Akhal(AnbarGeneric):
    """
    Model representing an anbar item in Akhal.
    Inherits from AnbarGeneric to reuse common fields and behaviors.
    """
    class Meta(AnbarGeneric.Meta):
        verbose_name_plural = "Anbar Akhal"

    def __str__(self):
        return f"{self.material_name} ({self.reel_number})"


class Consumption(models.Model):
    """
    Represents a consumption record in the system.
    Each record includes details about the material consumed,
    such as the supplier, material type, and quantity.
    """
    # Auto-incrementing primary key
    consumption_id = models.AutoField(primary_key=True)

    # Date and time when the consumption was recorded
    receive_date = models.DateTimeField(null=True, blank=True)

    # Foreign key to the Supplier model (assuming it exists)
    supplier_id = models.ForeignKey('Supplier', on_delete=models.SET_NULL, null=True, blank=True)

    # Name of the supplier
    supplier_name = models.CharField(max_length=255, null=True, blank=True)

    # Type of material consumed
    material_type = models.CharField(max_length=255, null=True, blank=True)

    # Name of the material consumed
    material_name = models.CharField(max_length=255, null=True, blank=True)

    # Unit of measurement for the material
    unit = models.CharField(max_length=255, null=True, blank=True)

    # Reel number for the material
    reel_number = models.CharField(max_length=255, null=True, blank=True)

    # Profile name for the material
    profile_name = models.CharField(max_length=255, null=True, blank=True)

    # Additional comments about the consumption
    comments = models.TextField(null=True, blank=True)

    # Status of the consumption
    status = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"Consumption (ID: {self.consumption_id}, Date: {self.date}, profile name: {self.profile_name})"


class MaterialType(models.Model):
    """
    Represents a type of material used in production.

    Attributes:
        material_type_id (int): Auto-incrementing primary key for the material type.
        name (str): Name of the material type (unique).
        username_created (str, optional): Username of the user who created the material type (not enforced in this implementation).
        created_on (datetime): Date and time the material type was created.
        status (str, default="Active"): Current status of the material type (e.g., Active, Archived).
    """

    material_type_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    username_created = models.CharField(max_length=255, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255, default="Active")

    def __str__(self):
        """
        Returns a human-readable representation of the MaterialType object.
        """
        return self.name


class Unit(models.Model):
    """
    Represents a unit of measurement for quantities.

    Attributes:
        unit_id (int): Auto-incrementing primary key for the unit.
        name (str): Name of the unit (unique).
        count_kg (float, optional): Value representing the unit's capacity in kilograms (e.g., 25 for 25kg bag).
        username_created (str, blank=True): Username of the user who created the unit (optional).
        created_on (datetime): Date and time the unit was created.
        status (str, default="Active"): Current status of the unit (e.g., Active, Archived).
    """

    unit_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    count_kg = models.FloatField(blank=True, null=True)
    username_created = models.CharField(max_length=255, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255, default="Active")

    def __str__(self):
        return self.name

