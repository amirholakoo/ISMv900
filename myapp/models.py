from django.utils import timezone
from django.db import models

class Truck(models.Model):
    """
    Represents a truck used for transportation purposes.

    Attributes:
        id (int): Auto-incrementing primary key for the truck.
        license_number (str): Unique license number of the truck (max length 255).
        driver_name (str, optional): Name of the driver assigned to the truck (max length 255).
        driver_doc (str, optional): doc of the driver assigned to the truck (max length 255).
        phone (str, optional): Phone number of the driver (max length 20).
        status (str): Current status of the truck (choices: 'Free', 'Busy').
        location (str, optional): Current location of the truck (max length 255).
        username (str, optional): username.
    """
    date = models.DateTimeField(default=timezone.now, blank=True)
    status = models.CharField(max_length=10, choices=[('Free', 'Free'), ('Busy', 'Busy')], default='Free')
    location = models.CharField(max_length=255, blank=True, default='Entrance')

    license_number = models.CharField(max_length=255, unique=True)
    driver_name = models.CharField(max_length=255, blank=True)
    driver_doc = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=20, blank=True)

    username = models.CharField(max_length=255, null=False, blank=True)
    logs = models.TextField(blank=True)

    # Meta
    class Meta:
        db_table = 'Truck'

    def __str__(self):
        """
        Returns a human-readable representation of the Truck object.

        Format: "Truck {license_number} - {status}"
        """
        return f"Truck {self.license_number} - {self.status} - {self.driver_name} - {self.location}"


class Shipments(models.Model):
    """
    Model representing a shipment record.
    """
    # Fields
    date = models.DateTimeField(default=timezone.now, blank=True)
    status = models.CharField(max_length=255, choices=[('Registered', 'Registered'), ('LoadingUnloading', 'LoadingUnloading'), ('LoadedUnloaded', 'LoadedUnloaded'), ('Office', 'Office'), ('Delivered', 'Delivered'), ('Cancelled', 'Cancelled')], null=True)
    location = models.CharField(max_length=255, null=True)
    receive_date = models.DateTimeField(blank=True, null=True)
    entry_time = models.DateTimeField(blank=True, null=True, default=timezone.now)
    weight1_time = models.DateTimeField(blank=True, null=True)
    weight2_time = models.DateTimeField(blank=True, null=True)
    exit_time = models.DateTimeField(blank=True, null=True)

    shipment_type = models.CharField(max_length=255, choices=[('Incoming', 'Incoming'), ('Outgoing', 'Outgoing')], null=True)
    # truck_id = models.ForeignKey(Truck, on_delete=models.SET_NULL, blank=True, null=True)
    license_number = models.CharField(max_length=255,null=True)
    customer_name = models.CharField(max_length=255, null=True)
    supplier_name = models.CharField(max_length=255, null=True)
    weight1 = models.IntegerField(null=True)
    unload_location = models.CharField(max_length=255, null=True)
    unit = models.CharField(max_length=255, null=True)
    quantity = models.IntegerField(null=True)
    quality = models.CharField(max_length=255, null=True)
    penalty = models.CharField(max_length=255, null=True)
    weight2 = models.IntegerField(null=True)
    net_weight = models.CharField(max_length=10, null=True)
    list_of_reels = models.TextField(null=True)
    profile_name = models.CharField(max_length=255, null=True)
    width = models.IntegerField(null=True, blank=True)
    sales_id = models.IntegerField(null=True)
    price_per_kg = models.BigIntegerField(null=True)
    total_price = models.BigIntegerField(null=True)
    extra_cost = models.BigIntegerField(null=True)
    # supplier_id = models.IntegerField(null=True)
    # material_id = models.IntegerField(null=True)
    material_type = models.CharField(max_length=255, null=True)
    material_name = models.CharField(max_length=255, null=True)
    purchase_id = models.ForeignKey('Purchases', on_delete=models.SET_NULL, blank=True, null=True)
    vat = models.IntegerField(null=True)
    invoice_status = models.CharField(max_length=255, choices=[('NA', 'NA'), ('Sent', 'Sent'), ('Received', 'Received')], null=True)
    payment_status = models.CharField(max_length=255, choices=[('Terms', 'Terms'), ('Paid', 'Paid')], null=True)
    document_info = models.TextField(null=True)
    comments = models.TextField(null=True)
    cancellation_reason = models.TextField(null=True)

    username = models.CharField(max_length=255, null=False, blank=True)
    logs = models.TextField(blank=True)

    # Meta
    class Meta:
        db_table = 'Shipments'
        verbose_name = 'Shipment'

    def __str__(self):
        """
        String representation of the Shipment instance.
        """
        return f"{self.receive_date} - {self.shipment_type} - {self.license_number} - {self.supplier_name} - {self.customer_name} - {self.material_type} - {self.material_name} - {self.status} - {self.location}"


