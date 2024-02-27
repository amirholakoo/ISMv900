from django.shortcuts import render, redirect
from .models import *
from django.http import  JsonResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
# Create your views here.

# Incoming process:
# Add Truck
# Add Shipment
# Weight 1
# Unloading by forklift
# Weight 2
# Create Purchase Order

# Operation API:


@csrf_exempt
def check_license_number(request):
    """
    Handles POST requests to check if a given license number exists in the Truck model.

    This view function is designed to be used with a POST request containing a 'license_number'
    in the request body. It checks the Truck model for the existence of a truck with the
    provided license number. If the truck exists, it returns a JSON response indicating
    that the license number exists. If the truck does not exist, it returns a JSON response
    indicating that the license number does not exist. If the request method is not POST or
    if the 'license_number' is not provided, it returns an error response.

    Parameters:
    - request (HttpRequest): The incoming HTTP request.

    Returns:
    - JsonResponse: A JSON response indicating the status of the license number check.
    """
    # Check if the request method is POST
    if request.method == 'POST':
        # Extract the license number from the request data
        license_number = request.GET.get('license_number')
        # Check if a license number was provided
        if license_number:
            try:
                # Attempt to retrieve a Truck object with the provided license number
                truck = Truck.objects.get(license_number=license_number)
                # If the truck exists, return a success response
                return JsonResponse({'status': 'exists', 'message': 'License number exists.'})
            except Truck.DoesNotExist:
                # If the truck does not exist, return an error response
                return JsonResponse({'status': 'not_exists', 'message': 'License number does not exist.'})
        else:
            # If no license number was provided, return an error response
            return JsonResponse({'status': 'error', 'message': 'License number not provided.'})
    else:
        # If the request method is not POST, return an error response
        return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})


@csrf_exempt
def add_truck(request):
    """
    Handles POST requests to add a new Truck to the database.

    This view function is designed to be used with a POST request containing the necessary
    data for creating a new Truck object. It creates a new Truck object with the provided
    data and saves it to the database.

    Parameters:
    - request (HttpRequest): The incoming HTTP request.

    Returns:
    - JsonResponse: A JSON response indicating the success or failure of the operation.
    """

    if request.method == 'POST':
        license_number = request.GET.get('license_number')
        driver_name = request.GET.get('driver_name')
        driver_doc = request.GET.get('driver_doc')
        phone = request.GET.get('phone')

        # Create new truck
        new_truck = Truck(
            license_number=license_number,
            driver_name=driver_name,
            driver_doc=driver_doc,
            phone=phone,
        )
        new_truck.save()

        # Return success response
        return JsonResponse({
            'success': 'Truck added successfully.',
            'license_number': new_truck.license_number,
        }, status=201)


@csrf_exempt
def add_supplier(request):
    """
    Handles POST requests to add a new Supplier to the database.

    This view function is designed to be used with a POST request containing the necessary
    data for creating a new Supplier object. It creates a new Supplier object with the provided
    data and saves it to the database.

    Parameters:
    - request (HttpRequest): The incoming HTTP request.

    Returns:
    - JsonResponse: A JSON response indicating the success or failure of the operation.
    """
    if request.method == 'POST':
        # Extract data from the request
        supplier_name = request.GET.get('supplier_name')
        address = request.GET.get('address')
        phone = request.GET.get('phone')
        comments = request.GET.get('comments')

        # Initialize an empty list to collect error messages
        errors = []

        # Check if all required fields are provided
        if not supplier_name:
            errors.append({'status': 'error', 'message': 'Supplier name is required.'})
        if not address:
            errors.append({'status': 'error', 'message': 'Address is required.'})
        if not phone:
            errors.append({'status': 'error', 'message': 'Phone is required.'})
        if not comments:
            errors.append({'status': 'error', 'message': 'Comments are required.'})
        # Load existing supplier names from DB
        existing_names = [supplier.supplier_name for supplier in Supplier.objects.all().values_list('supplier_name')]
        # Check for duplicate name
        if supplier_name in existing_names:
            error_message = "Supplier already exists with name '{}'. Please add full name and try again.".format(
                supplier_name)
            errors.append({'status': 'error', 'message': error_message})

        # If there are any errors, return them in the response
        if errors:
            return JsonResponse({'status': 'error', 'errors': errors})

        # Create a new Supplier object
        new_supplier = Supplier(
            supplier_name=supplier_name,
            address=address,
            phone=phone,
            comments=comments
        )

        # Save the new Supplier object to the database
        try:
            new_supplier.save()
            return JsonResponse({'status': 'success', 'message': 'Supplier added successfully.'})
        except Exception as e:
            # Handle any exceptions that occur during the save operation
            return JsonResponse({'status': 'error', 'message': f'Error adding supplier: {str(e)}'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})


