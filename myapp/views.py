import json
import logging
from django.shortcuts import render, redirect
from .models import *
from django.http import JsonResponse
from django.core.exceptions import ValidationError
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.db import connection
from django.apps import apps
from django.db import models
from django.apps import apps
from django.db.models.base import ModelBase
from jdatetime import datetime
import uuid

# Create your views here.

# Incoming process:
# Add Truck
# Add Shipments
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
            # Attempt to retrieve a Truck object with the provided license number
            # truck = Truck.objects.get(license_number=license_number)
            if Truck.objects.filter(license_number=license_number).exists():
                # If the truck exists, return a success response
                return JsonResponse({'isExists': 'true', 'message': 'License number exists.'})
            else:
                # If the truck does not exist, return an error response
                return JsonResponse({'isExists': 'false', 'message': 'License number does not exist.'})
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
        # Extract data from the request
        license_number = request.GET.get('license_number')
        driver_name = request.GET.get('driver_name')
        driver_doc = request.GET.get('driver_doc')
        phone = request.GET.get('phone')
        username = request.GET.get('username')
        errors = []
        print(driver_name)
        # Create new truck
        new_truck = Truck(
            license_number=license_number,
            driver_name=driver_name,
            driver_doc=driver_doc,
            phone=phone,
            username=username,
            logs=f'{username} Created NOW at time ({str(datetime.now())}),'
        )

        errors = []
        # Save the new Customer object to the database
        try:
            new_truck.save()
            return JsonResponse({'status': 'success', 'message': f'New license number {license_number} has been added to database successfully!'})
        except Exception as e:
            print(e)
            print(license_number)
            # Handle any exceptions that occur during the save operation
            errors.append({'status': 'error', 'message': f'Error adding license number: {str(e)}'})
            return JsonResponse({'status': 'error', 'errors': errors})
    if request.method == 'GET':
        return render(request, 'add_truck.html')

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
        username = request.GET.get('username')

        # Initialize an empty list to collect error messages
        errors = []

        # Check if all required fields are provided
        if not supplier_name:
            errors.append({'error': 'supplier_name', 'message': 'نام تامین کننده را وارد کنید.'})
        if not address:
            errors.append({'error': 'address', 'message': 'ادرس را وارد کنید.'})
        if not phone:
            errors.append({'error': 'phone', 'message': 'شماره همراه را وارد کنید.'})
        if not username:
            errors.append({'error': 'username', 'message': 'نام کاربری را وارد کنید.'})

        # Load existing supplier names from DB
        if Supplier.objects.filter(supplier_name=supplier_name).exists():
            error_message = f"در حال حاضر یک تامین کننده با نام {supplier_name} در دیتابیس وجود دارد."
            errors.append({'status': 'error', 'message': error_message})
        # Check for duplicate name
        # If there are any errors, return them in the response
        if errors:
            return JsonResponse({'status': 'error', 'errors': errors})
        print(datetime.now())
        # Create a new Supplier object
        new_supplier = Supplier(
            supplier_name=supplier_name,
            address=address,
            phone=phone,
            comments=comments,
            username=username,
            status='Active',
            logs =f'{username} Created NOW at time ({str(datetime.now())}),'
        )

        # Save the new Supplier object to the database
        try:
            new_supplier.save()
            return JsonResponse({'status': 'success', 'message': 'Supplier added successfully.'})
        except Exception as e:
            # Handle any exceptions that occur during the save operation
            errors.append({'status': 'error', 'message': f'Error adding supplier: {str(e)}'})
            return JsonResponse({'status': 'error', 'errors': errors})
    else:
        return render(request, 'add_supplier.html')


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
        username = request.GET.get('username')
        # Initialize an empty list to collect error messages
        errors = []

        # Check if all required fields are provided
        if not customer_name:
            errors.append({'status': 'error', 'message': 'اسم مشتری را وارد کنید'})
        if not address:
            errors.append({'status': 'error', 'message': 'آدرس مشتری را وارد کنید'})
        if not phone:
            errors.append({'status': 'error', 'message': 'شماره همراه مشتری را وارد کنید'})
        if not username:
            errors.append({'error': 'username', 'message': 'نام کاربری را وارد کنید.'})

        # Load existing customer names from DB Check for duplicate name
        if Customer.objects.filter(customer_name=customer_name).exists():
            error_message = f"در حال حاضر یک مشتری با نام {customer_name} در دیتابیس وجود دارد."
            errors.append({'status': 'error', 'message': error_message})

        # If there are any errors, return them in the response
        if errors:
            return JsonResponse({'status': 'error', 'errors': errors})

        # Create a new Customer object
        new_customer = Customer(
            customer_name=customer_name,
            address=address,
            phone=phone,
            comments=comments,
            username=username,
            status='Active',
            logs=f'{username} Created NOW at time ({str(datetime.now())}),'
        )

        # Save the new Customer object to the database
        try:
            new_customer.save()
            return JsonResponse({'status': 'success', 'message': f'New Customer {customer_name} has been added to database successfully!'})
        except Exception as e:
            # Handle any exceptions that occur during the save operation
            errors.append({'status': 'error', 'message': f'Error adding Customer: {str(e)}'})
            return JsonResponse({'status': 'error', 'errors': errors})
    else:
        return render(request, 'add_customer.html')


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
            supplier_name = request.GET.get('supplier_name')
            # Query the MaterialType model for all instances
            material_types = MaterialType.objects.filter(supplier_name=supplier_name)
            # Extract and return the names in a JSON response
            material_type = [material_type.material_type for material_type in material_types]
            return JsonResponse({'status': 'success', 'material_types': material_type})
        except Exception as e:
            # Handle any exceptions that occur during the query operation
            return JsonResponse({'status': 'error', 'message': f'Error retrieving material names: {str(e)}'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})


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
            suppliers = Supplier.objects.filter(status="Active")
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
        username = request.GET.get('username')

        # Initialize an empty list to collect error messages
        errors = []

        # Check if all required fields are provided
        if not supplier_name:
            errors.append({'status': 'error', 'message': 'اسم تامین کننده ا انتخاب کنید'})
        if not material_type:
            errors.append({'status': 'error', 'message': 'نوع ماده را انتخاب کنید'})
        if not material_name:
            errors.append({'status': 'error', 'message': 'اسم ماده را وارد کنید'})
        if not username:
            errors.append({'status': 'error', 'message': 'نام کاربری را وارد کنید'})
        # If there are any errors, return them in the response
        # Load existing customer names from DB Check for duplicate name
        if RawMaterial.objects.filter(material_name=material_name).exists():
            error_message = f"در حال حاضر یک حنس با نام {material_name} در سیستم وجود دارد."
            errors.append({'status': 'error', 'message': error_message})
        if errors:
            return JsonResponse({'status': 'error', 'errors': errors})

        # Create a new Customer object
        new_RawMaterial = RawMaterial(
            supplier_name=supplier_name,
            material_type=material_type,
            material_name=material_name,
            comments=comments,
            username=username,
            logs=f'{username} Created NOW at time ({str(datetime.now())}),'
        )

        # Save the new Customer object to the database
        try:
            new_RawMaterial.save()
            return JsonResponse({'status': 'success',
                                 'message': f'New Material: {material_name} has been added to database successfully!'})
        except Exception as e:
            # Handle any exceptions that occur during the save operation
            errors.append({'status': 'error', 'message': f'Error adding Customer: {str(e)}'})
            return JsonResponse({'status': 'error', 'errors': errors})
    else:
        return render(request, 'add_rawMaterial.html')


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

def get_reel_number(request):
    if request.method == 'GET':
        # Load the last reel number from the Products DB
        try:
            last_reel_number = Products.objects.latest('reel_number').reel_number
            width = Products.objects.latest('width').width
            GSM = Products.objects.latest('gsm').gsm
            length = Products.objects.latest('length').length
            breaks = Products.objects.latest('breaks').breaks
            grade = Products.objects.latest('grade').grade
            profile_name = Products.objects.latest('profile_name').profile_name

        except Products.DoesNotExist:
            last_reel_number = 0
            width = 0
            GSM = 0
            length = 0
            breaks = 0
            grade = 0
            profile_name = 0
        next_reel_number = int(last_reel_number) + 1
        data = {
            'next_reel_number': next_reel_number,
            'width': width,
            'GSM': GSM,
            'length': length,
            'breaks': breaks,
            'grade': grade,
            'profile_name': profile_name,
        }
        return JsonResponse(data=data, status=200)