class Supplier(models.Model):
    date = models.DateTimeField(default=timezone.now, blank=True)
    status = models.CharField(max_length=255, blank=True, default='Active')
    supplier_name = models.CharField(max_length=255, null=False)
    address = models.TextField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    comments = models.TextField(blank=True)
    username = models.CharField(max_length=255, null=False, blank=True)
    logs = models.TextField(blank=True)

    # Meta
    class Meta:
        db_table = 'Supplier'

    def __str__(self):
        return f"{self.supplier_name} - {self.status}"


class Products(models.Model):
    """
    Represents a product record in the system.
    Each record includes details about a product, such as its dimensions, grade,
    and various attributes related to its physical properties and status.
    """
    date = models.DateTimeField(default=timezone.now, blank=True)


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

    # Reel number for the product
    reel_number = models.CharField(max_length=255, unique=True)

    # Width of the product
    width = models.IntegerField()

    # GSM (Grams per Square Meter) of the product
    gsm = models.IntegerField()

    # Length of the product
    length = models.IntegerField()

    # Grade of the product
    grade = models.CharField(max_length=255)

    # Breaks of the product
    breaks = models.IntegerField()

    # Additional comments about the product
    comments = models.TextField(null=True, blank=True)

    # QR code associated with the product
    qr_code = models.TextField(null=True, blank=True)


    # Profile name for the product
    profile_name = models.CharField(max_length=255, null=True, blank=True)

    shipment_id = models.ForeignKey(Shipments, on_delete=models.SET_NULL, blank=True, null=True)

    username = models.CharField(max_length=255, null=False, blank=True)
    logs = models.TextField(blank=True)

    class Meta:
        """
        Metadata for the Products model.
        """
        db_table = 'Products'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return f"Product (Product Location: {self.location}, Reel Number: {self.reel_number}, Status: {self.status})"


class Customer(models.Model):
    date = models.DateTimeField(default=timezone.now, blank=True)
    status = models.CharField(max_length=255, blank=True, default='Active')
    customer_name = models.CharField(max_length=255, null=False)
    address = models.TextField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    comments = models.TextField(blank=True)
    username = models.CharField(max_length=255, null=False, blank=True)
    logs = models.TextField(blank=True)

    class Meta:
        db_table = 'Customer'

    def __str__(self):
        return f"{self.customer_name} (ID: {self.status})"


