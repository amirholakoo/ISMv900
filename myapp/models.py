from django.utils import timezone
from datetime import datetime
from django.db import models
# Create your models here.


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

    id = models.AutoField(primary_key=True)
    license_number = models.CharField(max_length=255, unique=True)
    driver_name = models.CharField(max_length=255, blank=True)
    driver_doc = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    status = models.CharField(max_length=10, choices=[('Free', 'Free'), ('Busy', 'Busy')], default='Free')
    location = models.CharField(max_length=255, blank=True)
    comments = models.TextField(blank=True)
    logs = models.TextField(blank=True)

    def __str__(self):
        """
        Returns a human-readable representation of the Truck object.

        Format: "Truck {license_number} - {status}"
        """
        return f"Truck {self.license_number} - {self.status}"


class Shipments(models.Model):
    """
    Model representing a shipment record.
    """
    # Fields
    id = models.AutoField(primary_key=True)
    shipment_type = models.CharField(max_length=255, choices=[('Incoming', 'Incoming'), ('Outgoing', 'Outgoing')], null=True)
    status = models.CharField(max_length=255, choices=[('Registered', 'Registered'), ('LoadingUnloading', 'LoadingUnloading'), ('LoadedUnloaded', 'LoadedUnloaded'), ('Offiffice', 'Offiffice'), ('Delivered', 'Delivered'), ('Canceled', 'Canceled')], null=True)
    location = models.CharField(max_length=255, choices=[('Entrance', 'Entrance'), ('Weight1', 'Weight1'), ('Weight2', 'Weight2'), ('Offiffice', 'Offiffice'), ('Delivered', 'Delivered')], null=True)
    truck_id = models.IntegerField(null=True)
    license_number = models.CharField(max_length=255, null=True)
    receive_date = models.DateTimeField(blank=True, null=True)
    entry_time = models.DateTimeField(blank=True, null=True)
    customer_name = models.CharField(max_length=255, null=True)
    supplier_name = models.CharField(max_length=255, null=True)
    weight1 = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    weight1_time = models.DateTimeField(blank=True, null=True)
    unload_location = models.CharField(max_length=255, null=True)
    unit = models.CharField(max_length=255, null=True)
    quantity = models.IntegerField(null=True)
    quality = models.CharField(max_length=255, null=True)
    penalty = models.CharField(max_length=255, null=True)
    weight2 = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    weight2_time = models.DateTimeField(blank=True, null=True)
    net_weight = models.CharField(max_length=10, null=True)
    list_of_reels = models.TextField(null=True)
    profile_name = models.CharField(max_length=255, null=True)
    sales_id = models.IntegerField(null=True)
    price_per_kg = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    extra_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    supplier_id = models.IntegerField(null=True)
    material_id = models.IntegerField(null=True)
    material_type = models.CharField(max_length=255, null=True)
    material_name = models.CharField(max_length=255, null=True)
    purchase_id = models.IntegerField(null=True)
    vat = models.DecimalField(max_digits=10, decimal_places=2, null=True) # Assuming VAT is a decimal field
    invoice_status = models.CharField(max_length=255, choices=[('NA', 'NA'), ('Sent', 'Sent'), ('Received', 'Received')], null=True)
    payment_status = models.CharField(max_length=255, choices=[('Terms', 'Terms'), ('Paid', 'Paid')], null=True)
    exit_time = models.DateTimeField(blank=True, null=True)
    document_info = models.TextField(null=True)
    comments = models.TextField(null=True)
    cancellation_reason = models.TextField(null=True)

    # Meta
    class Meta:
        db_table = 'Shipments'

    def __str__(self):
        """
        String representation of the Shipment instance.
        """
        return f"Shipment {self.shipment_id} ({self.shipment_type})"


class Supplier(models.Model):
    id = models.AutoField(primary_key=True)
    supplier_name = models.CharField(max_length=255, null=False)
    address = models.TextField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    status = models.CharField(max_length=255, blank=True)
    comments = models.TextField(blank=True)
    logs = models.TextField(blank=True)

    def __str__(self):
        return f"{self.supplier_name} (ID: {self.status})"