@csrf_exempt
def add_new_reel(request):
    """
    Handles the addition of a new reel to the system.

    This function processes a POST request to add a new reel, which involves
    creating new records in the Products and AnbarSalonTolid models, and updating
    the Consumption model based on the selected consumption profile. The function
    also validates the form data and handles errors gracefully by returning
    appropriate HTTP status codes and error messages.

    Parameters:
        request (HttpRequest): The HTTP request object containing the form data.

    Returns:
        JsonResponse: A JSON response containing a success message and the new reel number
                      if the operation is successful, or an error message if an error occurs.

    Raises:
        ValidationError: If the form data fails validation.

    Example usage:
        POST /add_new_reel/
        Form data: {
            "reel_number": "RN123",
            "width":  100,
            "gsm":  80,
            "length":  200,
            "breaks": "B10",
            "grade": "Grade A",
            "consumption_profile": "Profile1"
        }

    Example response (success):
        {
            "message": "Reel number has been added",
            "reel_number": "RN124"
        }

    Example response (error):
        {
            "error": "Invalid form data"
        }
    """
    if request.method == 'POST':
        try:
            # Extract form data from the request
            reel_number = request.GET.get('reel_number')
            width = request.GET.get('width')
            gsm = request.GET.get('gsm')
            length = request.GET.get('length')
            breaks = request.GET.get('breaks')
            grade = request.GET.get('grade')
            consumption_profile_name = request.GET.get('consumption_profile_name')
            qr_code = request.GET.get('qr_code')

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
            # from django.db.models import Q
            # consumptions  = Consumption.objects.filter(Q(supplier_name=supplier_name) & Q(material_name=material_name)
            # Create a new Products record
            new_product = Products(
                qr_code=qr_code,
                reel_number=reel_number,
                width=width,
                gsm=gsm,
                length=length,
                breaks=breaks,
                grade=grade,
                profile_name=consumption_profile_name,
                receive_date=str(datetime.now()),
                logs=f'Created NOW at time ({str(datetime.now())}),',
            )
            new_product.save()

            # Create a new Anbar_Salon_Tolid record
            new_anbar_record = Anbar_Salon_Tolid(
                qr_code=qr_code,
                location='Anbar_Salon_Tolid',
                status='In-stock',
                reel_number=reel_number,
                width=width,
                gsm=gsm,
                length=length,
                breaks=breaks,
                grade=grade,
                profile_name=consumption_profile_name,
                receive_date=str(datetime.now()),
            )
            new_anbar_record.save()

            # Update the Consumption DB based on the selected consumption profile name
            Consumption.objects.filter(profile_name=consumption_profile_name).update(
                reel_number=reel_number,
            )

            # inserts:
            cp = Consumption.objects.filter(profile_name=consumption_profile_name)
            # Get all table names from the database
            all_table_names = connection.introspection.table_names()
            anbar_table_names = [name for name in all_table_names if name.startswith('Anbar_')]
            # Dynamically get the model based on the anbar_name
            for anbar_name in anbar_table_names:
                AnbarModel = apps.get_model('myapp', anbar_name)
                for profile in cp:
                    AnbarModel.objects.filter(supplier_name=profile.supplier_name, material_name=profile.material_name, status='In-stock',).update(
                        status='Used',
                        supplier_name=profile.supplier_name,
                        material_name=profile.material_name,
                        receive_date=str(datetime.now()),
                    )
            # Return a success response
            return JsonResponse({'status': 'success', 'message': 'Reel number has been added'}, status=200)

        except ValidationError as e:
            # Return a validation error response
            return JsonResponse({'error': str(e)}, status=400)

        except Exception as e:
            print(e)
            # Return a general error response
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return render(request, 'add_new_reel.html')


def get_license_numbers(request):
    """
    Handles GET requests to retrieve all license numbers of trucks.

    This function queries the Truck model for all records and returns the license numbers
    in a JSON response. It handles errors by returning appropriate HTTP status codes
    and error messages.

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        JsonResponse: A JSON response containing a list of all license numbers if the
                      operation is successful, or an error message if an error occurs.
    """
    if request.method == 'GET':
        try:
            # Query the Truck model for all records
            trucks = Truck.objects.all()

            # Extract the license numbers from the queryset
            license_numbers = [truck.license_number for truck in trucks]

            free_truck = Truck.objects.filter(status='Free')
            free_truck = [truck.license_number for truck in free_truck]

            # Return the license numbers as a JSON response
            return JsonResponse({'license_numbers': license_numbers, 'free_truck': free_truck}, status=200)

        except Exception as e:
            # Return a general error response
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)


def get_material_names(request):
    """
    Handles GET requests to retrieve all material names from the RawMaterial model.
    """
    if request.method == 'GET':
        try:
            supplier_name = request.GET.get('supplier_name')
            print(request.GET)
            if not supplier_name:
                return JsonResponse({'error': 'Supplier name is required'}, status=400)

            # Query the RawMaterial model for all records
            materials = RawMaterial.objects.filter(supplier_name=supplier_name)

            # Extract the material names from the queryset
            material_names = [material.material_name for material in materials]

            # Return the material names in a JSON response
            return JsonResponse({'material_names': material_names}, status=200)

        except Exception as e:
            # Log the error for debugging
            logging.error(f"Error in get_material_names: {e}")
            # Return a general error response
            return JsonResponse({'error': 'Internal Server Error'}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)


def get_customer_names(request):
    """
    Handles GET requests to retrieve all customer names from the RawMaterial model.

    This function queries the RawMaterial model for all records and returns the
    customer names in a JSON response. If an error occurs during the process,
    it returns an appropriate HTTP status code and error message.

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        JsonResponse: A JSON response containing a list of all material names
                      if the operation is successful, or an error message if an error occurs.
    """
    if request.method == 'GET':
        try:
            # Query the RawMaterial model for all records
            Customers = Customer.objects.all()

            # Extract the material names from the queryset
            customer_names = [Customer.customer_name for Customer in Customers]

            # Return the material names in a JSON response
            return JsonResponse({'customer_names': customer_names}, status=200)

        except Exception as e:
            # Return a general error response
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)


@csrf_exempt
def add_shipment(request):
    if request.method == 'POST':
        # Extract data from request.GET
        license_number = request.GET.get('license_number')
        supplier_name = request.GET.get('supplier_name')
        material_type = request.GET.get('material_type')
        material_name = request.GET.get('material_name')
        shipment_type = request.GET.get('shipment_type')
        customer_name = request.GET.get('customer_name')
        username = request.GET.get('username')

        # Check required fields
        errors = []
        # if not license_number:
        #     errors.append('پلاک را انتخاب کنید')
        # if not supplier_name:
        #     errors.append('سام تامین کننده را انتخاب کنید')
        # if not material_type:
        #     errors.append('نوع ماده را انتخاب کنید')
        # if not material_name:
        #     errors.append('اسم ماده را انتخاب کنید')
        # if not shipment_type:
        #     errors.append('نوع بار نامه را انخاب کنید')
        # if not customer_name:
        #     errors.append('اسم مشتری را انخاب کنید')
        # if not username:
        #     errors.append('نام کاربری را وارد کنید')

        if errors:
            return JsonResponse({'status': 'error', 'errors': errors})

        else:
            print(shipment_type)
            # Create new shipment
            if shipment_type == "Incoming":
                shipment = Shipments(
                    truck_id=Truck.objects.get(license_number=license_number),
                    license_number=license_number,
                    supplier_name=supplier_name,
                    material_type=material_type,
                    material_name=material_name,
                    shipment_type=shipment_type,
                    status='Registered',
                    location='Entrance',
                    username=username,
                    entry_time=str(datetime.now()),
                    logs=f'{username} Now created NOW at time ({str(datetime.now())}),'
                )
            else:
                shipment = Shipments(
                    truck_id=Truck.objects.get(license_number=license_number),
                    license_number=license_number,
                    shipment_type=shipment_type,
                    customer_name=customer_name,
                    status='Registered',
                    location='Entrance',
                    username=username,
                    entry_time=str(datetime.now()),
                    logs=f'{username} Now created NOW ({str(datetime.now())}),'
                )

            # change Truck status to Busy
            try:
                # Use update to change the status atomically
                Truck.objects.filter(license_number=license_number).update(status='Busy')
            except Truck.DoesNotExist:
                return JsonResponse({'status': 'error', 'message': 'هیچ کامیونی با این پلاک وجود ندارد.'}, status=404)

            # Save the new Shipment object to the database
            try:
                shipment.save()
                return JsonResponse({'status': 'success', 'message': 'بار نامه با موفقیت اضافه شد.'})

            except Exception as e:
                # Handle any exceptions that occur during the save operation
                return JsonResponse({'status': 'error', 'message': f'Error adding supplier: {str(e)}'})
    else:
        return render(request, 'add_shipment.html')


# Weight Station/Create Orders

def weight_station_panel(request):
    if request.method == 'GET':
        return render(request, 'weight_station_panel.html')


@csrf_exempt
def get_shipment_license_numbers(request):
    """
    Handles GET requests to retrieve license numbers of shipments based on status .
    """
    if request.method == 'POST':
        try:
            status = request.GET.get('status')
            location = request.GET.get('location')
            # Query the Shipments model for records with status 'Registered'
            shipments = Shipments.objects.filter(status=status, location=location)
            # Extract the license numbers from the queryset
            license_numbers = [shipment.license_number for shipment in shipments]

            # Return the license numbers in a JSON response
            return JsonResponse({'license_numbers': license_numbers}, status=200)

        except Exception as e:
            # Return a general error response
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