class RawMaterial(models.Model):
    """
    Represents a raw material used in production.

    Attributes:
        supplier_name
        material_type (str): Type of the raw material (e.g., cotton, wool, plastic).
        material_name (str): Name of the specific raw material (e.g., Pima cotton, Merino wool).
        description (str, optional): Optional description of the raw material and its properties.
        status (str): Current status of the raw material (e.g., available, low stock, discontinued).
        comments (str, optional): Additional comments or notes about the raw material.
    """
    date = models.DateTimeField(default=timezone.now, blank=True)
    status = models.CharField(max_length=255, default='Active')
    supplier_name = models.CharField(max_length=255, null=True, blank=True)
    material_type = models.CharField(max_length=255)
    material_name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)
    comments = models.TextField(blank=True)
    username = models.CharField(max_length=255, null=False, blank=True)
    logs = models.TextField(blank=True)

    class Meta:
        db_table = 'RawMaterial'

    def __str__(self):
        """
        Returns a human-readable representation of the RawMaterial object.

        Format: "{material_name} (ID: {material_id})"
        """
        return f"{self.supplier_name} - {self.material_name} - {self.material_type} - {self.description} - {self.status}"


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

    date = models.DateTimeField(default=timezone.now, blank=True)
    status = models.CharField(max_length=225, choices=[('Paid', 'Paid'), ('Terms', 'Terms'), ('Cancelled', 'Cancelled')], blank=True, null=True)
    receive_date = models.DateTimeField(blank=True, null=True)
    payment_date = models.DateTimeField(blank=True, null=True)
    # supplier_id = models.ForeignKey('Supplier', on_delete=models.SET_NULL, blank=True, null=True)
    license_number = models.CharField(max_length=255, null=True)
    # material_id = models.ForeignKey('MaterialType', on_delete=models.SET_NULL, blank=True, null=True)

    material_type = models.CharField(max_length=255, blank=True, null=True)
    material_name = models.CharField(max_length=255, blank=True, null=True)
    supplier_name = models.CharField(max_length=255, blank=True, null=True)
    unit = models.CharField(max_length=255, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    quality = models.CharField(max_length=255, blank=True, null=True)
    penalty = models.CharField(max_length=255, blank=True, null=True)
    weight1 = models.IntegerField(null=True)
    weight2 = models.IntegerField(null=True)
    net_weight = models.IntegerField(null=True)
    price_per_kg = models.BigIntegerField(null=True)
    # VAT field needs further information on data type
    vat = models.IntegerField(null=True)
    total_price = models.BigIntegerField(null=True)
    extra_cost = models.BigIntegerField(null=True)
    invoice_status = models.CharField(max_length=255, choices=[('Received', 'Received'), ('NA', 'NA')], blank=True, null=True)
    payment_details = models.CharField(max_length=255, blank=True, null=True)
    invoice_number = models.CharField(max_length=255, blank=True, null=True)
    document_info = models.TextField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    cancellation_reason = models.TextField(blank=True, null=True)

    shipment_id = models.ForeignKey(Shipments, on_delete=models.SET_NULL, blank=True, null=True)
    username = models.CharField(max_length=255, null=False, blank=True)
    logs = models.TextField(blank=True)

    class Meta:
        db_table = "Purchases"
        verbose_name_plural = "Purchases"

    def __str__(self):
        """
        String representation of the Purchase instance.
        """
        return f"Purchase {self.id} on {self.date} - {self.username} - {self.receive_date}"


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

    date = models.DateTimeField(default=timezone.now, null=True)
    status = models.CharField(max_length=255, choices=[('Paid', 'Paid'), ('Terms', 'Terms'), ('Cancelled', 'Cancelled')], null=True)
    payment_date = models.DateTimeField(null=True)
    customer_name = models.CharField(max_length=255, null=False)
    license_number = models.CharField(max_length=255, null=True)
    list_of_reels = models.TextField(null=True)
    width = models.IntegerField(null=True, blank=True)
    weight1 = models.IntegerField(null=True)
    weight2 = models.IntegerField(null=True)
    net_weight = models.IntegerField(null=True)
    price_per_kg = models.BigIntegerField(null=True)
    vat = models.IntegerField(null=True)
    total_price = models.BigIntegerField(null=True)
    extra_cost = models.BigIntegerField(null=True)
    profile_name = models.CharField(max_length=255, null=True)
    invoice_status = models.CharField(max_length=255, choices=[('Sent', 'Sent'), ('NA', 'NA')], null=True)
    invoice_number = models.CharField(max_length=255, null=True)

    payment_details = models.CharField(max_length=255, null=True)
    document_info = models.TextField(null=True)
    comments = models.TextField(null=True)
    cancellation_reason = models.TextField(null=True)
    shipment = models.ForeignKey('Shipments', on_delete=models.CASCADE, null=True)

    username = models.CharField(max_length=255, null=False, blank=True)
    logs = models.TextField(blank=True)
    # Meta
    class Meta:
        db_table = 'Sales'
        verbose_name_plural = "Sales"

    def __str__(self):
        return f"Sale (ID: {self.id}, Date: {self.date}, Customer: {self.customer})"


class AnbarGeneric(models.Model):
    """
    Abstract base model for generic anbar items.
    This model provides common fields and behaviors for all anbar items.
    """

    # Status of the material
    STATUS_CHOICES = [
        ('In-stock', 'In-stock'),
        ('Sold', 'Sold'),
        ('Moved', 'Moved'),
        ('Used', 'Used'),
        ('Cancelled', 'Cancelled'),
    ]
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, null=True, blank=True)

    # Location of the material
    location = models.CharField(max_length=255, null=True, blank=True)

    date = models.DateTimeField(default=timezone.now, blank=True)
    # Date and time when the record was received
    receive_date = models.DateTimeField(null=True, blank=True)

    # Last date the material was updated
    last_date = models.DateTimeField(null=True, blank=True)

    # Reel number for the material
    reel_number = models.CharField(max_length=255, null=True, blank=True)

    # Foreign key to the Supplier model (assuming it exists)
    # supplier_id = models.ForeignKey('Supplier', on_delete=models.SET_NULL, null=True, blank=True)

    # Name of the supplier
    supplier_name = models.CharField(max_length=255, null=True, blank=True)

    # Type of material
    material_type = models.CharField(max_length=255, null=True, blank=True)

    # Name of the material
    material_name = models.CharField(max_length=255, null=True, blank=True)

    # Description of the material
    description = models.TextField(null=True, blank=True)

    # Width of the material
    width = models.IntegerField(null=True, blank=True)

    # GSM (Grams per Square Meter) of the material
    gsm = models.IntegerField(null=True, blank=True)

    # Length of the material
    length = models.IntegerField(null=True, blank=True)

    # Grade of the material
    grade = models.CharField(max_length=255, null=True, blank=True)

    # Breaks of the material
    breaks = models.IntegerField(null=True, blank=True)

    # Additional comments about the material
    comments = models.TextField(null=True, blank=True)
    shipment_id = models.ForeignKey(Shipments, on_delete=models.SET_NULL, blank=True, null=True)
    # QR code associated with the material
    qr_code = models.TextField(null=True, blank=True)
    unit = models.CharField(max_length=255, null=True, blank=True)
    # Profile name for the material
    profile_name = models.CharField(max_length=255, null=True, blank=True)

    username = models.CharField(max_length=255, null=False, blank=True)
    logs = models.TextField(blank=True)

    # Meta
    class Meta:
        abstract = True # Make this model abstract so it's not created in the DB


