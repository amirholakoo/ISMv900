from django.shortcuts import render, redirect
from .models import *
from django.http import  JsonResponse
from datetime import datetime
# Create your views here.

def add_customer_view(request):
    if request.method == 'POST':
        # Load existing customer names from DB
        existing_names = [customer.customer_name for customer in Customer.objects.all().values_list('customer_name')]

        # Validate and process form data
        customer_name = request.POST.get('customer_name')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        comments = request.POST.get('comments')

        # Check for duplicate name
        if customer_name in existing_names:
            error_message = "Customer already exists with name '{}'. Please add full name and try again.".format(customer_name)
            return render(request, 'add_customer.html', {'error_message': error_message})

        # Create new customer object
        new_customer = Customer(
            customer_name=customer_name,
            address=address,
            phone=phone,
            status="Active",
            comments=f"Username Created NOW (CVS)"
        )
        new_customer.save()

        # Success message
        success_message = f"Customer '{customer_name}' has been added successfully."
        return render(request, 'add_customer.html', {'success_message': success_message})

    else:
        # Display empty form
        return render(request, 'add_customer.html')


def add_supplier_view(request):
    if request.method == 'POST':
        # Load existing supplier names from DB
        existing_names = [supplier.supplier_name for supplier in Supplier.objects.all().values_list('supplier_name')]

        # Validate and process form data
        supplier_name = request.POST.get('supplier_name')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        comments = request.POST.get('comments')

        # Check for duplicate name
        if supplier_name in existing_names:
            error_message = "Supplier already exists with name '{}'. Please add full name and try again.".format(supplier_name)
            return render(request, 'add_supplier.html', {'error_message': error_message})

        # Create new supplier object
        new_supplier = Supplier(
            supplier_name=supplier_name,
            address=address,
            phone=phone,
            status="Active",
            comments=f"Username Created NOW (CVS)"
        )
        new_supplier.save()

        # Success message
        success_message = f"Supplier '{supplier_name}' has been added successfully."
        return render(request, 'add_supplier.html', {'success_message': success_message})

    else:
        # Display empty form
        return render(request, 'add_supplier.html')


def add_material_type(request):
    if request.method == 'POST':
        material_type = request.POST.get('material_type')

        # Check if material type already exists
        existing_type = RawMaterial.objects.filter(material_type=material_type).first()
        if existing_type:
            return JsonResponse({'error': 'Material type already exists.'}, status=400)

        # Create new material type
        new_material = RawMaterial(
            material_type=material_type,
            comments=f"Username Created NOW (CVS)",
            status="Active",
        )
        new_material.save()

        return JsonResponse({'success': 'Material type added successfully.'}, status=201)
    else:
        return render(request, 'add_material_type.html')