@csrf_exempt
def get_shipment_license_numbers_by_status(request, status):
    """
    Handles GET requests to retrieve license numbers of shipments based on status .
    """
    if request.method == 'GET':
        try:
            # Query the Shipments model for records with status 'Registered'
            registered_shipments = Shipments.objects.filter(status=status)

            # Extract the license numbers from the queryset
            license_numbers = [shipment.license_number for shipment in registered_shipments]

            # Return the license numbers in a JSON response
            return JsonResponse({'license_numbers': license_numbers}, status=200)

        except Exception as e:
            # Return a general error response
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)


@csrf_exempt
def get_shipment_license_numbers_outgoing_by_status(request, status):
    """
    Handles GET requests to retrieve license numbers of shipments based on status .
    """
    if request.method == 'GET':
        try:
            # Query the Shipments model for records with status 'Registered'
            registered_shipments = Shipments.objects.filter(location=status, shipment_type='Outgoing')


            # Extract the license numbers from the queryset
            license_numbers = [shipment.license_number for shipment in registered_shipments]

            # Return the license numbers in a JSON response
            return JsonResponse({'license_numbers': license_numbers}, status=200)

        except Exception as e:
            # Return a general error response
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)


@csrf_exempt
def get_shipment_license_numbers_by_location(request, location):
    """
    Handles GET requests to retrieve license numbers of shipments based on location .
    """
    if request.method == 'GET':
        try:
            # Query the Shipments model for records with status 'Registered'
            registered_shipments = Shipments.objects.filter(location=location)

            # Extract the license numbers from the queryset
            license_numbers = [shipment.license_number for shipment in registered_shipments]

            # Return the license numbers in a JSON response
            return JsonResponse({'license_numbers': license_numbers}, status=200)

        except Exception as e:
            # Return a general error response
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)


@csrf_exempt
def get_shipment_details_by_license_number(request):
    """
    Handles GET requests to retrieve shipment details (supplier_name, material_type, material_name, weight1, weight2, net_weight, unload_location, unit, quantity, quality) based on a provided license number.
    """
    if request.method == 'POST':
        try:
            # Extract data from request.GET
            license_number = request.GET.get('license_number')
            if license_number:
                # Filter Shipments based on the license_number
                shipment = Shipments.objects.filter(license_number=license_number).first()
                if shipment:
                    # Prepare the data to be returned
                    shipment_details = {
                        'supplier_name': shipment.supplier_name,
                        'material_type': shipment.material_type,
                        'material_name': shipment.material_name,
                        'weight1': shipment.weight1,
                        'weight2': shipment.weight2,
                        'net_weight': shipment.net_weight,
                        'unload_location': shipment.unload_location,
                        'unit': shipment.unit,
                        'quantity': shipment.quantity,
                        'quality': shipment.quality,
                    }
                    # Return the shipment details in a JSON response
                    return JsonResponse(shipment_details, status=200)
                else:
                    return JsonResponse({'error': 'No shipment found with the provided license number.'}, status=404)
            else:
                return JsonResponse({'error': 'License number is required.'}, status=400)
        except Exception as e:
            # Return a general error response
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)


@csrf_exempt
def get_shipment_details2_by_license_number(request):
    """
    Handles GET requests to retrieve shipment details (supplier_name, material_type, material_name, weight1, weight2, net_weight, unload_location, unit, quantity, quality) based on a provided license number.
    """
    if request.method == 'POST':
        try:
            # Extract data from request.GET
            license_number = request.GET.get('license_number')
            if license_number:
                # Filter Shipments based on the license_number
                shipment = Shipments.objects.filter(license_number=license_number,  status='Office',location='Office', shipment_type='Outgoing').first()

                if shipment:
                    # Prepare the data to be returned
                    shipment_details = {
                    'customer_name': shipment.customer_name,
                    'list_of_reels': shipment.list_of_reels,
                    'weight1': shipment.weight1,
                    'weight2': shipment.weight2,
                    'net_weight': shipment.net_weight,
                    'unloaded_location': shipment.unload_location,
                    'consuption_profile_name': shipment.profile_name,
                    }
                    # Return the shipment details in a JSON response
                    return JsonResponse(shipment_details, status=200)
                else:
                    return JsonResponse({'error': 'No shipment found with the provided license number.'}, status=404)
            else:
                return JsonResponse({'error': 'License number is required.'}, status=400)
        except Exception as e:
            # Return a general error response
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)


@csrf_exempt
def update_weight1(request):
    """
    Handles a POST request to update the weight1 field of a Shipments instance.

    This view function expects the following data in the POST request:
    - shipment_id: The UUID of the Shipments instance to update.
    - weight1: The new weight1 value to set, as a string that can be converted to a float.
    - username: The username of the user making the request, used for comments.

    It performs the following operations:
    - Validates that the weight1 value is within the range of 9 to 38000 KG.
    - Retrieves the Shipments instance by its shipment_id.
    - Updates the weight1, weight1_time, and comments fields of the Shipments instance.
    - Saves the changes to the database.
    - Returns a JSON response indicating success or failure, along with a message.

    Parameters:
    - request: The Django HttpRequest object.

    Returns:
    - A JsonResponse object with a success flag and a message.
    """
    if request.method == 'POST':
        # Assuming shipment_id and weight1 are sent in the POST data
        license_number = request.GET.get('license_number')
        weight1 = request.GET.get('weight1')
        username = request.GET.get('username')

        # Check required fields
        errors = []
        if not license_number:
            errors.append('پلاک را انتخاب کنید')
        if not weight1:
            errors.append('وزن اولیه را وارد کنید')
        if not username:
            errors.append('نام کاربری را وارد کنید')
        # Convert weight1 to a decimal and validate the range
        weight1 = float(weight1)
        if weight1 < 9 or weight1 > 38000:
            errors.append('وزن وارد شده باید بین 9 تا 38000 کیلوگرم باشد.')

        if errors:
            return JsonResponse({'status': 'error', 'errors': errors})
        else:
            try:
                Shipments.objects.filter(license_number=license_number, status='Registered', location='Entrance').update(
                    weight1=weight1,
                    username=username,
                    weight1_time=str(datetime.now()),
                    comments=f"{username} updated Weight1",
                    status='LoadingUnloading',
                    location='Weight1',
                    logs=f'{username} Weight1 NOW ({str(datetime.now())}),'
                )
                return JsonResponse({'status': 'success', 'message': 'وزن اولیه بار نامه با موفقیت آپدیت شد.'})

            except Exception as e:
                # Handle any exceptions that occur during the save operation
                return JsonResponse({'status': 'error', 'message': f'Error updating shipment weight1: {str(e)}'})
    return render(request, 'update_weight1.html')


def show_weight1(request):
    """
    Handles GET requests to retrieve the weight1 of a shipment based on a provided license number.

    This view function extracts the license number from the request's query parameters,
    filters the Shipments model to find a shipment with the matching license number,
    and returns the weight1 of the found shipment in a JSON response.

    If no shipment is found with the provided license number, a JSON response with an error message
    and a 404 status code is returned. If the license number is not provided, a JSON response with
    an error message and a 400 status code is returned.

    Parameters:
    - request (HttpRequest): The HTTP request object.

    Returns:
    - JsonResponse: A JSON response containing the weight1 of the shipment if found, or an error message.
    """
    if request.method == 'GET':
        # Extract data from request.GET
        license_number = request.GET.get('license_number')
        print(license_number)
        if license_number:
            # Filter Shipments based on the license_number
            shipment = Shipments.objects.filter(license_number=license_number).first()
            if shipment:
                # Return the weight1 of the shipment
                return JsonResponse({'weight1': shipment.weight1})
            else:
                return JsonResponse({'error': 'هیج بار نامه ای با شماره پلاک مورد نظر یافت نشد.'}, status=404)
        else:
            return JsonResponse({'error': 'شماره پلاک مورد نیازاست'}, status=400)