@csrf_exempt
def add_customer(request):
    """
    Handles POST requests to add a new Customer to the database.

    This view function is designed to be used with a POST request containing the necessary
    data for creating a new Customer object. It checks for the presence of required fields,
    ensures the customer name is unique, and then creates a new Customer object with the
    provided data and saves it to the database.

    Parameters:
    - request (HttpRequest): The incoming HTTP request.

    Returns:
    - JsonResponse: A JSON response indicating the success or failure of the operation.
    """
    if request.method == 'POST':
        # Extract data from the request
        customer_name = request.GET.get('customer_name')
        address = request.GET.get('address')
        phone = request.GET.get('phone')
        comments = request.GET.get('comments')

        # Initialize an empty list to collect error messages
        errors = []

        # Check if all required fields are provided
        if not customer_name:
            errors.append({'status': 'error', 'message': 'Customer name is required.'})
        if not address:
            errors.append({'status': 'error', 'message': 'Address is required.'})
        if not phone:
            errors.append({'status': 'error', 'message': 'Phone is required.'})
        if not comments:
            errors.append({'status': 'error', 'message': 'Comments are required.'})

        # Load existing customer names from DB
        existing_names = [customer.customer_name for customer in Customer.objects.all().values_list('customer_name')]
        # Check for duplicate name
        if customer_name in existing_names:
            error_message = f"Customer already exists with name '{customer_name}'. Please add full name and try again."
            errors.append({'status': 'error', 'message': error_message})

        # If there are any errors, return them in the response
        if errors:
            return JsonResponse({'status': 'error', 'errors': errors})

        # Create a new Customer object
        new_customer = Supplier(
            supplier_name=customer_name,
            address=address,
            phone=phone,
            comments=comments
        )

        # Save the new Customer object to the database
        try:
            new_customer.save()
            return JsonResponse({'status': 'success', 'message': f'New Customer {customer_name} has been added to database successfully!'})
        except Exception as e:
            # Handle any exceptions that occur during the save operation
            return JsonResponse({'status': 'error', 'message': f'Error adding Customer: {str(e)}'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})


@csrf_exempt
def get_materialTypes(request):
    """
    Handles GET requests to retrieve all material names from the database.

    This view function is designed to be used with a POST request. It queries the
    MaterialType model for all instances and returns the names in a JSON response.

    Parameters:
    - request (HttpRequest): The incoming HTTP request.

    Returns:
    - JsonResponse: A JSON response containing all material names.
    """
    if request.method == 'GET':
        try:
            # Query the MaterialType model for all instances
            material_types = MaterialType.objects.all()
            # Extract and return the names in a JSON response
            material_names = [material_type.name for material_type in material_types]
            return JsonResponse({'status': 'success', 'material_names': material_names})
        except Exception as e:
            # Handle any exceptions that occur during the query operation
            return JsonResponse({'status': 'error', 'message': f'Error retrieving material names: {str(e)}'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})