class Products(models.Model):
    """
    Represents a product record in the system.
    Each record includes details about a product, such as its dimensions, grade,
    and various attributes related to its physical properties and status.
    """
    id = models.AutoField(primary_key=True)
    # Reel number for the product
    reel_number = models.CharField(max_length=255)

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
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='In-stock')

    # Date and time when the product was received
    receive_date = models.DateTimeField(blank=True, null=True)

    # Last date the product was updated
    last_date = models.DateTimeField(blank=True, null=True)

    # Profile name for the product
    profile_name = models.CharField(max_length=255, null=True, blank=True)
    logs = models.TextField(blank=True)

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
    id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=255, null=False)
    address = models.TextField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    status = models.CharField(max_length=255, blank=True)
    comments = models.TextField(blank=True)
    logs = models.TextField(blank=True)

    def __str__(self):
        return f"{self.customer_name} (ID: {self.status})"


class RawMaterial(models.Model):
    """
    Represents a raw material used in production.

    Attributes:
        id (int): Auto-incrementing primary key for the raw material.
        supplier (ForeignKey): Foreign key to the Supplier model representing the raw material's source.
        material_type (str): Type of the raw material (e.g., cotton, wool, plastic).
        material_name (str): Name of the specific raw material (e.g., Pima cotton, Merino wool).
        description (str, optional): Optional description of the raw material and its properties.
        status (str): Current status of the raw material (e.g., available, low stock, discontinued).
        comments (str, optional): Additional comments or notes about the raw material.
    """

    id = models.AutoField(primary_key=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True, related_name='raw_materials')
    material_type = models.CharField(max_length=255)
    material_name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)
    status = models.CharField(max_length=255)
    comments = models.TextField(blank=True)
    logs = models.TextField(blank=True)

    def __str__(self):
        """
        Returns a human-readable representation of the RawMaterial object.

        Format: "{material_name} (ID: {material_id})"
        """
        return f"{self.material_name} (ID: {self.material_id})  (ID: {self.supplier}) (ID: {self.status})"