def update_weight2(request):
    """
    Handles a POST request to update the weight2 and net_weight of a Shipments instance.

    This function retrieves a Shipments instance based on the provided license number, validates the weight2 and net_weight values,
    updates the instance with the new weights, and saves the changes to the database. It returns a JSON response indicating
    the success or failure of the operation, along with appropriate messages.
    """
    if request.method == 'POST':
        # Extract data from the request
        license_number = request.GET.get('license_number')
        weight1 = request.GET.get('weight1')
        weight2 = request.GET.get('weight2')
        net_weight = request.GET.get('net_weight')
        username = request.GET.get('username')
        # Check required fields
        errors = []
        if not license_number:
            errors.append({'status': 'error', 'message': 'پلاک را انتخاب کنید'})
        if not weight1:
            errors.append({'status': 'error', 'message': 'وزن اولیه را وارد کنید'})
        if not weight2:
            errors.append({'status': 'error', 'message': 'وزن ثانویه را وارد کنید'})
        if not username:
            errors.append({'status': 'error', 'message': 'نام کاربری را وارد کنید'})
        try:
            weight1 = float(weight1)
            weight2 = float(weight2)
            net_weight = float(net_weight)
        except ValueError:
            errors.append({'status': 'error', 'message': 'وزن ثانویه و وزن خالص باید عدد باشند'})
        if not (9 <= weight2 <= 38000) or not (9 <= net_weight <= 38000):
            errors.append({'status': 'error', 'message': 'وزن ثاویه و وزن حالص  وارد شده باید بین 9 تا 38000 کیلوگرم باشند.'})
        # Check if the absolute difference between weight1 and weight2 equals net_weight
        if abs(weight1 - weight2) != net_weight:
            errors.append({'status': 'error', 'message': 'تفاوت  بین وزن اولیه و وزن ثانویه باید با وزن خالص برابر باشد.'})
        if errors:
            return JsonResponse({'status': 'error', 'errors': errors})
        else:
            try:
                # Update the Shipments instance
                Shipments.objects.filter(license_number=license_number, status='LoadedUnloaded', location='Weight2').update(
                    weight1=weight1,
                    weight2=weight2,
                    net_weight=net_weight,
                    username=username,
                    weight2_time=str(datetime.now()),
                    status='Office',
                    location='Office',
                    logs=f'{username} Weight2 NOW ({str(datetime.now())}),'
                )

                return JsonResponse({'status': 'success', 'message': f'Weight2 and Net Weight for Shipments with License Number {license_number} has been updated successfully.'})
            except Shipments.DoesNotExist:
                return JsonResponse({'status': 'error', 'message': f'Shipments with License Number {license_number} does not exist.'})
    else:
        return render(request, 'update_weight2.html')


@csrf_exempt
def create_purchase_order(request):
    """
    Handles the creation of a Purchase Order based on the provided algorithm.
    """
    if request.method == 'POST':
        try:
            # Extract data from request.GET
            license_number = request.GET.get('license_number')
            supplier_name = request.GET.get('supplier_name')
            material_type = request.GET.get('material_type')
            material_name = request.GET.get('material_name')
            weight1 = request.GET.get('weight1')
            weight2 = request.GET.get('weight2')
            net_weight = request.GET.get('net_weight')
            unloaded_location = request.GET.get('unloaded_location')
            unit = request.GET.get('unit')
            quantity = request.GET.get('quantity')
            quality = request.GET.get('quality')
            penalty = request.GET.get('penalty')
            price_pre_kg = request.GET.get('price_pre_kg')
            vat = request.GET.get('vat')
            total_price = request.GET.get('total_price')
            extra_cost = request.GET.get('extra_cost')
            invoice_status = request.GET.get('invoice_status')
            supplier_invoice = request.GET.get('supplier_invoice')
            payment_status = request.GET.get('payment_status')
            document_info = request.GET.get('document_info')
            commnet = request.GET.get('commnet')
            username = request.GET.get('username')

            # Check required fields
            errors = []
            if not license_number:
                errors.append({'status':'error', 'message': 'پلاک را انتخاب کنید'})
            if not supplier_name:
                errors.append({'status': 'error', 'message': 'اسم تامین کننده مورد نیاز است'})
            if not material_type:
                errors.append({'status':'error', 'message': 'نوغ ماده مورد نیاز است'})
            if not material_name:
                errors.append({'status':'error', 'message': 'اسم ماده مورد نیاز است'})
            if not weight1:
                errors.append({'status':'error', 'message': 'وزن اولیه مورد نیاز است'})
            if not weight2:
                errors.append({'status':'error', 'message': 'وزن ثانویه مورد نیاز است'})
            if not net_weight:
                errors.append({'status':'error', 'message': 'وزن خالص مورد نیاز است'})
            if not unloaded_location:
                errors.append({'status':'error', 'message': 'محل تخلیه شده مورد نیاز است'})
            if not unit:
                errors.append({'status': 'error', 'message': 'واخد مورد نیاز است'})
            if not quantity:
                errors.append({'status': 'error', 'message': 'کمیت (مقدار) مورد نیاز است'})
            if not quality:
                errors.append({'status': 'error', 'message': 'کیفیت مورد نیاز است'})
            if not penalty:
                errors.append({'status': 'error', 'message': 'مقدار جریمه را وارد کنید'})
            if not price_pre_kg:
                errors.append({'status':'error', 'message': 'مقدار قیمت هر کیلوگرم را وارد کنید'})
            if not vat:
                errors.append({'status':'error', 'message': 'مقدار مالیات بر ارزش افزوده را انتحاب کنید'})
            if not total_price:
                errors.append({'status':'error', 'message': 'مقدار قمیت کل را وارد کنید'})
            if not extra_cost:
                errors.append({'status':'error', 'message': ' مقدار هزینه اضافی را وارد کنید'})
            if not invoice_status:
                errors.append({'status':'error', 'message': 'وضعیت فاکتور را انتخاب کنید'})
            if not supplier_invoice:
                errors.append({'status': 'error', 'message': 'فرم فاکتور تامین کننده را پر کنید'})
            if not payment_status:
                errors.append({'status': 'error', 'message': 'وضعیت پرداخت را انتخاب کنید'})
            if not document_info:
                errors.append({'status':'error', 'message': 'اظلاعات سند را وارد کنید'})
            if not username:
                errors.append({'status':'error', 'message': 'فرم نام کاربری را پر کنید'})
            if errors:
                return JsonResponse({'status': 'error', 'errors': errors})
            else:
                Shipments.objects.filter(license_number=license_number, status='LoadingUnloading', location='Office').update(
                    vat=vat,
                    penalty=penalty,
                    price_pre_kg=price_pre_kg,
                    extra_cost=extra_cost,
                    invoice_status=invoice_status,
                    payment_status=payment_status,
                    document_info=document_info,
                    exit_time=str(datetime.now()),
                    receive_date=str(datetime.now()),
                    status='Delivered',
                    location='Delivered',
                    username=username,
                    comments=commnet,
                )

                # Update truck status and location
                Truck.objects.filter(license_number=license_number).update(
                    status='Free',
                    location='Entrance'
                )
                purchase = Purchases(
                    date=str(datetime.now()),
                    receive_date=str(datetime.now()),  # Assuming you want to set the current date/time
                    # supplier_id=Supplier.objects.get(supplier_name=supplier_name),
                    # truck_id=Truck.objects.get(license_number=license_number),
                    # material_id=MaterialType.objects.get(material_type=material_type),
                    # shipment_id=Shipments.objects.get(license_number=license_number),
                    material_type=material_type,
                    material_name=material_name,
                    unit=unit,
                    quantity=quantity,
                    quality=quality,
                    penalty=penalty,
                    weight1=weight1,
                    weight2=weight2,
                    net_weight=net_weight,
                    price_per_kg=price_pre_kg,
                    vat=vat,
                    total_price=total_price,
                    extra_cost=extra_cost,
                    invoice_status=invoice_status,
                    invoice_number=supplier_invoice,
                    status=payment_status,
                    document_info=document_info,
                    comments=commnet,
                    username=username,
                    logs=f'{username} Created PO NOW ({str(datetime.now())}),',
                )
                # Save the new purchase object to the database
                try:
                    purchase.save()
                    return JsonResponse({'status': 'success', 'message': 'purchase added successfully.'})
                except Exception as e:
                    # Handle any exceptions that occur during the save operation
                    return JsonResponse({'status': 'error', 'message': f'Error adding purchase: {str(e)}'})
            # Return success response
            return JsonResponse({'status': 'success', 'message': 'Purchase Order created successfully.'})

        except Exception as e:
            print(e)
            return JsonResponse({'status': 'error', 'message': str(e)})

    else:
        return render(request, 'create_purchase_order.html')