@csrf_exempt
def get_supplierNames(request):
    """
    Handles GET requests to retrieve all supplier names from the database.

    This view function is designed to be used with a POST request. It queries the
    Supplier model for all instances and returns the names in a JSON response.

    Parameters:
    - request (HttpRequest): The incoming HTTP request.

    Returns:
    - JsonResponse: A JSON response containing all supplier names.
    """
    if request.method == 'GET':
        try:
            # Query the Supplier model for all instances
            suppliers = Supplier.objects.all()
            # Extract and return the names in a JSON response
            supplier_names = [supplier.supplier_name for supplier in suppliers]
            return JsonResponse({'status': 'success', 'supplier_names': supplier_names})
        except Exception as e:
            # Handle any exceptions that occur during the query operation
            return JsonResponse({'status': 'error', 'message': f'Error retrieving supplier names: {str(e)}'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})


@csrf_exempt
def add_rawMaterial(request):
    """
    Handles POST requests to add a new RawMaterial to the database.

    This view function is designed to be used with a POST request containing the necessary
    data for creating a new RawMaterial object. It checks for the presence of required fields,
    creates a new RawMaterial object with the provided data, and saves it to the database.

    Parameters:
    - request (HttpRequest): The incoming HTTP request.

    Returns:
    - JsonResponse: A JSON response indicating the success or failure of the operation.
    """
    if request.method == 'POST':
        # Extract data from the request
        supplier_name = request.GET.get('supplier_name')
        material_type = request.GET.get('material_type')
        material_name = request.GET.get('material_name')
        comments = request.GET.get('comments')

        # Initialize an empty list to collect error messages
        errors = []

        # Check if all required fields are provided
        if not supplier_name:
            errors.append({'status': 'error', 'message': 'supplier name is required.'})
        if not material_type:
            errors.append({'status': 'error', 'message': 'material type is required.'})
        if not material_name:
            errors.append({'status': 'error', 'message': 'material name is required.'})
        if not comments:
            errors.append({'status': 'error', 'message': 'Comments are required.'})
        # Load existing material names from DB
        existing_names = [customer.customer_name for customer in RawMaterial.objects.all().values_list('material_name')]
        # Check for duplicate name
        if material_name in existing_names:
            error_message = f"Error: Material Name with name '{material_name}' already exist"
            errors.append({'status': 'error', 'message': error_message})

        # If there are any errors, return them in the response
        if errors:
            return JsonResponse({'status': 'error', 'errors': errors})

        # Create a new Customer object
        new_RawMaterial = RawMaterial(
            supplier=supplier_name,
            material_type=material_type,
            material_name=material_name,
            comments=comments
        )

        # Save the new Customer object to the database
        try:
            new_RawMaterial.save()
            return JsonResponse({'status': 'success',
                                 'message': f'New Material: {material_name} has been added to database successfully!'})
        except Exception as e:
            # Handle any exceptions that occur during the save operation
            return JsonResponse({'status': 'error', 'message': f'Error adding Customer: {str(e)}'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})


def get_consumption_profile_names(request):
    """
    Retrieves all profile names from the Consumption model and returns them as a JSON response.

    This view function is designed to be accessed via a GET request. It queries the database for all
    Consumption records, extracts the 'profile_name' attribute from each record, and returns these names
    in a JSON format. The response includes a list of profile names under the key 'profile_names'.

    If an exception occurs during the process, the function returns a JSON response with an error message
    and a  500 status code.

    Returns:
        JsonResponse: A JSON response containing a list of profile names or an error message.

    Example usage:
        GET /consumption/profile_names/

    Example response:
        {
            "profile_names": ["Profile1", "Profile2", "Profile3"]
        }
    """
    if request.method == 'GET':
        try:
            # Retrieve all consumption records
            consumptions = Consumption.objects.all()

            # Extract the profile names from each record
            profile_names = [consumption.profile_name for consumption in consumptions]

            # Return the profile names as a JSON response
            return JsonResponse({'profile_names': profile_names}, status=200)

        except Exception as e:
            # Return a   500 error for any exceptions
            return JsonResponse({'error': str(e)}, status=500)


