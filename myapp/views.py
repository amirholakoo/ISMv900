import json

from django.shortcuts import render, redirect
from .models import *
from django.http import JsonResponse
from django.core.exceptions import ValidationError
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
import uuid

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
        # Extract data from the request
        license_number = request.GET.get('license_number')
        driver_name = request.GET.get('driver_name')
        driver_doc = request.GET.get('driver_doc')
        phone = request.GET.get('phone')
        username = request.GET.get('username')
        print(license_number, driver_name)
        print(type(license_number))
        # Create new truck
        # new_truck = Truck(
        #     license_number=license_number,
        #     driver_name=driver_name,
        #     driver_doc=driver_doc,
        #     phone=phone,
        # )
        # new_truck.save()
        #
        # # Return success response
        return JsonResponse({
            'success': 'Truck added successfully.',
            # 'license_number': new_truck.license_number,
        }, status=201)
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
            # Query the MaterialType model for all instances
            material_types = MaterialType.objects.all()
            # Extract and return the names in a JSON response
            material_names = [material_type.material_type for material_type in material_types]
            return JsonResponse({'status': 'success', 'material_names': material_names})
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

            # Load the last reel number from the Products DB
            last_reel_number = Products.objects.latest('reel_number').reel_number
            next_reel_number = f"{last_reel_number[:-1]}{int(last_reel_number[-1]) +   1}"

            # Create a new Products record
            new_product = Products(
                reel_number=next_reel_number,
                width=width,
                gsm=gsm,
                length=length,
                breaks=breaks,
                grade=grade,
                profile_name=consumption_profile_name,
            )
            new_product.save()

            # Create a new Anbar_Salon_Tolid record
            new_anbar_record = Anbar_Salon_Tolid(
                reel_number=next_reel_number,
                width=width,
                gsm=gsm,
                length=length,
                breaks=breaks,
                grade=grade,
                profile_name=consumption_profile_name,
            )
            new_anbar_record.save()

            # Update the Consumption DB based on the selected consumption profile
            # Note: Add your own logic to update the Consumption model here

            # Return a success response
            return JsonResponse({'message': 'Reel number has been added', 'reel_number': next_reel_number}, status=200)

        except ValidationError as e:
            # Return a validation error response
            return JsonResponse({'error': str(e)}, status=400)

        except Exception as e:
            # Return a general error response
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)


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

            # Return the license numbers as a JSON response
            return JsonResponse({'license_numbers': license_numbers}, status=200)

        except Exception as e:
            # Return a general error response
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)