@csrf_exempt
def create_sales_order(request):
    """
    Function to create a Sales Order and update related entities based on the provided algorithm.
    """
    if request.method == 'POST':
        # Assuming the request data is in JSON format
        license_number = request.GET.get('lic_number')
        customer_name = request.GET.get('customer_name')
        list_of_reels = request.GET.get('list_of_reels')
        weight1 = request.GET.get('weight1')
        weight2 = request.GET.get('weight2')
        net_weight = request.GET.get('net_weight')
        loading_location = request.GET.get('loading_location')
        consuption_profile_name = request.GET.get('consuption_profile_name')
        price_pre_kg = request.GET.get('price_pre_kg')
        vat = request.GET.get('vat')
        total_price = request.GET.get('total_price')
        extra_cost = request.GET.get('extra_cost')
        invoice_status = request.GET.get('invoice_status')
        invoice_number = request.GET.get('invoice_number')
        payment_status = request.GET.get('payment_status')
        document_info = request.GET.get('document_info')
        commnet = request.GET.get('commnet')
        username = request.GET.get('username')

        errors = []
        if not license_number:
            errors.append({'status':'error', 'message': 'پلاک را انتخاب کنید'})
        if not customer_name:
            errors.append({'status':'error', 'message': 'اسم مشتری مورد نیاز است'})
        if not list_of_reels:
            errors.append({'status':'error', 'message': ''})
        if not weight1:
            errors.append({'status':'error', 'message': 'وزن اولیه مورد نیاز است'})
        if not weight2:
            errors.append({'status':'error', 'message': 'وزن ثانویه مورد نیاز است'})
        if not net_weight:
            errors.append({'status':'error', 'message': 'وزن خالص مورد نیاز است'})
        if not loading_location:
            errors.append({'status':'error', 'message': 'محل تخلیه شده مورد نیاز است'})
        if not consuption_profile_name:
            errors.append({'status':'error', 'message': 'پروفایل مصرفی مورد نیاز است'})
        if not price_pre_kg:
            errors.append({'status':'error', 'message': 'مقدار قیمت هر کیلوگرم را وارد کنید'})
        if not vat:
            errors.append({'status':'error', 'message': 'مقدار مالیات بر ارزش افزوده را انتحاب کنید'})
        if not total_price:
            errors.append({'status':'error', 'message': 'مقدار قمیت کل را وارد کنید'})
        if not extra_cost:
            errors.append({'status':'error', 'message': ' مقدار هزینه اضافی را وارد کنید'})
        if not invoice_status:
            errors.append({'status':'error', 'message': 'وضعیت فاکتور را انتخاب کنید'})
        if not invoice_number:
            errors.append({'status':'error', 'message': 'شماره فاکتور را وارد کنید'})
        if not payment_status:
            errors.append({'status':'error', 'message': 'وضعیت پرداخت را انتخاب کنید'})
        if not document_info:
            errors.append({'status':'error', 'message': 'اظلاعات سند را وارد کنید'})
        if not commnet:
            errors.append({'status':'error', 'message': 'فرم کامنت را پر کنید'})
        if not username:
            errors.append({'status':'error', 'message': 'فرم نام کاربری را پر کنید'})
        if errors:
            return JsonResponse({'status': 'error', 'errors': errors})
        else:
            try:
                customer = Customer.objects.get(customer_name=customer_name)
                truck = Truck.objects.get(license_number=license_number)
                shipment = Shipments.objects.get(license_number=license_number)

                # Create a new instance of the Sales model
                sale = Sales(
                    customer=customer,
                    truck=truck,
                    license_number=license_number,
                    list_of_reels=list_of_reels,
                    profile_name=consuption_profile_name,
                    weight1=weight1,
                    weight2=weight2,
                    net_weight=net_weight,
                    price_per_kg=price_pre_kg,
                    vat=vat,
                    total_price=total_price,
                    extra_cost=extra_cost,
                    invoice_status=invoice_status,
                    invoice_number=invoice_number,
                    status=payment_status,
                    document_info=document_info,
                    comments=commnet,
                    username=username,
                    shipment=shipment,
                    date=str(datetime.now()),  # Assuming you want to set the current date and time
                )
                # Save the instance
                sale.save()

                # Retrieve the shipment instance
                Shipments.objects.filter(license_number=license_number).update(
                    exit_time=str(datetime.now()),
                    status='Delivered',
                    location=customer_name,
                    username=username,
                    comments=commnet,
                )
                # Update truck status and location
                Truck.objects.filter(license_number=license_number).update(
                    status='Free',
                    location=customer_name
                )
                # Dynamically get the model based on the anbar_name
                AnbarModel = apps.get_model('myapp', loading_location)
                anbar_instance = AnbarModel.objects.create(
                    status='Delivered',
                    location=customer_name,
                    last_date=str(datetime.now()),
                )
                # Return a success response
                return JsonResponse({'status': 'success', 'message': 'Sales Order created successfully.'})

            except Shipments.DoesNotExist:
                return JsonResponse({'status': 'error', 'message': 'Shipments not found.'}, status=404)
            except Exception as e:
                print(e)
                return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    else:
        return render(request, 'create_sales_order.html')


def get_anbar_table_names(request):
    if request.method == 'GET':
        # Get all table names from the database
        all_table_names = connection.introspection.table_names()
        # Filter table names to include only those that start with 'Anbar_'
        anbar_table_names = [name for name in all_table_names if name.startswith('Anbar_')]
        return JsonResponse({'status':'success', 'data': anbar_table_names })


def get_unit_names(request):
    if request.method == 'GET':
        units = Unit.objects.all()
        unit_names = [unit.unit_name for unit in units]
        return JsonResponse({'unit_names':unit_names}, safe=False)
    else:
        return JsonResponse({"error": "Invalid request method"}, status=400)

def get_unit_names_based_on_supplier(request):
    if request.method == 'GET':
        supplier_name = request.GET.get('supplier_name')
        units = Unit.objects.filter(supplier_name=supplier_name)
        unit_names = [unit.unit_name for unit in units]
        return JsonResponse({'unit_names':unit_names}, safe=False)
    else:
        return JsonResponse({"error": "Invalid request method"}, status=400)

# Forklift Panel
def forklift_panel(request):
    if request.method == 'GET':
        return render(request, 'forklift_panel.html')


@csrf_exempt
def unload(request):
    """
    Handles the unloading of a shipment by updating the Shipments and AnbarGeneric models.

    This view processes a POST request containing shipment details, including the license number
    and the quantity to be unloaded. It updates the status of the shipment to 'LoadedUnloaded' and
    sets its location to 'Weight2'. Additionally, it creates new entries in the AnbarGeneric model
    (specifically Anbar_Akhal in this example) for each unit to be unloaded, setting their status to
    'In-stock' and their receive date to the current time.

    The view returns a JSON response indicating the success or failure of the operation, including a
    message detailing the outcome.

    Parameters:
    - request (HttpRequest): The HTTP request object containing the POST data.

    Returns:
    - JsonResponse: A JSON response indicating the success or failure of the operation, along with
                    a message detailing the outcome.

    Raises:
    - Http404: If the shipment with the provided license number does not exist.
    - HttpResponse: If an exception occurs during the operation, with a status code indicating the
                    type of error.

    Example POST data:
    {
        "license_number": "12345",
        "quantity": 5
    }
    """
    if request.method == 'POST':
        # Extract form data from the request
        license_number = request.GET.get('license_number')
        unloading_location = request.GET.get('unloading_location')
        unit = request.GET.get('unit')
        quantity = request.GET.get('quantity')
        quality = request.GET.get('quality')
        forklift_driver = request.GET.get('forklift_driver')

        # Initialize an empty list to collect error messages
        errors = []

        # Check if all required fields are provided
        if not license_number:
            errors.append({'status': 'error', 'message': 'پلاک را انتخاب کنید'})
        if not unloading_location:
            errors.append({'status': 'error', 'message': 'محل تخلیه را انتخاب کنید'})
        if not unit:
            errors.append({'status': 'error', 'message': 'واحد را انتخاب کنید'})
        if not quantity:
            errors.append({'status': 'error', 'message': 'کمیت(مقدار) را وارد کنید'})
        if not quality:
            errors.append({'status': 'error', 'message': 'کیفیت را وارد کنید'})
        if not forklift_driver:
            errors.append({'status': 'error', 'message': 'اسم راننده فورک لیفت را وارد کنید'})
        # If there are any errors, return them in the response
        if errors:
            return JsonResponse({'status': 'error', 'errors': errors})
        else:
            try:
                shipment = Shipments.objects.filter(license_number=license_number, status='LoadingUnloading', location='Weight1', shipment_type='Incoming')
                print([ship for ship in shipment])
                material_name = shipment[0].material_name
                supplier_name = shipment[0].supplier_name
                print('unloaded:',material_name, supplier_name)
                shipment.update(
                    unload_location=unloading_location,
                    unit=unit,
                    quantity=quantity,
                    quality=quality,
                    location='Weight2',
                    status='LoadedUnloaded',
                )
                # Dynamically get the model based on the anbar_name
                AnbarModel = apps.get_model('myapp', unloading_location)
                # Calculate the quantity to be unloaded
                quantity_to_unload = int(quantity)
                # Update AnbarGeneric (Anbar_Akhal in this case)
                for _ in range(quantity_to_unload):
                    # Insert data into the specific Anbar table
                    anbar_instance = AnbarModel.objects.create(
                        supplier_name=supplier_name,
                        material_name=material_name,
                        unit=unit,
                        status='In-stock',
                        location=unloading_location,
                        receive_date=str(datetime.now()),
                        last_date=str(datetime.now()),
                    )

                # Return a success response
                return JsonResponse({'status': 'success',
                                     'message': f' {quantity_to_unload}واحد به {license_number} اضافه شد.'})

            except Shipments.DoesNotExist:
                return JsonResponse({'status': 'error', 'message': 'Shipments not found.'}, status=404)
            except Exception as e:
                print(e)
                return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method.'}, status=400)


def get_widths_from_anbar_location(anbar_location, status):
    # Dynamically import the model class
    model_class = apps.get_model('myapp', anbar_location)

    # Query the model to get widths where the status is "In-stock"
    widths = model_class.objects.filter(status=status).values_list('width', flat=True).distinct()

    return list(widths)