class Anbar_Sangin(AnbarGeneric):
    """
    Model representing an anbar item in Sangin.
    Inherits from AnbarGeneric to reuse common fields and behaviors.
    """
    class Meta(AnbarGeneric.Meta):
        verbose_name_plural = "Anbar Sangin"
        db_table = 'Anbar_Sangin'

    def __str__(self):
        return f"{self.receive_date} - {self.reel_number}  - {self.width} - {self.supplier_name} - {self.material_type} - {self.material_name}- {self.unit} - {self.description} - {self.status} - {self.location}"


class Anbar_Salon_Tolid(AnbarGeneric):
    """
    Model representing an anbar item in Salon Tolid.
    Inherits from AnbarGeneric to reuse common fields and behaviors.
    """
    class Meta(AnbarGeneric.Meta):
        verbose_name_plural = "Anbar Salon Tolid"
        db_table = 'Anbar_Salon_Tolid'

    def __str__(self):
        return f"{self.receive_date} - {self.reel_number}  - {self.width} - {self.supplier_name} - {self.material_type} - {self.material_name}- {self.unit} - {self.description} - {self.status} - {self.location}"


class Anbar_Parvandeh(AnbarGeneric):
    """
    Model representing an anbar item in Parvandeh.
    Inherits from AnbarGeneric to reuse common fields and behaviors.
    """
    class Meta(AnbarGeneric.Meta):
        verbose_name_plural = "Anbar Parvandeh"
        db_table = 'Anbar_Parvandeh'

    def __str__(self):
        return f"{self.receive_date} - {self.reel_number}  - {self.width} - {self.supplier_name} - {self.material_type} - {self.material_name}- {self.unit} - {self.description} - {self.status} - {self.location}"