def get_material_names(request):
    """
    Handles GET requests to retrieve all material names from the RawMaterial model.

    This function queries the RawMaterial model for all records and returns the
    material names in a JSON response. If an error occurs during the process,
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
            materials = RawMaterial.objects.all()

            # Extract the material names from the queryset
            material_names = [material.material_name for material in materials]

            # Return the material names in a JSON response
            return JsonResponse({'material_names': material_names}, status=200)

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

        # Check required fields
        errors = []
        if not license_number:
            errors.append('License number is required.')
        if not supplier_name:
            errors.append('supplier name is required.')
        if not material_type:
            errors.append('material type is required.')
        if not material_name:
            errors.append('material name is required.')
        if not shipment_type:
            errors.append('shipment type is required.')
        if not customer_name:
            errors.append('customer name is required.')

        if errors:
            return JsonResponse({'status': 'error', 'errors': errors})
        else:
            # Process data and create shipment
            truck = Truck.objects.filter(license_number=license_number, status='Free').first()
            if not truck:
                return JsonResponse({'status': 'error', 'message': 'No free truck with that license number.'})
            else:
                truck.save()

            shipment = Shipment()
            shipment.entry_time = timezone.now()
            shipment.license_number = license_number
            shipment.shipment_type = shipment_type

            # Handle incoming/outgoing shipment logic
            if shipment_type == 'Incoming':
                shipment.supplier = Supplier.objects.get(supplier_name=supplier_name)
                shipment.material_type = MaterialType.objects.get(material_type=material_type)
                shipment.material_name = MaterialType.objects.get(material_name=material_name)
                # Update material quantity if applicable
                # ...

            elif shipment_type == 'Outgoing':
                shipment.customer = Customer.objects.get(customer_name=customer_name)
                # Update customer inventory if applicable
                # ...

            shipment.save()

            # truck.status = 'Busy'
            # truck.location = 'Entrance'
            # truck.save()

            return JsonResponse({'status': 'success', 'message': 'Shipment created successfully!'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})



# Weight Station/Create Orders


@csrf_exempt
def update_weight1(request):
    """
    Handles a POST request to update the weight1 field of a Shipment instance.

    This view function expects the following data in the POST request:
    - shipment_id: The UUID of the Shipment instance to update.
    - weight1: The new weight1 value to set, as a string that can be converted to a float.
    - username: The username of the user making the request, used for comments.

    It performs the following operations:
    - Validates that the weight1 value is within the range of 9 to 38000 KG.
    - Retrieves the Shipment instance by its shipment_id.
    - Updates the weight1, weight1_time, and comments fields of the Shipment instance.
    - Saves the changes to the database.
    - Returns a JSON response indicating success or failure, along with a message.

    Parameters:
    - request: The Django HttpRequest object.

    Returns:
    - A JsonResponse object with a success flag and a message.
    """
    if request.method == 'POST':
        # Assuming shipment_id and weight1 are sent in the POST data
        shipment_id = request.GET.get('shipment_id')
        weight1 = request.GET.get('weight1')
        username = request.GET.get('username')

        try:
            # Convert weight1 to a decimal and validate the range
            weight1 = float(weight1)
            if weight1 < 9 or weight1 > 38000:
                return JsonResponse({'success': False, 'message': 'Weight must be between 9 and 38000 KG.'})

            # Retrieve the shipment instance
            shipment = Shipment.objects.get(shipment_id=shipment_id)

            # Update the fields
            shipment.weight1 = weight1
            shipment.weight1_time = timezone.now()
            shipment.comments = f"{username} Weight1"

            # Save the changes
            shipment.save()

            # Return a success response
            return JsonResponse({'success': True, 'message': f'You entered WEIGHT 1 KG for Shipment for SUPPLIER/CUSTOMER with LICENSE NUMBER: {shipment.license_number} has been added.'})

        except Shipment.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Shipment not found.'})
        except ValueError:
            return JsonResponse({'success': False, 'message': 'Invalid weight format.'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})

    return JsonResponse({'success': False, 'message': 'Invalid request method.'})


def update_weight2(request):
    """
    Handles a POST request to update the weight2 and net_weight of a Shipment instance.

    This function retrieves a Shipment instance based on the provided license number, validates the weight2 and net_weight values,
    updates the instance with the new weights, and saves the changes to the database. It returns a JSON response indicating
    the success or failure of the operation, along with appropriate messages.
    """
    if request.method == 'POST':
        # Extract data from the request
        license_number = request.POST.get('license_number')
        weight2 = request.POST.get('weight2')
        net_weight = request.POST.get('net_weight')

        # Validate input
        if not license_number or not weight2 or not net_weight:
            return JsonResponse({'status': 'error', 'message': 'All fields are required.'})

        try:
            weight2 = float(weight2)
            net_weight = float(net_weight)
        except ValueError:
            return JsonResponse({'status': 'error', 'message': 'Weight2 and Net Weight must be numbers.'})

        if not (9 <= weight2 <= 38000) or not (9 <= net_weight <= 38000):
            return JsonResponse({'status': 'error', 'message': 'Weight2 and Net Weight must be between 9 KG and 38000 KG.'})

        # Update the Shipment instance
        try:
            shipment = Shipment.objects.get(license_number=license_number)
            shipment.weight2 = weight2
            shipment.weight2_time = timezone.now()
            shipment.net_weight = net_weight
            shipment.save()

            # Check if the absolute difference between weight1 and weight2 equals net_weight
            if abs(shipment.weight1 - weight2) != net_weight:
                return JsonResponse({'status': 'error', 'message': 'The absolute difference between Weight1 and Weight2 must equal the Net Weight.'})

            return JsonResponse({'status': 'success', 'message': f'Weight2 and Net Weight for Shipment with License Number {license_number} has been updated successfully.'})
        except Shipment.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': f'Shipment with License Number {license_number} does not exist.'})

    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})


@csrf_exempt
def create_purchase_order(request):
    """
    Handles the creation of a Purchase Order based on the provided algorithm.
    """
    if request.method == 'POST':
        try:
            # Assuming the request data is in JSON format
            data = request.json()

            # Load shipment data
            shipment = Shipment.objects.get(license_number=data['license_number'], status='Office')

            # Update shipment status and location
            shipment.status = 'Delivered'
            shipment.location = 'Delivered'
            shipment.exit_time = timezone.now()
            shipment.save()

            # Insert new purchase order data
            # Assuming PurchaseOrder is another model not shown here
            # purchase_order = PurchaseOrder(**data)
            # purchase_order.save()

            # Update truck status and location
            # Assuming Truck is another model not shown here
            # truck = Truck.objects.get(id=shipment.truck_id)
            # truck.status = 'Free'
            # truck.location = 'Entrance'
            # truck.save()

            # Return success response
            return JsonResponse({'success': True, 'message': 'Purchase Order created successfully.'})

        except Shipment.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Shipment not found or not in Office status.'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})

    else:
        return JsonResponse({'success': False, 'message': 'Invalid request method.'})


@csrf_exempt
def create_sales_order(request):
    """
    Function to create a Sales Order and update related entities based on the provided algorithm.
    """
    if request.method == 'POST':
        # Assuming the request data is in JSON format
        data = request.json()

        try:
            # Retrieve the shipment instance
            shipment = Shipment.objects.get(shipment_id=data['shipment_id'])

            # Update shipment fields
            shipment.status = 'Delivered'
            shipment.location = 'Delivered'
            shipment.exit_time = timezone.now()

            # Calculate total price
            total_price = shipment.net_weight * shipment.price_per_kg * (shipment.vat / 100)

            # Update other fields as necessary
            # This is a simplified example, you might need to adjust based on your actual requirements

            # Save the updated shipment
            shipment.save()

            # Perform other updates as per the algorithm
            # This might involve updating other models like Products, Anbar_, Trucks, etc.
            # This is a simplified example, you might need to adjust based on your actual requirements

            # Return a success response
            return JsonResponse({'status': 'success', 'message': 'Sales Order created successfully.'})

        except Shipment.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Shipment not found.'}, status=404)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method.'}, status=400)

# Forklift Panel

@csrf_exempt
def unload(request):
    """
    Handles the unloading of a shipment by updating the Shipment and AnbarGeneric models.

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
        # Assuming the request data is in JSON format
        data = request.json()

        try:
            # Retrieve the shipment instance
            shipment = Shipment.objects.get(license_number=data['license_number'])

            # Update shipment fields
            shipment.status = 'LoadedUnloaded'
            shipment.location = 'Weight2'
            shipment.save()

            # Calculate the quantity to be unloaded
            quantity_to_unload = data['quantity']

            # Assuming Anbar_Akhal is used for unloading location
            # Update AnbarGeneric (Anbar_Akhal in this case)
            for _ in range(quantity_to_unload):
                anbar_item = Anbar_Akhal(
                    status='In-stock',
                    receive_date=timezone.now(),
                    # Add other necessary fields as per your model
                )
                anbar_item.save()

            # Return a success response
            return JsonResponse({'status': 'success', 'message': f'{quantity_to_unload} units have been added to {data["license_number"]}.'})

        except Shipment.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Shipment not found.'}, status=404)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method.'}, status=400)