class Purchases(models.Model):
    """
    Represents a purchase transaction in the inventory management system.

    Fields:
        purchase_id (int): Unique identifier for the purchase (auto-incrementing).
        date (datetime): Date of the purchase.
        receive_date (datetime): Date the purchase was received.
        supplier (ForeignKey): Reference to the Supplier who provided the materials.
        truck (ForeignKey): Reference to the Truck that delivered the materials (optional).
        material (ForeignKey): Reference to the specific material purchased.
        material_type (CharField): Type of material (e.g., "Wood", "Steel").
        material_name (CharField): Name of the material.
        unit (CharField): Unit of measurement (e.g., "Kg", "Litre").
        quantity (IntegerField): Quantity of the material purchased.
        quality (CharField): Quality of the material (e.g., "Good", "Fair").
        penalty (CharField): Any penalty or fee associated with the purchase (optional).
        weight1 (DecimalField): First weight measurement (optional).
        weight2 (DecimalField): Second weight measurement (optional).
        net_weight (DecimalField): Calculated net weight of the material.
        price_per_kg (DecimalField): Price per kilogram of the material.
        vat (DecimalField): Value-Added Tax (optional).
        total_price (DecimalField): Total price of the purchase, including VAT.
        extra_cost (DecimalField): Any additional costs incurred (optional).
        invoice_status (CharField): Status of the invoice (e.g., "Received", "NA"). Choices: 'RECEIVED', 'NA'
        status (CharField): Status of the payment (e.g., "Paid", "Terms", "Cancelled"). Choices: 'PAID', 'TERMS', 'CANCELLED'
        payment_details (TextField): Details about the payment method (optional).
        payment_date (datetime): Date the payment was made (optional).
        invoice_number (CharField): Invoice number associated with the purchase.
        document_info (TextField): Additional information from documents (optional).
        comments (TextField): Comments or notes related to the purchase.
        cancellation_reason (TextField): Reason for cancellation, if applicable.
        shipment (ForeignKey): Reference to the Shipment related to the purchase (optional).

    """
    # Fields
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField(default=timezone.now, blank=True)
    receive_date = models.DateTimeField(blank=True, null=True)

    supplier_id = models.ForeignKey('Supplier', on_delete=models.SET_NULL, blank=True, null=True)
    truck_id = models.ForeignKey('Truck', on_delete=models.SET_NULL, blank=True, null=True)
    material_id = models.ForeignKey('Material', on_delete=models.SET_NULL, blank=True, null=True)

    material_type = models.CharField(max_length=255, blank=True, null=True)
    material_name = models.CharField(max_length=255, blank=True, null=True)
    unit = models.CharField(max_length=255, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)

    quality = models.CharField(max_length=255, blank=True, null=True)
    penalty = models.CharField(max_length=255, blank=True, null=True)

    weight1 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    weight2 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    net_weight = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    price_per_kg = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)

    # VAT field needs further information on data type
    vat = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    extra_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    invoice_status = models.CharField(max_length=7, choices=[('Received', 'Received'), ('NA', 'NA')], blank=True, null=True)
    status = models.CharField(max_length=5, choices=[('Paid', 'Paid'), ('Terms', 'Terms'), ('Cancelled', 'Cancelled')], blank=True, null=True)

    payment_details = models.CharField(max_length=255, blank=True, null=True)
    payment_date = models.DateTimeField(blank=True, null=True)

    invoice_number = models.CharField(max_length=255, blank=True, null=True)
    document_info = models.TextField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    cancellation_reason = models.TextField(blank=True, null=True)

    shipment_id = models.ForeignKey('Shipment', on_delete=models.SET_NULL, blank=True, null=True)
    logs = models.TextField(blank=True)

    class Meta:
        db_table = "Purchases"

    def __str__(self):
        """
        String representation of the Purchase instance.
        """
        return f"Purchase {self.purchase_id} on {self.date}"