def get_widths_view(request):
    """
    A Django view function that handles GET requests to fetch widths from a specific anbar location
    where the status is "In-stock". The anbar location is specified as a query parameter.

    Expected Query Parameters:
    - anbar_location: The name of the anbar location (e.g., 'Anbar_Akhal').

    Returns:
    - A JSON response containing a list of distinct widths from the specified anbar location
      where the status is "In-stock".
    """
    try:
        # Extract the anbar_location from the query parameters
        anbar_location = request.GET.get('anbar_location')
        if not anbar_location:
            return JsonResponse({'error': 'Anbar location is required'}, status=400)

        # Fetch widths from the specified anbar location where the status is "In-stock"
        widths = get_widths_from_anbar_location(anbar_location, 'In-stock')
        # Return the widths as a JSON response
        return JsonResponse({'widths': widths}, status=200)
    except Exception as e:
        # Handle any exceptions that occur during the process
        return JsonResponse({'error': str(e)}, status=500)


def get_reel_numbers_by_width_and_status(request):
    try:
        # Extract the anbar_location from the query parameters
        anbar_location = request.GET.get('anbar_location')
        width = request.GET.get('width')
        if not anbar_location:
            return JsonResponse({'error': 'Anbar location is required'}, status=400)

        # Dynamically import the model class
        model_class = apps.get_model('myapp', anbar_location)

        # Query the model to get reel numbers where the width matches the specified width,
        # the status is "In-stock", and sort the results by receive_date (old to new)
        reel_numbers = model_class.objects.filter(width=width, status='In-stock').order_by('receive_date').values_list('reel_number', flat=True)

        # Return the widths as a JSON response
        return JsonResponse({'reel_numbers': list(reel_numbers)}, status=200)
    except Exception as e:
        # Handle any exceptions that occur during the process
        return JsonResponse({'error': str(e)}, status=500)

@csrf_exempt
def loaded(request):
    """
    Handles the loading of a shipment by updating the Shipments and AnbarGeneric models.

    This view processes a POST request containing shipment details, including the license number,
    loading location, width, and selected reel numbers. It updates the status of the shipment to
    'LoadedUnloaded', sets its location to 'Weight2', and updates the status of the selected
    reel numbers to 'Sold'. It also stores the list of reel numbers in the shipment's
    'list_of_reels' field.

    The view returns a JSON response indicating the success or failure of the operation, including a
    message detailing the outcome.

    Parameters:
    - request (HttpRequest): The HTTP request object containing the POST data.

    Returns:
    - JsonResponse: A JSON response indicating the success or failure of the operation, along with
                    a message detailing the outcome.

    Raises:
    - Http404: If the shipment with the provided license number does not exist.
    - HttpResponse: If an exception occurs during the operation, with a status code indicating the
                    type of error.

    Example POST data:
    {
        "license_number": "12345",
        "loading_location": "Weight2",
        "width": 25,
        "reel_numbers": ["RN123", "RN456"]
    }
    """
    if request.method == 'POST':
        # Assuming the request data is in JSON format
        license_number = request.GET.get('lic_number')
        loading_location = request.GET.get('loading_location')
        width = request.GET.get('width')
        reel_numbers = json.loads(request.GET.get('reel_numbers'))
        forklift_driver = request.GET.get('forklift_driver')
        # Initialize an empty list to collect error messages
        errors = []
        if not license_number:
            errors.append({'status': 'error', 'message': 'پلاک را انتخاب کنید'})
        if not loading_location:
            errors.append({'status':'error', 'message': 'محل بارگیری را انتخاب کنید'})
        if not width:
            errors.append({'status':'error', 'message': 'عزض را انتخاب کنید'})
        if not reel_numbers:
            errors.append({'status':'error', 'message': 'شماره رول مورد نیاز است'})
        if not forklift_driver:
            errors.append({'status': 'error', 'message': 'اسم راننده فورک لیفت را وارد کنید'})
        # If there are any errors, return them in the response
        if errors:
            return JsonResponse({'status': 'error', 'errors': errors})
        else:
            try:
                shipment = Shipments.objects.filter(license_number=license_number, status='LoadingUnloading',location='Weight1', shipment_type='Outgoing')
                material_name = shipment[0].material_name
                supplier_name = shipment[0].supplier_name

                # Dynamically import the model class
                AnbarModel = apps.get_model('myapp', loading_location)
                for reel_number in reel_numbers:
                    AnbarModel.objects.filter(reel_number=reel_number, width=width,).update(
                        status='Sold',
                        location=license_number,
                        supplier_name=supplier_name,
                        material_name=material_name,
                        receive_date=str(datetime.now()),
                        last_date=str(datetime.now()),
                    )
                    product = Products.objects.filter(reel_number=reel_number, width=width,)
                    product.update(
                        status='Sold',
                        location=license_number,
                        receive_date=str(datetime.now()),
                        last_date=str(datetime.now()),
                    )
                profile_name = product[0].profile_name
                print(profile_name)
                shipment.update(
                    profile_name=profile_name,
                    unload_location=loading_location,
                    list_of_reels=','.join(reel_numbers),
                    location='Weight2',
                    status='LoadedUnloaded',
                    logs=f'{forklift_driver} Loaded NOW at time ({str(datetime.now())})',
                )

                # Return a success response
                return JsonResponse({'status': 'success',
                                     'message': f'Width and List of Reels has been added to {license_number}.'})
            except Shipments.DoesNotExist:
                return JsonResponse({'status': 'error', 'message': 'Shipments not found.'}, status=404)

    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method.'}, status=400)

def get_supplierNames_based_andbar(request):
    if request.method == 'GET':
        anbar_location = request.GET.get('anbar_location')
        try:
            anbar_model = apps.get_model('myapp', anbar_location)
            supplier_name = anbar_model.objects.values_list('supplier_name', flat=True)
            material_name = anbar_model.objects.values_list('material_name', flat=True)
            unit = anbar_model.objects.values_list('unit', flat=True)
            supplier_names = list(supplier_name)
            material_names = list(material_name)
            units = list(unit)
            # Return the widths as a JSON response
            return JsonResponse({'supplier_names': supplier_names, 'material_names': material_names, 'units':units}, status=200)
        except Exception as e:
            # Handle any exceptions that occur during the process
            return JsonResponse({'error': str(e)}, status=500)

def get_unit_based_supplier_name(request):
    if request.method == 'GET':
        supplier_name = request.GET.get('supplier_name')
        try:
            # Get all unit names for the specified supplier
            unit_names = Unit.objects.filter(supplier_name=supplier_name).values_list('unit_name', flat=True)
            unit_names = list(unit_names)
            print(unit_names)
            # Return the widths as a JSON response
            return JsonResponse({'unit_names': unit_names}, status=200)
        except Exception as e:
            # Handle any exceptions that occur during the process
            return JsonResponse({'error': str(e)}, status=500)


@csrf_exempt
def used(request):
    """
    Handles the marking of materials as used by updating the Consumption and AnbarGeneric models.

    This view processes a POST request containing consumption details, including the unloading location,
    supplier name, material name, unit, quantity, and forklift driver. It creates new entries in the
    Consumption model for each unit consumed, setting their received date to the current time, status to
    'Used', and comments to the forklift driver's name. It also updates the status, location, last date,
    and comments of the corresponding AnbarGeneric items to reflect their consumption.

    The view returns a JSON response indicating the success or failure of the operation, including a
    message detailing the outcome.

    Parameters:
    - request (HttpRequest): The HTTP request object containing the POST data.

    Returns:
    - JsonResponse: A JSON response indicating the success or failure of the operation, along with
                    a message detailing the outcome.

    Raises:
    - HttpResponse: If an exception occurs during the operation, with a status code indicating the
                    type of error.

    Example POST data:
    {
        "unloading_location": "Weight2",
        "supplier_name": "Supplier A",
        "material_name": "Material X",
        "unit": "Unit 1",
        "quantity": 2,
        "forklift_driver": "Driver John"
    }
    """

    if request.method == 'POST':
        # Assuming the request data is in JSON format

        unloading_location = request.GET.get('unloading_location')
        supplier_name = request.GET.get('supplier_name')
        material_name = request.GET.get('material_name')
        unit = request.GET.get('unit')
        quantity = request.GET.get('quantity')
        forklift_driver = request.GET.get('forklift_driver')
        try:
            # Calculate the quantity to be unloaded
            quantity_to_unload = int(quantity)
            # Dynamically get the model based on the anbar_name
            AnbarModel = apps.get_model('myapp', unloading_location)

            # Create Consumption records
            for _ in range(quantity_to_unload):
                consumption = Consumption(
                    receive_date=str(datetime.now()),
                    supplier_name=supplier_name,
                    material_name=material_name,
                    unit=unit,
                    status='Used',
                    logs=f'{forklift_driver} Used NOW at ({str(datetime.now())}),'
                )
                consumption.save()
                # Insert data into the specific Anbar table
                anbar_items = AnbarModel.objects.filter(
                    supplier_name=supplier_name,
                    material_name=material_name,
                    unit=unit,
                ).update(
                    status='Used',
                    location='Consumption DB',
                    logs=f'{forklift_driver} Used NOW at ({str(datetime.now())}),',
                    receive_date = str(datetime.now()),
                    last_date=str(datetime.now()),
                )

            # Return a success response
            #  'message': f'{data["quantity"]} units of {data["material_name"]} have been marked as used.'
            return JsonResponse({'status': 'success',})

        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method.'}, status=400)