@csrf_exempt
def loaded(request):
    """
    Handles the loading of a shipment by updating the Shipment and AnbarGeneric models.

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
        data = request.json()

        try:
            # Retrieve the shipment instance
            shipment = Shipment.objects.get(license_number=data['license_number'])

            # Update shipment fields
            shipment.status = 'LoadedUnloaded'
            shipment.location = 'Weight2'
            shipment.list_of_reels = ','.join(data['reel_numbers'])
            shipment.save()

            # Update AnbarGeneric (Anbar_Akhal in this example)
            for reel_number in data['reel_numbers']:
                anbar_item = Anbar_Akhal.objects.get(reel_number=reel_number)
                anbar_item.status = 'Sold'
                anbar_item.save()

            # Return a success response
            return JsonResponse({'status': 'success', 'message': f'Width and List of Reels has been added to {data["license_number"]}.'})

        except Shipment.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Shipment not found.'}, status=404)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method.'}, status=400)


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
        data = request.json()

        try:
            # Create Consumption records
            for _ in range(data['quantity']):
                consumption = Consumption(
                    receive_date=timezone.now(),
                    supplier_name=data['supplier_name'],
                    material_name=data['material_name'],
                    unit=data['unit'],
                    status='Used',
                    comments=data['forklift_driver']
                )
                consumption.save()

            # Update AnbarGeneric (Anbar_Akhal in this example)
            anbar_items = Anbar_Akhal.objects.filter(
                location=data['unloading_location'],
                supplier_name=data['supplier_name'],
                material_name=data['material_name']
            )
            for item in anbar_items:
                item.status = 'Used'
                item.location = 'Consumption DB'
                item.last_date = timezone.now()
                item.comments = data['forklift_driver']
                item.save()

            # Return a success response
            return JsonResponse({'status': 'success', 'message': f'{data["quantity"]} units of {data["material_name"]} have been marked as used.'})

        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method.'}, status=400)


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

        try:
            # Update source AnbarGeneric items
            source_items = Anbar_Akhal.objects.filter(
                location=data['from_anbar'],
                supplier_name=data['supplier_name'],
                material_name=data['material_name']
            )
            for item in source_items:
                item.status = 'Moved'
                item.location = data['to_anbar']
                item.last_date = timezone.now()
                item.save()

            # Create new entries in the destination AnbarGeneric location
            for _ in range(data['quantity']):
                new_item = Anbar_Akhal(
                    receive_date=timezone.now(),
                    location=data['to_anbar'],
                    status='In-stock',
                    supplier_name=data['supplier_name'],
                    material_name=data['material_name'],
                    # Add other necessary fields as per your model
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

@csrf_exempt
def add_new_anbar(request):
    """
    Handles the creation of a new anbar based on the provided location name and username.
    Expects a POST request with 'location_name' and 'username' in the request body.

    Returns a JSON response indicating success or failure, along with relevant messages.
    """
    if request.method == 'POST':
        try:
            # Extract data from the request
            location_name = request.GET.get('location_name')
            username = request.GET.get('username')

            # Check if the location already exists
            if AnbarGeneric.objects.filter(location=location_name).exists():
                return JsonResponse({'status': 'fail', 'message': 'Anbar location already exists.'})

            # Create a new anbar entry
            anbar = AnbarGeneric(location=location_name, comments=f'Username Created on {username} (CVS)')
            anbar.save()

            # Return success response
            return JsonResponse({'status': 'success', 'message': f'Anbar {location_name} has been added.'})

        except ValidationError as e:
            # Handle validation errors
            return JsonResponse({'status': 'fail', 'message': str(e)})
        except Exception as e:
            # Handle unexpected errors
            return JsonResponse({'status': 'fail', 'message': 'An unexpected error occurred.'})

    else:
        return JsonResponse({'status': 'fail', 'message': 'Invalid request method.'})


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
            supplier_name = request.POST.get('supplier_name')
            material_type = request.POST.get('material_type')
            username = request.POST.get('username')

            # Initialize an empty list to collect error messages
            errors = []

            # Check if all required fields are provided
            if not supplier_name:
                errors.append({'status': 'error', 'message': 'supplier name is required.'})
            if not material_type:
                errors.append({'status': 'error', 'message': 'material type is required.'})
            if not username:
                errors.append({'status': 'error', 'message': 'username is required.'})

            # If there are any errors, return them in the response
            if errors:
                return JsonResponse({'status': 'error', 'errors': errors})

            # Create a new MaterialType instance
            new_material_type = MaterialType(
                supplier_name=supplier_name,
                material_type=material_type,
                username=username
            )
            # Save the new Customer object to the database
            try:
                new_material_type.save()
                # Return success response
                return JsonResponse({'status': 'success', 'message': 'Material type has been added.'})
            except Exception as e:
                # Handle any exceptions that occur during the save operation
                return JsonResponse({'status': 'error', 'message': f'Error adding Material type: {str(e)}'})

        except Exception as e:
            # Handle other exceptions
            return JsonResponse({'status': 'fail', 'message': 'An error occurred: ' + str(e)})

    else:
        # Handle non-POST requests
        return JsonResponse({'status': 'fail', 'message': 'Invalid request method.'})


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

        # If there are any errors, return them in the response
        if errors:
            return JsonResponse({'status': 'error', 'errors': errors})

        # Create a new Unit instance
        new_unit = Unit(
            supplier_name=supplier_name,
            material_type=material_type,
            unit_name=unit_name,
            count=count,
            username=username
        )

        # Save the new Customer object to the database
        try:
            new_unit.save()
            # Return success response
            return JsonResponse({'status': 'success', 'message': 'Unit has been added.'})
        except Exception as e:
            # Handle any exceptions that occur during the save operation
            return JsonResponse({'status': 'error', 'message': f'Error adding Unit: {str(e)}'})
    else:
        # Handle non-POST requests
        return JsonResponse({'status': 'fail', 'message': 'Invalid request method.'})


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

        # Create a new Consumption instance
        new_consumption = Consumption(
            supplier_name=supplier_name,
            material_name=material_name,
            unit=unit,
            quantity=quantity,
            profile_name=profile_name,
            username=username
        )

        # Save the new Customer object to the database
        try:
            new_consumption.save()
            # Return success response
            return JsonResponse({'status': 'success', 'message': 'Consumption profile has been added.'})
        except Exception as e:
                # Handle any exceptions that occur during the save operation
                return JsonResponse({'status': 'error', 'message': f'Error adding consumption: {str(e)}'})
    else:
        # Handle non-POST requests
        return JsonResponse({'status': 'fail', 'message': 'Invalid request method.'})


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
                raise ValidationError("Shipment ID and cancellation reason are required.")

            # Fetch the shipment
            shipment = Shipment.objects.get(shipment_id=shipment_id)

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
            sales = Sale.objects.filter(shipment=shipment)
            for sale in sales:
                sale.payment_status = 'Cancelled'
                sale.comments = cancellation_reason
                sale.save()

            # This is a simplified example; actual implementation will depend on the specific logic required
            # For example, updating the status of related products to 'In-stock' and their location to 'Canceled'

            # Return success response
            return JsonResponse({'status': 'success', 'message': f'Shipment {shipment_id} has been canceled.'})

        except Shipment.DoesNotExist:
            # Handle case where the shipment does not exist
            return JsonResponse({'status': 'fail', 'message': 'Shipment not found.'})

        except ValidationError as e:
            # Handle validation errors
            return JsonResponse({'status': 'fail', 'message': str(e)})

        except Exception as e:
            # Handle other exceptions
            return JsonResponse({'status': 'fail', 'message': 'An error occurred: ' + str(e)})

    else:
        # Handle non-POST requests
        return JsonResponse({'status': 'fail', 'message': 'Invalid request method.'})


@csrf_exempt
def apiHandler(request):
    if request.method == 'POST':
        print(dict(request.GET.items()))
        # print(request.json())
        # Extract data from the request
        data = request.GET
        print(data)
        # Define required fields
        required_fields = ['supplier_name', 'material_type', 'unit_name', 'quantity', 'anbar_location', 'reason', 'forklift_driver']

        # Validate required fields
        errors = [{'status': 'error', 'message': f'{field} is required.'} for field in required_fields if not data.get(field)]

        # If there are any errors, return them in the response
        if errors:
            return JsonResponse({'status': 'error', 'errors': errors})

        return JsonResponse({'status':'ok', 'data': data, 'error': errors})
    else:
        # Handle non-POST requests
        return JsonResponse({'error': 'Method not allowed'}, status=405)