class Anbar_Koochak(AnbarGeneric):
    """
    Model representing an anbar item in Koochak.
    Inherits from AnbarGeneric to reuse common fields and behaviors.
    """
    class Meta(AnbarGeneric.Meta):
        verbose_name_plural = "Anbar Koochak"
        db_table = 'Anbar_Koochak'

    def __str__(self):
        return f"{self.receive_date} - {self.reel_number}  - {self.width} - {self.supplier_name} - {self.material_type} - {self.material_name}- {self.unit} - {self.description} - {self.status} - {self.location}"


class Anbar_Khamir_Ghadim(AnbarGeneric):
    """
    Model representing an anbar item in Khamir Ghadim.
    Inherits from AnbarGeneric to reuse common fields and behaviors.
    """
    class Meta(AnbarGeneric.Meta):
        verbose_name_plural = "Anbar Khamir Ghadim"
        db_table = 'Anbar_Khamir_Ghadim'

    def __str__(self):
        return f"{self.receive_date} - {self.reel_number}  - {self.width} - {self.supplier_name} - {self.material_type} - {self.material_name}- {self.unit} - {self.description} - {self.status} - {self.location}"


class Anbar_Khamir_Kordan(AnbarGeneric):
    """
    Model representing an anbar item in Khamir Kordan.
    Inherits from AnbarGeneric to reuse common fields and behaviors.
    """
    class Meta(AnbarGeneric.Meta):
        verbose_name_plural = "Anbar Khamir Kordan"
        db_table = 'Anbar_Khamir_Kordan'

    def __str__(self):
        return f"{self.receive_date} - {self.reel_number}  - {self.width} - {self.supplier_name} - {self.material_type} - {self.material_name}- {self.unit} - {self.description} - {self.status} - {self.location}"


class Anbar_Muhvateh_Kardan(AnbarGeneric):
    """
    Model representing an anbar item in Muhvateh Kardan.
    Inherits from AnbarGeneric to reuse common fields and behaviors.
    """
    class Meta(AnbarGeneric.Meta):
        verbose_name_plural = "Anbar Muhvateh Kardan"
        db_table = 'Anbar_Muhvateh_Kardan'

    def __str__(self):
        return f"{self.receive_date} - {self.reel_number}  - {self.width} - {self.supplier_name} - {self.material_type} - {self.material_name}- {self.unit} - {self.description} - {self.status} - {self.location}"


class Anbar_Akhal(AnbarGeneric):
    """
    Model representing an anbar item in Akhal.
    Inherits from AnbarGeneric to reuse common fields and behaviors.
    """
    class Meta(AnbarGeneric.Meta):
        verbose_name_plural = "Anbar Akhal"
        db_table = 'Anbar_Akhal'

    def __str__(self):
        return f"{self.receive_date} - {self.reel_number}  - {self.width} - {self.supplier_name} - {self.material_type} - {self.material_name}- {self.unit} - {self.description} - {self.status} - {self.location}"


class Consumption(models.Model):
    """
    Represents a consumption record in the system.
    Each record includes details about the material consumed,
    such as the supplier, material type, and quantity.
    """
    date = models.DateTimeField(default=timezone.now, blank=True)
    # Status of the consumption
    status = models.CharField(max_length=50, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)

    # Date and time when the consumption was recorded
    receive_date = models.DateTimeField(null=True, blank=True)

    # Foreign key to the Supplier model (assuming it exists)
    # supplier_id = models.ForeignKey('Supplier', on_delete=models.SET_NULL, null=True, blank=True)
    shipment_id = models.ForeignKey(Shipments, on_delete=models.SET_NULL, blank=True, null=True)

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

    # Grade of matterials
    grade = models.CharField(max_length=255, null=True, blank=True)

    # Additional comments about the consumption
    comments = models.TextField(null=True, blank=True)
    cancelling_reason = models.TextField(null=True, blank=True)

    username = models.CharField(max_length=255, null=False, blank=True)
    logs = models.TextField(blank=True)

    # Meta
    class Meta:
        db_table = 'Consumption'

    def __str__(self):
        """
        String representation of the Consumption instance.
        """
        return f'{self.receive_date} - {self.supplier_name} - {self.material_type} - {self.material_name} - {self.unit} - {self.reel_number} - {self.profile_name} - {self.cancelling_reason} - {self.status} - {self.location}'


