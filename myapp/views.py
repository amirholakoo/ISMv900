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
        driver_doc = request.POST.get('driver_doc')
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
            driver_doc=driver_doc,
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


def add_anbar(request):
    """
    Handles POST requests to add a new Anbar.

    Returns:
        JsonResponse:
            - success (str): Success message upon successful creation.
            - error (str): Error message if validation fails or Anbar already exists.
        HttpResponse:
            - Renders the "add_anbar.html" template if GET request.
    """

    if request.method == 'POST':
        location_name = request.POST.get('location_name')

        # Validate input
        if not location_name:
            return JsonResponse({'error': 'Location name is required.'}, status=400)

        # Check for existing Anbar
        existing_anbar = Anbar.objects.filter(location_name=location_name).first()
        if existing_anbar:
            return JsonResponse({'error': 'Anbar with this location name already exists.'}, status=400)

        # Create new Anbar
        new_anbar = Anbar(
            location_name=location_name,
            comments=f"Automatically Created",
        )
        new_anbar.save()

        # Return success response
        return JsonResponse({
            'success': 'Anbar added successfully.',
            'location_name': new_anbar.location_name,
        }, status=201)

    else:
        return render(request, 'add_anbar.html')


def add_reel(request):
    """
    Handles requests to add a new reel.

    Returns:
        HttpResponse:
            - Renders the "add_reel.html" template if GET request.
        JsonResponse:
            - Success message and reel data upon successful creation.
            - Error message and error details upon validation failure or issue.
    """

    if request.method == 'GET':
        # Get last reel number and consumption profile data
        last_reel_number = Product.objects.order_by('reel_number').last().reel_number if Product.objects.exists() else None
        consumption_profiles = Consumption.objects.all()

        context = {
            'last_reel_number': last_reel_number,
            'consumption_profiles': consumption_profiles,
        }
        return render(request, 'add_reel.html', context)

    elif request.method == 'POST':
        # Validate user input
        reel_number = request.POST.get('reel_number').strip()
        width = float(request.POST.get('width')) if request.POST.get('width') else None
        gsm = float(request.POST.get('gsm')) if request.POST.get('gsm') else None
        length = float(request.POST.get('length')) if request.POST.get('length') else None
        breaks = int(request.POST.get('breaks')) if request.POST.get('breaks') else None
        grade = request.POST.get('grade').strip() if request.POST.get('grade') else None
        consumption_profile_id = int(request.POST.get('consumption_profile'))

        errors = {}
        if not reel_number:
            errors['reel_number'] = 'Reel number is required.'
        elif Product.objects.filter(reel_number=reel_number).exists():
            errors['reel_number'] = 'Reel number already exists.'
        if not width:
            errors['width'] = 'Width is required.'
        if not gsm:
            errors['gsm'] = 'GSM is required.'
        if not length:
            errors['length'] = 'Length is required.'
        if not breaks:
            errors['breaks'] = 'Number of breaks is required.'
        if not grade:
            errors['grade'] = 'Grade is required.'
        if not Consumption.objects.filter(pk=consumption_profile_id).exists():
            errors['consumption_profile'] = 'Invalid consumption profile.'

        if errors:
            return JsonResponse({'error': errors})

        # Create new product (reel) and consumption objects
        product = Product.objects.create(
            reel_number=reel_number,
            width=width,
            gsm=gsm,
            length=length,
            breaks=breaks,
            grade=grade,
            location=Anbar.objects.get(pk=1),  # Assuming Anbar_Salon_Tolid has ID 1
            status='In-stock',
        )
        consumption = Consumption.objects.create(
            consumption_profile=Consumption.objects.get(pk=consumption_profile_id),
            material_type=product.reel_number,  # Using reel number as material type
            material_name='New Material',  # Default material name
            quantity=1,  # Assuming quantity is 1 for new reels
            status='Completed',
        )

        # Update Anbar_XXX (details needed based on the PDF diagram)
        # ...

        # Return success response
        return JsonResponse({
            'success': 'Reel added successfully!',
            'reel_number': reel_number,
            # Add other relevant reel data to the response as needed
        })

    else:
        return JsonResponse({'error': 'Invalid request method.'})



from django.utils import timezone

def create_shipment(request):
    """
    Creates a new shipment based on user input.

    Handles both POST and GET requests:
        - POST: Processes form data and creates a shipment, returning JSON response.
        - GET: Renders the initial form with available trucks, suppliers, etc.

    Validates required fields and performs appropriate actions based on shipment type.
    """

    if request.method == 'POST':
        # Extract data from request.POST
        license_number = request.POST.get('license_number')
        supplier_id = request.POST.get('supplier')
        material_type_id = request.POST.get('material_type')
        material_id = request.POST.get('material')
        customer_id = request.POST.get('customer')
        shipment_type = request.POST.get('shipment_type')

        # Check required fields
        errors = []
        if not license_number:
            errors.append('License number is required.')
        if shipment_type == 'Incoming' and not (supplier_id and material_type_id and material_id):
            errors.append('Supplier, material type, and material are required for incoming shipments.')
        if shipment_type == 'Outgoing' and not customer_id:
            errors.append('Customer is required for outgoing shipments.')

        if errors:
            return JsonResponse({'status': 'error', 'errors': errors})

        # Process data and create shipment
        truck = Truck.objects.filter(license_number=license_number, status='Free').first()
        if not truck:
            return JsonResponse({'status': 'error', 'message': 'No free truck with that license number.'})

        shipment = Shipment()
        shipment.entry_time = timezone.now()
        shipment.license_number = license_number
        shipment.shipment_type = shipment_type

        # Handle incoming/outgoing shipment logic
        if shipment_type == 'Incoming':
            shipment.supplier = Supplier.objects.get(pk=supplier_id)
            shipment.material_type = MaterialType.objects.get(pk=material_type_id)
            shipment.material = MaterialType.objects.get(pk=material_id)
            # Update material quantity if applicable
            # ...

        elif shipment_type == 'Outgoing':
            shipment.customer = Customer.objects.get(pk=customer_id)
            # Update customer inventory if applicable
            # ...

        shipment.save()

        truck.status = 'Busy'
        truck.location = 'Entrance'
        truck.save()

        return JsonResponse({'status': 'success', 'message': 'Shipment created successfully!'})

    # Render initial form or handle GET requests
    trucks = Truck.objects.filter(status='Free')
    suppliers = Supplier.objects.filter(status='Active')
    material_types = MaterialType.objects.filter(status='Active')
    customers = Customer.objects.filter(status='Active')
    return render(request, 'create_shipment.html', {'trucks': trucks, 'suppliers': suppliers, 'material_types': material_types, 'customers': customers})