def load_data_for_moved(request):
    try:
        # Extract the anbar_location from the query parameters
        anbar_location = request.GET.get('anbar_location')
        if not anbar_location:
            return JsonResponse({'error': 'Anbar location is required'}, status=400)

        # Dynamically import the model class
        model_class = apps.get_model('myapp', anbar_location)

        # Query the model to get reel numbers where the width matches the specified width,
        # the status is "In-stock", and sort the results by receive_date (old to new)
        anbar = model_class.objects.filter(status='In-stock')
        print(anbar)
        data = {
            "supplier_name": anbar.supplier_name,
            "material_name": anbar.material_name,
            "unit": anbar.unit,

            "width": anbar.width,
            "reel_number": anbar.reel_number,
        }

        # Return the widths as a JSON response
        return JsonResponse(data=data, status=200)
    except Exception as e:
        print(e)
        # Handle any exceptions that occur during the process
        return JsonResponse({'error': str(e)}, status=500)


@csrf_exempt
def moved(request):
    """
    Handles the movement of materials within the warehouse by updating the AnbarGeneric models.

    This view processes a POST request containing movement details, including the source and destination
    locations, the type of material (raw or reel), and the specific details of the material (supplier name,
    material name, unit, quantity, width, reel numbers, and forklift driver). It updates the status,
    location, and last date of the source AnbarGeneric items to reflect their movement and creates new
    entries in the destination AnbarGeneric location for the moved materials.

    The view returns a JSON response indicating the success or failure of the operation, including a
    message detailing the outcome.

    Parameters:
    - request (HttpRequest): The HTTP request object containing the POST data.

    Returns:
    - JsonResponse: A JSON response indicating the success or failure of the operation, along with
                    a message detailing the outcome.

    Raises:
    - HttpResponse: If an exception occurs during the operation, with a status code indicating the
                    type of error.

    Example POST data:
    {
        "from_anbar": "Weight1",
        "to_anbar": "Weight2",
        "material_type": "Raw",
        "supplier_name": "Supplier A",
        "material_name": "Material X",
        "unit": "Unit 1",
        "quantity": 2,
        "forklift_driver": "Driver John"
    }
    """
    if request.method == 'POST':
        # Assuming the request data is in JSON format
        data = request.json()
        from_anbar = request.GET.get('from_anbar')
        real = request.GET.get('real')
        supplier_name = request.GET.get('supplier_name')
        material_name = request.GET.get('material_name')
        unit = request.GET.get('unit')
        Quantity = request.GET.get('Quantity')
        width = request.GET.get('width')
        to_anbar = request.GET.get('to_anbar')
        forklift_driver = request.GET.get('forklift_driver')
        real_or_raw = request.GET.get('real_or_raw')

        try:
            AnbarModel1 = apps.get_model('myapp', from_anbar)
            AnbarModel2 = apps.get_model('myapp', to_anbar)
            # Update source AnbarGeneric items
            if real_or_raw == 'Raw':
                source_items = AnbarModel1.objects.filter(
                    location=from_anbar,
                    supplier_name=supplier_name,
                    material_name=material_name,
                    logs=f'{forklift_driver} Moved NOW at time ({str(datetime.now())})'
                )
                for item in source_items:
                    item.status = 'Moved'
                    item.location = to_anbar
                    item.last_date = str(datetime.now())
                    item.save()
            if real_or_raw == 'Reel':
                # Update source AnbarGeneric items
                source_items2 = Products.objects.filter(
                    location=from_anbar,
                    supplier_name=supplier_name,
                    material_name=material_name,
                    logs=f'{forklift_driver} Moved NOW at time ({str(datetime.now())})'
                )
                for item in source_items2:
                    item.status = 'Moved'
                    item.location = to_anbar
                    item.last_date = str(datetime.now())
                    item.save()

            # Create new entries in the destination AnbarGeneric location
            for _ in range(int(Quantity)):
                new_item = AnbarModel2(
                    receive_date=str(datetime.now()),
                    location=to_anbar,
                    status='In-stock',
                    supplier_name=supplier_name,
                    material_name=material_name,
                    width=width,
                    unit=unit,
                    reel_number=real
                )
                new_item.save()

            # Return a success response
            return JsonResponse({'status': 'success', 'message': f'{data["quantity"]} units of {data["material_name"]} have been moved from {data["from_anbar"]} to {data["to_anbar"]}.'})

        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method.'}, status=400)


@csrf_exempt
def retuned(request):
    """
    Handles the POST request to process returned materials.

    This view function validates the input data, checks if all required fields are provided,
    and returns an appropriate response. It adheres to best practices and the DRY principle.

    Parameters:
    - request: The HTTP request object.

    Returns:
    - A JSON response with the result of the operation.
    """
    if request.method == 'POST':
        # Extract data from the request
        supplier_name = request.GET.get('supplier_name')
        material_type = request.GET.get('material_type')
        unit_name = request.GET.get('unit_name')
        quantity = request.GET.get('quantity')
        anbar_location = request.GET.get('anbar_location')
        reason = request.GET.get('reason')
        forklift_driver = request.GET.get('forklift_driver')

        errors = []

        # Check if all required fields are provided
        if not supplier_name:
            errors.append({'status': 'error', 'message': 'supplier name is required.'})
        if not material_type:
            errors.append({'status': 'error', 'message': 'material type is required.'})
        if not unit_name:
            errors.append({'status': 'error', 'message': 'unit_name is required.'})
        if not quantity:
            errors.append({'status': 'error', 'message': 'quantity is required.'})
        if not anbar_location:
            errors.append({'status': 'error', 'message': 'anbar location is required.'})
        if not reason:
            errors.append({'status': 'error', 'message': 'reason is required.'})
        if not forklift_driver:
            errors.append({'status': 'error', 'message': 'forklift_driver is required.'})

        # If there are any errors, return them in the response
        if errors:
            return JsonResponse({'status': 'error', 'errors': errors})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})


# Admin panel
from django.contrib import admin

@csrf_exempt
def add_new_anbar(request):
    """
    Handles the creation of a new anbar based on the provided location name and username.
    Expects a POST request with 'location_name' and 'username' in the request body.

    Returns a JSON response indicating success or failure, along with relevant messages.
    """
    if request.method == 'POST':
        # Extract data from the request
        location = request.GET.get('location')
        username = request.GET.get('username')
        errors = []
        if not location:
            errors.append({'status': 'error', 'message': 'اسم مکان انبار را وارد کنید'})
        if not username:
            errors.append({'status': 'error', 'message': 'نام کابری را وارد کنید.'})
        location = 'Anbar_'+location
        try:
            # Define a new model class that inherits from AnbarGeneric
            attrs = {
                '__module__': 'myapp.models',  # Replace 'your_app_name' with your actual app name
                'Meta': type('Meta', (), {
                    'db_table': location,
                }),
            }
            # Create a new model class
            new_model = ModelBase(location, (AnbarGeneric,), attrs)
            # Register the new model with Django's app registry
            # apps.get_app_config('myapp').models.add(new_model)
            app_config = apps.get_app_config('myapp')
            app_config.models[location] = new_model

            # Create the table in the database
            with connection.schema_editor() as schema_editor:
                schema_editor.create_model(new_model)

            @admin.register(new_model)
            class AnbarAdmin(admin.ModelAdmin):
                # Specify the fields to display in the list view
                list_display = ('material_name', 'reel_number', 'status', 'location', 'last_date')
                # Specify the fields to use in the search box
                search_fields = ('material_name', 'reel_number')
                # Specify the fields to use in the filter sidebar
                list_filter = ('status', 'location')
                # Specify the fields to display in the detail view
                fields = (
                'material_name', 'reel_number', 'status', 'location', 'last_date', 'width', 'gsm', 'length', 'grade',
                'breaks', 'comments', 'qr_code', 'profile_name', 'username', 'logs')

            # Return success response
            return JsonResponse({'status': 'success', 'message': f'Anbar {location} has been added.'})

        except ValidationError as e:
            # Handle validation errors
            errors.append({'status': 'error', 'message': f'An unexpected error occurred.{e}'})
            return JsonResponse({'status': 'error', 'errors': errors})

        except Exception as e:
            # Handle unexpected errors
            errors.append({'status': 'error', 'message': f'An unexpected error occurred.{e}'})
            return JsonResponse({'status': 'error', 'errors': errors})
    else:
        return render(request, 'add_new_anbar.html')