class ConsumptionProfile(models.Model):
    status = models.CharField(max_length=255, blank=True, default="Active")
    date = models.DateTimeField(default=timezone.now, blank=True)
    receive_date = models.DateTimeField(blank=True, null=True)
    profile_name = models.CharField(max_length=255, null=True, blank=True)
    supplier_name = models.CharField(max_length=255)
    material_type = models.CharField(max_length=255)
    material_name = models.CharField(max_length=255)
    unit = models.CharField(max_length=100)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)

    username = models.CharField(max_length=255, null=False, blank=True)
    logs = models.TextField(blank=True)
    # Meta
    class Meta:
        db_table = 'ConsumptionProfile'

    def __str__(self):
        return f"{self.material_name} ({self.quantity} {self.unit})"


class MaterialType(models.Model):
    """
    MaterialType model represents different types of materials supplied by suppliers.

    Fields:
    - id: Auto-incrementing primary key.
    - supplier_name: Name of the supplier. Can be null or blank.
    - material_type: Type of material. Required field.
    - username: Username associated with the material type. Can be null or blank.
    """
    status = models.CharField(max_length=50, null=True, blank=True, default='Active')
    date = models.DateTimeField(default=timezone.now, blank=True)
    supplier_name = models.CharField(max_length=255, null=True, blank=True)
    # Ensure material_type is always provided to avoid empty entries
    material_type = models.CharField(max_length=255)
    username = models.CharField(max_length=255, null=False, blank=True)
    logs = models.TextField(blank=True)

    # Meta
    class Meta:
        db_table = 'MaterialType'

    def __str__(self):
        """
        Returns a string representation of the MaterialType object, including the supplier name, material type, and username.
        This method is used to display a human-readable representation of the object.
        """
        return f"{self.supplier_name} - {self.material_type} - {self.status}"


class Unit(models.Model):
    """
    Represents a unit of measurement for quantities.

    Attributes:
        id (int): Auto-incrementing primary key for the unit.
        supplier_name (str, null=True, blank=True): Name of the supplier associated with the unit.
        material_type (str): Type of material the unit is associated with.
        unit_name (str): Name of the unit, unique across all units.
        count (float, optional): Value representing the unit's capacity in kilograms (e.g., 25 for a 25kg bag).
        username (str, blank=True): Username of the user who created the unit, if applicable.
        date (datetime): Date and time the unit was created, defaults to the current time.
        logs (str, blank=True): Text field for storing logs or additional information about the unit.
    """
    status = models.CharField(max_length=255, blank=True, default='Active')
    date = models.DateTimeField(default=timezone.now, blank=True)
    supplier_name = models.CharField(max_length=255, null=True, blank=True)
    material_type = models.CharField(max_length=255)
    unit_name = models.CharField(max_length=255, null=True, blank=True)
    count = models.FloatField(blank=True, null=True)
    username = models.CharField(max_length=255, null=False, blank=True)

    logs = models.TextField(blank=True)

    # Meta
    class Meta:
        db_table = 'Unit'

    def __str__(self):
        """
        Returns a string representation of the Unit object, including the Unit name, count, and username.
        This method is used to display a human-readable representation of the object.
        """
        return f"{self.supplier_name} - {self.material_type} - {self.unit_name} - {self.count} - {self.status}"


class Alert(models.Model):
    """
    Model representing an alert event within the system.

    Attributes:
        - message: TextField that stores the alert message.
        - date: DateTimeField that records the time of alert creation.
        - status: CharField that indicates the current processing status of the alert.
                  It uses predefined choices and defaults to 'Pending'.

    The status field can have the following values:
        - 'Pending': The alert has been created but not yet addressed.
        - 'Resolved': The alert has been addressed and is considered resolved.
    """
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Resolved', 'Resolved'),
    ]
    date = models.DateTimeField(default=timezone.now, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending', null=True, blank=True)
    message = models.TextField()

    def __str__(self):
        """
        Return a string representation of the Alert, which includes
        the creation timestamp and a snippet of the message.
        """
        # Format the created_at datetime for a cleaner string representation
        formatted_time = self.date.strftime('%Y-%m-%d %H:%M')
        # Return a formatted string with the timestamp and the first 30 characters of the message
        return f"[{formatted_time}] Alert: {self.message[:30]}..."

    class Meta:
        db_table = 'Alert'
