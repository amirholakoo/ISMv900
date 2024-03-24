# Pseudocode for Django views/functions
import json
from django.http import JsonResponse
from django.apps import apps
from django.db.models import Count, Sum, Q
from django.core.serializers import serialize


from .models import Shipments
from .models import Sales
from .models import Purchases
from .models import RawMaterial, AnbarGeneric
from .models import Consumption
from .models import Products, Anbar_Sangin, Anbar_Salon_Tolid, Anbar_Parvandeh, Anbar_Koochak, Anbar_Khamir_Ghadim, Anbar_Khamir_Kordan, Anbar_Muhvateh_Kardan, Anbar_Akhal


LOW_STOCK_THRESHOLD = 10  # Define a low stock threshold


def fetch_ongoing_shipments(request):
    """
    Fetches ongoing shipments from the database.

    An ongoing shipment is defined as a shipment whose status is either 'Registered',
    'LoadingUnloading', or 'LoadedUnloaded'.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        JsonResponse: A JSON response containing a list of ongoing shipments.
    """
    # Define the statuses that indicate an ongoing shipment
    ongoing_statuses = ['Registered', 'LoadingUnloading', 'LoadedUnloaded']
    
    # Query the Shipments table for ongoing shipments
    ongoing_shipments = Shipments.objects.filter(status__in=ongoing_statuses).values(
        'id', 'shipment_type', 'status', 'location', 'license_number', 
        'receive_date', 'entry_time', 'customer_name', 'supplier_name', 
        'material_type', 'material_name', 'weight1', 'weight2', 'net_weight', 
        'list_of_reels', 'profile_name', 'sales_id', 'price_per_kg', 
        'total_price', 'extra_cost', 'vat', 'invoice_status', 'payment_status', 
        'exit_time', 'document_info', 'comments', 'cancellation_reason', 'username'
    )

    # Serialize the queryset to JSON format
    shipments_data = json.loads(serialize('json', ongoing_shipments))

    # Return the JsonResponse
    return JsonResponse({"status": "success", "shipments": shipments_data})

def fetch_sales_report(request):
    """
    Fetches sales data and aggregates it by customer and date.

    Returns:
        JsonResponse: A JSON response containing aggregated sales data.
    """
    # Aggregate sales data
    sales_data = Sales.objects.values('customer__customer_name', 'date').annotate(
        total_sales=Sum('total_price'),
        total_weight=Sum('net_weight'),
        total_units=Sum('quantity')
    ).order_by('date', 'customer__customer_name')

    # Prepare the data for JSON response
    formatted_sales_data = []
    for item in sales_data:
        formatted_sales_data.append({
            'customer': item['customer__customer_name'],
            'date': item['date'].strftime("%Y-%m-%d"),
            'total_sales': item['total_sales'],
            'total_weight': item['total_weight'],
            'total_units': item['total_units'],
        })

    return JsonResponse({'status': 'success', 'data': formatted_sales_data})

def fetch_purchase_report(request):
    """
    Fetches purchase order records from the Purchases model.

    Returns:
        JsonResponse: A JSON response containing a list of purchase order records.
    """
    # Query the Purchases table to get all purchase records
    purchase_orders = Purchases.objects.all().values(
        'id', 'date', 'receive_date', 'supplier_name', 'material_type',
        'material_name', 'unit', 'quantity', 'price_per_kg', 'total_price',
        'vat', 'status', 'payment_details', 'invoice_number', 'comments'
    )

    # Convert the query result to a list of dictionaries
    purchase_data = list(purchase_orders)

    # Return the JsonResponse
    return JsonResponse({"status": "success", "purchase_data": purchase_data})

def fetch_inventory_report(request):
    """
    Fetches inventory report from the database, aggregating data across various Anbars and Products.

    Returns:
        JsonResponse: A JSON response containing the aggregated inventory data.
    """

    # Fetch in-stock products
    product_data = Products.objects.filter(status='In-stock').values('reel_number', 'width', 'gsm', 'length', 'grade', 'location', 'quantity').annotate(total=Sum('quantity'))

    # Initialize a dictionary to hold the aggregated data
    inventory_data = {
        'products': list(product_data),
        'anbars': []
    }

    # List of Anbar models
    anbar_models = [Anbar_Sangin, Anbar_Salon_Tolid, Anbar_Parvandeh, Anbar_Koochak, Anbar_Khamir_Ghadim, Anbar_Khamir_Kordan, Anbar_Muhvateh_Kardan, Anbar_Akhal]

    # Aggregate data for each Anbar
    for anbar_model in anbar_models:
        anbar_name = anbar_model._meta.verbose_name_plural
        anbar_data = anbar_model.objects.filter(status='In-stock').values('material_name', 'material_type', 'quantity', 'location').annotate(total=Sum('quantity'))
        inventory_data['anbars'].append({
            'name': anbar_name,
            'data': list(anbar_data)
        })

    return JsonResponse({'status': 'success', 'inventory_data': inventory_data})