class Sales(models.Model):
    """
    Model representing a sales record.

    Each instance of this model represents a sale transaction, including details such as the date of the sale, the customer involved, the truck used, and various financial details. The model also includes references to related entities such as the customer, truck, and shipment involved in the sale.

    Fields:
    - sale_id: An auto-incrementing primary key for each sale record.
    - date: The date and time when the sale was made.
    - customer: A foreign key to the Customers model, representing the customer involved in the sale.
    - truck: A foreign key to the Trucks model, representing the truck used in the sale.
    - license_number: The license number of the truck used in the sale.
    - list_of_reels: A text field containing a list of reels involved in the sale.
    - profile_name: The name of the profile associated with the sale.
    - weight1, weight2, net_weight: Decimal fields representing various weights associated with the sale.
    - price_per_kg: A decimal field representing the price per kilogram for the sale.
    - vat: A decimal field representing the VAT amount for the sale.
    - total_price: A decimal field representing the total price of the sale.
    - extra_cost: A decimal field representing any extra costs associated with the sale.
    - invoice_status: A char field indicating the status of the invoice, with choices for 'Sent' and 'NA'.
    - invoice_number: A char field containing the invoice number for the sale.
    - status: A char field indicating the status of the sale, with choices for 'Paid', 'Terms', and 'Cancelled'.
    - payment_details: A char field containing details about the payment made for the sale.
    - payment_date: A datetime field representing the date and time when the payment was made.
    - document_info: A text field containing information about any documents associated with the sale.
    - comments: A text field for any comments or notes about the sale.
    - cancellation_reason: A text field containing the reason for cancellation, if applicable.
    - shipment: A foreign key to the Shipments model, representing the shipment associated with the sale.

    Relationships:
    - Each sale is related to one customer, one truck, and one shipment.
    - The customer, truck, and shipment fields are foreign keys, establishing a relationship with the Customers, Trucks, and Shipments models, respectively.
    """
    # Fields
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField(null=True)
    customer = models.ForeignKey('Customers', on_delete=models.CASCADE, null=True)
    truck = models.ForeignKey('Trucks', on_delete=models.CASCADE, null=True)
    license_number = models.CharField(max_length=255, null=True)
    list_of_reels = models.TextField(null=True)
    profile_name = models.CharField(max_length=255, null=True)
    weight1 = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    weight2 = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    net_weight = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    price_per_kg = models.DecimalField(max_digits=10, decimal_places=0, null=True)
    vat = models.DecimalField(max_digits=10, decimal_places=2, null=True) # Assuming VAT is a decimal field
    total_price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    extra_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    invoice_status = models.CharField(max_length=255, choices=[('Sent', 'Sent'), ('NA', 'NA')], null=True)
    invoice_number = models.CharField(max_length=255, null=True)
    status = models.CharField(max_length=255, choices=[('Paid', 'Paid'), ('Terms', 'Terms'), ('Cancelled', 'Cancelled')], null=True)
    payment_details = models.CharField(max_length=255, null=True)
    payment_date = models.DateTimeField(null=True)
    document_info = models.TextField(null=True)
    comments = models.TextField(null=True)
    cancellation_reason = models.TextField(null=True)
    shipment = models.ForeignKey('Shipments', on_delete=models.CASCADE, null=True)
    logs = models.TextField(blank=True)
    # Meta
    class Meta:
        db_table = 'Sales'

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
    location = models.CharField(max_length=255, null=True, blank=True, default='Entrance')

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

    logs = models.TextField(blank=True)

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
    id = models.AutoField(primary_key=True)

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

    logs = models.TextField(blank=True)

    def __str__(self):
        """
        String representation of the Consumption instance.
        """
        return f"Consumption {self.consumption_id}: {self.supplier_name} - {self.material_type} - {self.material_name}"


class MaterialType(models.Model):
    """
    MaterialType model represents different types of materials supplied by suppliers.

    Fields:
    - id: Auto-incrementing primary key.
    - supplier_name: Name of the supplier. Can be null or blank.
    - material_type: Type of material. Required field.
    - username: Username associated with the material type. Can be null or blank.
    - data: Date and time when the material type was added. Auto-populated on creation.
    """
    id = models.AutoField(primary_key=True)
    supplier_name = models.CharField(max_length=255, null=True, blank=True)
    # Ensure material_type is always provided to avoid empty entries
    material_type = models.CharField(max_length=255)
    username = models.CharField(max_length=255, blank=True)

    date = models.DateTimeField(default=timezone.now, blank=True)
    logs = models.TextField(blank=True)

    def __str__(self):
        """
        Returns a string representation of the MaterialType object, including the supplier name, material type, and username.
        This method is used to display a human-readable representation of the object.
        """
        return f"{self.supplier_name} - {self.material_type} - {self.username}"


class Unit(models.Model):
    """
    Represents a unit of measurement for quantities.

    Attributes:
        id (int): Auto-incrementing primary key for the unit.
        name (str): Name of the unit (unique).
        count (float, optional): Value representing the unit's capacity in kilograms (e.g., 25 for 25kg bag).
        username (str, blank=True): Username of the user who created the unit (optional).
        date (datetime): Date and time the unit was created.
    """

    id = models.AutoField(primary_key=True)
    supplier_name = models.CharField(max_length=255, null=True, blank=True)
    material_type = models.CharField(max_length=255)
    unit_name = models.CharField(max_length=255, unique=True)
    count = models.FloatField(blank=True, null=True)
    username = models.CharField(max_length=255, blank=True)
    date = models.DateTimeField(default=timezone.now, blank=True)
    logs = models.TextField(blank=True)

    def __str__(self):
        """
        Returns a string representation of the Unit object, including the Unit name, count, and username.
        This method is used to display a human-readable representation of the object.
        """
        return f"{self.supplier_name} - {self.count} - {self.username}"