@csrf_exempt
def add_reel(request):
    if request.method == 'POST':
        # Extract data from the request
        reel_number = request.GET.get('reel_number')
        width = request.GET.get('width')
        gsm = request.GET.get('gsm')
        length = request.GET.get('length')
        breaks = request.GET.get('breaks')
        grade = request.GET.get('grade')
        consumption_profile_name = request.GET.get('consumption_profile_name')


        # Initialize an empty list to collect error messages
        errors = []

        # Check if all required fields are provided
        if not reel_number:
            errors.append({'status': 'error', 'message': 'reel number is required.'})
        if not width:
            errors.append({'status': 'error', 'message': 'width is required.'})
        if not gsm:
            errors.append({'status': 'error', 'message': 'gsm is required.'})
        if not length:
            errors.append({'status': 'error', 'message': 'length is required.'})
        if not breaks:
            errors.append({'status': 'error', 'message': 'breaks is required.'})
        if not grade:
            errors.append({'status': 'error', 'message': 'grade is required.'})
        if not consumption_profile_name:
            errors.append({'status': 'error', 'message': 'consumption profile name is required.'})

        # If there are any errors, return them in the response
        if errors:
            return JsonResponse({'status': 'error', 'errors': errors})

        # Create new product (reel) and consumption objects
        product = Product.objects.create(
            reel_number=reel_number,
            width=width,
            gsm=gsm,
            length=length,
            breaks=breaks,
            grade=grade,
            location=Anbar.objects.get(pk=1),
            status='In-stock',
        )
        consumption = Consumption.objects.create(
            consumption_profile=Consumption.objects.get(pk=consumption_profile_name),
            material_type=product.reel_number,  # Using reel number as material type
            material_name='New Material',  # Default material name
            quantity=1,  # Assuming quantity is 1 for new reels
            status='Completed',
        )
        # Update Anbar_XXX (details needed based on the PDF diagram)
        # ...

        # Save the new object to the databases
        try:
            product.save()
            consumption.save()
            # product.save()
            return JsonResponse({'status': 'success',
                                 'message': f'New Reel Number:{reel_number} has been added to database successfully!'})
        except Exception as e:
            # Handle any exceptions that occur during the save operation
            return JsonResponse({'status': 'error', 'message': f'Error: Reel No. already exist'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})



def add_shipment(request):
    """
    Creates a new shipment based on user input.

    Handles both POST and GET requests:
        - POST: Processes form data and creates a shipment, returning JSON response.

    Validates required fields and performs appropriate actions based on shipment type.
    """
    if request.method == 'POST':
        # Extract data from request.POST
        data = dict(request.GET.items())

    return JsonResponse()



def new_material_type(request):
    existing_types = MaterialType.objects.all()
    if request.method == 'POST':
        name = request.GET['name']
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
        name = request.GET['name']
        count_kg = request.GET.get('count_kg', None)  # Handle optional field
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
        location_name = request.GET.get('location_name')

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


def add_reeel(request):
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
        reel_number = request.GET.get('reel_number').strip()
        width = float(request.GET.get('width')) if request.GET.get('width') else None
        gsm = float(request.GET.get('gsm')) if request.GET.get('gsm') else None
        length = float(request.GET.get('length')) if request.GET.get('length') else None
        breaks = int(request.GET.get('breaks')) if request.GET.get('breaks') else None
        grade = request.GET.get('grade').strip() if request.GET.get('grade') else None
        consumption_profile_id = int(request.GET.get('consumption_profile'))

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
        license_number = request.GET.get('license_number')
        supplier_id = request.GET.get('supplier')
        material_type_id = request.GET.get('material_type')
        material_id = request.GET.get('material')
        customer_id = request.GET.get('customer')
        shipment_type = request.GET.get('shipment_type')

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

# @csrf_exempt
# def apiHandler(request, api):
    # if request.method == 'POST':
    #     license_number = request.GET.get('license_number')
    #     driver_name = request.GET.get('driver_name')
    #     driver_doc = request.GET.get('driver_doc')
    #     phone = request.GET.get('phone')
    #     status = request.GET.get('status')
    #     location = request.GET.get('location')
    #     comments = request.GET.get('comments')
    #     print(dict(request.GET.items()))
    #
    #     return JsonResponse({'status':'ok'})
    # else:
    #     # Handle non-POST requests
    #     return JsonResponse({'error': 'Method not allowed'}, status=405)
    # if api == 'add'