@csrf_exempt
def add_material_type(request):
    """
    Handles the POST request to add a new material type.

    This view function processes the form data, validates it, and saves a new MaterialType instance to the database.
    It handles potential errors gracefully and provides informative feedback to the user.

    Parameters:
    - request: The HTTP request object.

    Returns:
    - A JSON response with the result of the operation.
    """
    if request.method == 'POST':
        try:
            # Extract data from the request
            supplier_name = request.GET.get('supplier_name')
            material_type = request.GET.get('material_type')
            username = request.GET.get('username')

            # Initialize an empty list to collect error messages
            errors = []

            # Check if all required fields are provided
            if not supplier_name:
                errors.append({'status': 'error', 'message': 'اسم تامین کننده را انتخاب کنید.'})
            if not material_type:
                errors.append({'status': 'error', 'message': 'نوع ماده را وارد کنید'})
            if not username:
                errors.append({'status': 'error', 'message': 'نام کاربری را وارد کنید.'})

            # If there are any errors, return them in the response
            if errors:
                return JsonResponse({'status': 'error', 'errors': errors})

            # Create a new MaterialType instance
            new_material_type = MaterialType(
                supplier_name=supplier_name,
                material_type=material_type,
                username=username,
                status='Active',
                logs=f'{username} Created NOW at time ({datetime.now()}),'
            )
            # Save the new Customer object to the database
            try:
                new_material_type.save()
                # Return success response
                return JsonResponse({'status': 'success', 'message': 'Material type has been added.'})
            except Exception as e:
                # Handle any exceptions that occur during the save operation
                errors.append({'status': 'error', 'message': f'Error adding Material type: {str(e)}'})
                return JsonResponse({'status': 'error', 'errors': errors})

        except Exception as e:
            # Handle other exceptions
            return JsonResponse({'status': 'fail', 'message': 'An error occurred: ' + str(e)})

    else:
        # Handle non-POST requests
        return render(request, 'add_material_type.html')


@csrf_exempt
def add_unit(request):
    """
    Handles the POST request to add a new unit.

    This view function processes the form data, validates it, and saves a new Unit instance to the database.
    It handles potential errors gracefully and provides informative feedback to the user.

    Parameters:
    - request: The HTTP request object.

    Returns:
    - A JSON response with the result of the operation.
    """
    if request.method == 'POST':
        # Extract data from the request
        supplier_name = request.GET.get('supplier_name')
        material_type = request.GET.get('material_type')
        unit_name = request.GET.get('unit_name')
        count = request.GET.get('count')
        username = request.GET.get('username')

        errors = []

        # Check if all required fields are provided
        if not supplier_name:
            errors.append({'status': 'error', 'message': 'supplier name is required.'})
        if not material_type:
            errors.append({'status': 'error', 'message': 'material type is required.'})
        if not unit_name:
            errors.append({'status': 'error', 'message': 'unit_name is required.'})
        if not count:
            errors.append({'status': 'error', 'message': 'count are required.'})
        if not username:
            errors.append({'status': 'error', 'message': 'username are required.'})
        # Load existing customer names from DB Check for duplicate name
        if Unit.objects.filter(unit_name=unit_name).exists():
            error_message = f"در حال حاضر یک واحد با نام {unit_name} در سیستم وجود دارد."
            errors.append({'status': 'error', 'message': error_message})

        # If there are any errors, return them in the response
        if errors:
            return JsonResponse({'status': 'error', 'errors': errors})
        else:
            # Create a new Unit instance
            new_unit = Unit(
                supplier_name=supplier_name,
                material_type=material_type,
                unit_name=unit_name,
                count=count,
                username=username,
                date=str(datetime.now()),
                status='Active',
                logs=f'{username} Created NOW at time ({str(datetime.now())}),'
            )

            # Save the new Customer object to the database
            try:
                new_unit.save()
                # Return success response
                return JsonResponse({'status': 'success', 'message': 'Unit has been added.'})
            except Exception as e:
                print(e)
                # Handle any exceptions that occur during the save operation
                errors.append({'status': 'error', 'message': f'Error adding Unit: {str(e)}'})
                return JsonResponse({'status': 'error', 'errors': errors})
    else:
        # Handle non-POST requests
        return render(request, 'add_unit.html')

def get_unit_based_on_material_type(request):
    if request.method == 'GET':
        pass


@csrf_exempt
def add_consumption_profile(request):
    """
    Handles the POST request to add a new consumption profile.

    This view function processes the form data, validates it, and saves a new Consumption instance to the database.
    It handles potential errors gracefully and provides informative feedback to the user.

    Parameters:
    - request: The HTTP request object.

    Returns:
    - A JSON response with the result of the operation.
    """
    if request.method == 'POST':
        # Extract data from the request
        supplier_name = request.GET.get('supplier_name')
        material_name = request.GET.get('material_name')
        unit = request.GET.get('unit')
        quantity = request.GET.get('quantity')
        profile_name = request.GET.get('profile_name')
        username = request.GET.get('username')
        consumption_list = request.GET.get('consumption_list')
        consumption_list = json.loads(consumption_list)

        # Initialize an empty list to collect error messages
        errors = []

        # Check if all required fields are provided
        if not supplier_name:
            errors.append({'status': 'error', 'message': 'supplier name is required.'})
        if not material_name:
            errors.append({'status': 'error', 'message': 'material name is required.'})
        if not unit:
            errors.append({'status': 'error', 'message': 'unit is required.'})
        if not quantity:
            errors.append({'status': 'error', 'message': 'quantity is required.'})
        if not profile_name:
            errors.append({'status': 'error', 'message': 'profile name is required.'})
        if not username:
            errors.append({'status': 'error', 'message': 'username is required.'})

        # If there are any errors, return them in the response
        if errors:
            return JsonResponse({'status': 'error', 'errors': errors})

        for profile in consumption_list:
            supplier_name = profile['supplier_name']
            material_name = profile['material_name']
            unit = profile['unit']
            quantity = profile['quantity']
            for num in range(int(quantity)):
                # Create a new Consumption instance
                new_consumption = Consumption(
                    supplier_name=supplier_name,
                    material_name=material_name,
                    unit=unit,
                    profile_name=profile_name,
                    username=username,
                    status="Active",
                    logs=f'{username} Created NOW at time ({datetime.now()}),'
                )
                new_consumption.save()

        # Save the new Customer object to the database
        try:
            # new_consumption.save()
            # Return success response
            return JsonResponse({'status': 'success', 'message': 'Consumption profile has been added.'})
        except Exception as e:
                # Handle any exceptions that occur during the save operation
                return JsonResponse({'status': 'error', 'message': f'Error adding consumption: {str(e)}'})
    else:
        # Handle non-POST requests
        return render(request, 'add_consumption_profile.html')


@csrf_exempt
def cancel_shipment(request):
    """
    Handles the POST request to cancel a shipment.

    This view function processes the cancellation request, updates related entities,
    and manages statuses across different models. It handles potential errors gracefully
    and provides informative feedback to the user.

    Parameters:
    - request: The HTTP request object.

    Returns:
    - A JSON response with the result of the operation.
    """
    if request.method == 'POST':
        try:
            # Extract data from the request
            shipment_id = request.GET.get('shipment_id')
            cancellation_reason = request.GET.get('cancellation_reason')

            # Validate the data
            if not shipment_id or not cancellation_reason:
                raise ValidationError("Shipments ID and cancellation reason are required.")

            # Fetch the shipment
            shipment = Shipments.objects.get(shipment_id=shipment_id)

            # Update shipment status and cancellation reason
            shipment.status = 'Canceled'
            shipment.cancellation_reason = cancellation_reason
            shipment.save()

            # Update related entities (e.g., Truck, Products, AnbarGeneric, Purchases, Sale)
            # Assuming the shipment is associated with a truck
            truck = Truck.objects.get(truck_id=shipment.truck_id)
            truck.status = 'Free'
            truck.location = 'Entrance'
            truck.save()
            # Assuming the shipment has a list of reels (product IDs)
            reels = shipment.list_of_reels.split(',')
            for reel in reels:
                product = Products.objects.get(reel_number=reel)
                product.status = 'In-stock'
                product.location = 'Canceled'
                product.save()
            # Assuming AnbarGeneric subclasses are Anbar_Sangin, Anbar_Salon_Tolid, etc.
            # You would need to repeat the update logic for each subclass
            # For example, updating Anbar_Sangin:
            anbar_sangin_reels = Anbar_Sangin.objects.filter(reel_number__in=reels)
            for item in anbar_sangin_reels:
                item.status = 'In-stock'
                item.location = 'Canceled'
                item.save()
            purchases = Purchases.objects.filter(ShipmentID=shipment)
            for purchase in purchases:
                purchase.Status = 'Cancelled'
                purchase.CancellationReason = cancellation_reason
                purchase.save()
            sales = Sales.objects.filter(shipment=shipment)
            for sale in sales:
                sale.payment_status = 'Cancelled'
                sale.comments = cancellation_reason
                sale.save()

            # This is a simplified example; actual implementation will depend on the specific logic required
            # For example, updating the status of related products to 'In-stock' and their location to 'Canceled'

            # Return success response
            return JsonResponse({'status': 'success', 'message': f'Shipments {shipment_id} has been canceled.'})

        except Shipments.DoesNotExist:
            # Handle case where the shipment does not exist
            return JsonResponse({'status': 'fail', 'message': 'Shipments not found.'})

        except ValidationError as e:
            # Handle validation errors
            return JsonResponse({'status': 'fail', 'message': str(e)})

        except Exception as e:
            # Handle other exceptions
            return JsonResponse({'status': 'fail', 'message': 'An error occurred: ' + str(e)})

    else:
        # Handle non-POST requests
        return JsonResponse({'status': 'fail', 'message': 'Invalid request method.'})


