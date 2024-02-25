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



def new_material_type(request):
    existing_types = MaterialType.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        if MaterialType.objects.filter(name=name).exists():
            # Material type already exists
            error_message = 'Material type already exists'
            return render(request, 'add_material_error.html', {'error': error_message})
        else:
            # Optionally capture username for reference
            # username = request.user.username  # If using User model
            new_type = MaterialType.objects.create(
                name=name
                # username_created=username  # Uncomment if capturing username
            )
            return redirect('add_material_success', material_type_id=new_type.id)
    else:
        return render(request, 'new_material_form.html', {'existing_types': existing_types})


def add_material_success(request, material_type_id):
    material_type = MaterialType.objects.get(pk=material_type_id)
    return render(request, 'add_material_success.html', {'material_type': material_type})



def new_unit(request):
    existing_units = Unit.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        count_kg = request.POST.get('count_kg', None)  # Handle optional field
        if Unit.objects.filter(name=name).exists():
            # Unit already exists
            error_message = 'Unit already exists'
            return render(request, 'add_unit_error.html', {'error': error_message})
        else:
            # Optionally capture username for reference
            username = request.user.username  # If using User model
            new_unit = Unit.objects.create(
                name=name,
                count_kg=count_kg,
                username_created=username
            )
            return redirect('add_unit_success', unit_id=new_unit.id)
    else:
        return render(request, 'new_unit_form.html', {'existing_units': existing_units})



def add_unit_success(request, unit_id):
    unit = Unit.objects.get(pk=unit_id)
    return render(request, 'add_unit_success.html', {'unit': unit})



def new_raw_material(request):
    """
    View for adding a new raw material.

    Retrieves existing suppliers and material types, validates form data,
    and creates a new RawMaterial object if valid.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse:
            - Rendered new_material_form.html on GET.
            - Redirect to add_material_success on successful POST.
            - Rendered add_material_error.html with error message on failed POST.
    """

    suppliers = Supplier.objects.all()
    material_types = MaterialType.objects.all()
    if request.method == 'POST':
        supplier_id = request.POST['supplier']
        material_type_id = request.POST['material_type']
        name = request.POST['name']
        comments = request.POST.get('comments', "")  # Handle optional field

        # Check for existing material with same name and supplier
        if RawMaterial.objects.filter(supplier_id=supplier_id, material_type_id=material_type_id, name=name).exists():
            error_message = 'Material already exists'
            return render(request, 'add_material_error.html', {'error': error_message})

        # Optionally capture username for reference
        username = request.user.username  # If using User model

        # Create new RawMaterial object
        new_material = RawMaterial.objects.create(
            supplier_id=supplier_id,
            material_type_id=material_type_id,
            name=name,
            comments=comments,
            username_created=username
        )

        return redirect('add_material_success', material_id=new_material.id)
    else:
        return render(request, 'new_material_form.html', {'suppliers': suppliers, 'material_types': material_types})


def add_material_success(request, material_id):
    """
    View for displaying success message after adding a new raw material.

    Args:
        request: The HTTP request object.
        material_id: ID of the newly created RawMaterial object.

    Returns:
        HttpResponse: Rendered add_material_success.html with material details.
    """

    material = RawMaterial.objects.get(pk=material_id)
    return render(request, 'add_material_success.html', {'material': material})


def add_truck(request):
    """
    Handles POST requests to add a new truck.

    Returns:
        JsonResponse:
            - success (str): Success message upon successful creation.
            - error (str): Error message if validation fails or truck already exists.
        HttpResponse:
            - Renders the "add_truck.html" template if GET request.
    """

    if request.method == 'POST':
        license_number = request.POST.get('license_number')
        driver_name = request.POST.get('driver_name')
        phone = request.POST.get('phone')
        status = request.POST.get('status')
        location = request.POST.get('location')
        comments = request.POST.get('comments')

        # Validate input
        if not license_number:
            return JsonResponse({'error': 'License number is required.'}, status=400)

        # Check for existing truck
        existing_truck = Truck.objects.filter(license_number=license_number).first()
        if existing_truck:
            return JsonResponse({'error': 'Truck with this license number already exists.'}, status=400)

        # Create new truck
        new_truck = Truck(
            license_number=license_number,
            driver_name=driver_name,
            phone=phone,
            status=status if status in ['Free', 'Busy'] else 'Free',
            location=location,
            comments=comments,
        )
        new_truck.save()

        # Return success response
        return JsonResponse({
            'success': 'Truck added successfully.',
            'license_number': new_truck.license_number,
        }, status=201)

    else:
        return render(request, 'add_truck.html')