def fetch_raw_material_report(request):
    """
    Fetches a report on raw materials from the database.

    This function aggregates data from the RawMaterial model and related Anbar models
    to provide a comprehensive report on the available raw materials, their quantities,
    and statuses in different Anbars.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        JsonResponse: A JSON response containing the raw materials report.
    """
    # Aggregate raw material data
    raw_materials = RawMaterial.objects.values(
        'material_type', 'material_name', 'supplier_name'
    ).annotate(
        total_count=Count('material_name'),
        active_count=Count('status', filter=Q(status='Active'))
    ).order_by('material_type', 'material_name')

    # Aggregate data from different Anbar models
    anbar_totals = []
    anbar_models = [Anbar_Sangin, Anbar_Salon_Tolid, Anbar_Parvandeh, Anbar_Koochak, Anbar_Khamir_Ghadim, Anbar_Khamir_Kordan, Anbar_Muhvateh_Kardan, Anbar_Akhal]

    for anbar_model in anbar_models:
        anbar_data = anbar_model.objects.values(
            'material_name', 'location'
        ).annotate(
            total=Sum('quantity')
        ).order_by('material_name')
        anbar_totals.append({
            "anbar": anbar_model._meta.verbose_name,
            "data": anbar_data
        })

    return JsonResponse({
        'status': 'success',
        'raw_materials': list(raw_materials),
        'anbar_totals': anbar_totals
    })

def fetch_anbar_stock_report(request):
    """
    Fetches a stock report for each Anbar.

    This function aggregates data from various Anbar models to provide a report on the stock
    available in each Anbar, categorized by material name and type.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        JsonResponse: A JSON response containing the stock report for each Anbar.
    """
    # List of all Anbar models
    anbar_models = [
        Anbar_Sangin, Anbar_Salon_Tolid, Anbar_Parvandeh, 
        Anbar_Koochak, Anbar_Khamir_Ghadim, Anbar_Khamir_Kordan, 
        Anbar_Muhvateh_Kardan, Anbar_Akhal
    ]

    # Initialize a dictionary to hold the aggregated data
    anbar_reports = []

    # Iterate over each Anbar model to aggregate the stock data
    for anbar_model in anbar_models:
        anbar_name = anbar_model._meta.verbose_name_plural
        stock_data = anbar_model.objects.values(
            'material_name', 'material_type'
        ).annotate(
            total_quantity=Sum('quantity')
        ).order_by('material_name')

        # Add the aggregated data to the reports list
        anbar_reports.append({
            'anbar_name': anbar_name,
            'stock_data': list(stock_data)
        })

    return JsonResponse({
        'status': 'success',
        'anbar_reports': anbar_reports
    })

def fetch_consumption_report(request):
    """
    Fetches a report on the consumption of materials.

    This function aggregates data from the Consumption model to provide a detailed report
    on the consumed materials, including their types, quantities, and other relevant details.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        JsonResponse: A JSON response containing the consumption report.
    """
    # Aggregate consumption data
    consumption_data = Consumption.objects.values(
        'material_name', 'material_type', 'supplier_name', 'profile_name'
    ).annotate(
        total_quantity=Sum('quantity'),
        total_consumptions=Count('id')
    ).order_by('material_type', 'material_name')

    return JsonResponse({
        'status': 'success',
        'consumption_data': list(consumption_data)
    })

def check_low_stock_alert(request):
    """
    Checks the inventory levels in Products and Anbar models and generates alerts for low stock items.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        JsonResponse: A JSON response containing the low stock alerts for each product and Anbar item.
    """
    alerts = []

    # Check low stock in Products
    low_stock_products = Products.objects.filter(
        Q(status='In-stock') & Q(quantity__lt=LOW_STOCK_THRESHOLD)
    ).values('reel_number', 'quantity', 'material_name')

    for product in low_stock_products:
        alerts.append(f"Product {product['reel_number']} ({product['material_name']}) is low on stock with only {product['quantity']} items remaining.")

    # Check low stock in each Anbar model
    anbar_models = [Anbar_Sangin, Anbar_Salon_Tolid, Anbar_Parvandeh, Anbar_Koochak, Anbar_Khamir_Ghadim, Anbar_Khamir_Kordan, Anbar_Muhvateh_Kardan, Anbar_Akhal]

    for anbar_model in anbar_models:
        low_stock_anbar_items = anbar_model.objects.filter(
            Q(status='In-stock') & Q(quantity__lt=LOW_STOCK_THRESHOLD)
        ).values('reel_number', 'quantity', 'material_name')

        for item in low_stock_anbar_items:
            alerts.append(f"{anbar_model._meta.verbose_name} item {item['reel_number']} ({item['material_name']}) is low on stock with only {item['quantity']} items remaining.")

    return JsonResponse({
        'status': 'success',
        'alerts': alerts
    })


# Example usage in a Django view
def report_page_view(request):
    context = {
        'ongoing_shipments': fetch_ongoing_shipments(),
        'sales_report': fetch_sales_report(),
        'purchase_report': fetch_purchase_report(),
        'inventory_report': fetch_inventory_report(),
        'raw_material_report': fetch_raw_material_report(),
        # Add Anbar stock reports for each Anbar
        'consumption_report': fetch_consumption_report(),
    }
    return render(request, 'report_page.html', context)
