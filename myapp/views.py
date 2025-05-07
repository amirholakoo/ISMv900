import json
import pandas as pd
import logging
from django.shortcuts import render, redirect
from .models import *
from django.db.models import Count
from django.http import JsonResponse
from django.core.exceptions import ValidationError
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.db import connection
from django.apps import apps
from django.db import models
from django.apps import apps
from django.db.models.base import ModelBase
import jdatetime
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.forms.models import model_to_dict
import os
import qrcode
from io import BytesIO
from django.core.files.base import ContentFile
from django.http import HttpResponse
import base64
from django.contrib import admin
from django.http import JsonResponse
import pandas as pd
from django.utils import timezone
from django.http import FileResponse
from django.http import JsonResponse
from django.utils import timezone
from datetime import timedelta
from .models import Shipments

datetime_fields = ['receive_date', 'entry_time', 'weight1_time', 'weight2_time', 'exit_time', 'date', 'payment_date']


def get_time():
    return timezone.now().strftime('%Y-%m-%d %H:%M')

def log_generator(username, action):
    # Get the current timestamp
    current_time = timezone.now().strftime('%Y-%m-%d %H:%M')

    # Create the log entry
    log = f' {current_time} {action} By {username},'
    return log


def not_enough_log_generator(location):
    # Get the current timestamp
    current_time = timezone.now().strftime('%Y-%m-%d %H:%M')

    # Create the log entry
    log = f' {current_time} ERROR:NOT ENOUGH IN {location} by SYSERR,'

    return log


def not_enough_alert(msg):
    # Create a new Alert instance with a message
    new_alert = Alert(message=msg, date=get_time())
    new_alert.save()  # Save the object to the database
    alert_values = model_to_dict(new_alert)
    # Broadcast the message to all connected clients
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "alert", {"type": "alert.message", "message": msg, "data": alert_values}
    )

def append_log(fields, page):
    current_time = timezone.now().strftime('%Y-%m-%d %H:%M')
    logs = ''
    for filed, message in fields.items():
        logs += f" {current_time} {message} by {page} FOR {filed},"
    return logs

def not_enough_message(inventory, amount, required, transferred, location, action):
    msg = f"عدم موجودی کافی در انبار {location}! موجودی: {inventory}, درخواست شده: {amount}, مقدار مورد نیاز: {required}, انتقال یافته: {transferred}, متاسفیم! درحال حاضر موجودی در انبار {location} کافی نیست. حداکثر {transferred} از این کالا {action}."
    return msg


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
            truck = Truck.objects.filter(license_number=license_number)
            if truck.exists():
                # If the truck exists, return a success response
                return JsonResponse({'isExists': 'true', 'message': 'License number exists.', 'status': truck.first().status})
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
        # print(driver_name)
        # Create new truck
        new_truck = Truck(
            license_number=license_number,
            driver_name=driver_name,
            driver_doc=driver_doc,
            phone=phone,
            username=username,
            logs=log_generator(username, 'Created'),
        )

        errors = []
        # Save the new Customer object to the database
        try:
            new_truck.save()
            return JsonResponse({'status': 'success', 'message': f'New license number {license_number} has been added to database successfully!'})
        except Exception as e:
            # print(e)
            # print(license_number)
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

        # Create a new Supplier object
        new_supplier = Supplier(
            supplier_name=supplier_name,
            address=address,
            phone=phone,
            comments=comments,
            username=username,
            status='Active',
            logs=log_generator(username, 'Created') + append_log({'comments': comments}, 'add Supplier')
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
            error_message = f"در حال حاضر یک مشتری با نام {customer_name} در سیستم وجود دارد."
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
            logs=log_generator(username, 'Created') + append_log({'comments':comments}, 'add Customer')
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
        isExist = RawMaterial.objects.filter(supplier_name=supplier_name,material_type=material_type,material_name=material_name).exists()
        # Load existing customer names from DB Check for duplicate name
        if isExist:
            error_message = f"در حال حاضر یک مشتری با نام {supplier_name} و نوع ماده {material_type} و ماده {material_name} در سیستم وجود دارد."
            errors.append({'status': 'error', 'message': error_message})

        # If there are any errors, return them in the response
        if errors:
            return JsonResponse({'status': 'error', 'errors': errors})

        # Create a new Customer object
        new_RawMaterial = RawMaterial(
            supplier_name=supplier_name,
            material_type=material_type,
            material_name=material_name,
            description=comments,
            username=username,
            logs=log_generator(username, 'Created') + append_log({'description': comments}, 'add RawMaterial')
        )

        # Save the new Customer object to the database
        try:
            new_RawMaterial.save()
            return JsonResponse({'status': 'success',
                                 'message': f'New Material: {material_name} has been added to database successfully!'})
        except Exception as e:
            # Handle any exceptions that occur during the save operation
            errors.append({'status': 'error', 'message': f'Error adding RawMaterial: {str(e)}'})
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
            consumptions = ConsumptionProfile.objects.all()

            # Extract the profile names from each record
            profile_names = [consumption.profile_name for consumption in consumptions]

            # Return the profile names as a JSON response
            return JsonResponse({'profile_names': list(set(profile_names))}, status=200)

        except Exception as e:
            # Return a   500 error for any exceptions
            return JsonResponse({'error': str(e)}, status=500)

def get_reel_number(request):
    if request.method == 'GET':
        # Load the last reel number from the Products DB
        last_product = Products.objects.last()
        if last_product:
            last_reel_number = last_product.reel_number
            width = last_product.width
            GSM = last_product.gsm
            length = last_product.length
            breaks = last_product.breaks
            grade = last_product.grade
            profile_name = last_product.profile_name
        else:
            last_reel_number = 0
            width = 0
            GSM = 0
            length = 0
            breaks = 0
            grade = 0
            profile_name = 0
        next_reel_number = int(last_reel_number) + 1
        # print(next_reel_number, last_reel_number)
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
            profile_name = request.GET.get('consumption_profile_name')
            qr_code = request.GET.get('qr_code')
            username = request.GET.get('username')
            commnet = request.GET.get('commnet')

            # Initialize an empty list to collect error messages
            errors = []
            warning = []

            # # Check if all required fields are provided
            # if not reel_number:
            #     errors.append({'status': 'error', 'message': 'reel number is required.'})
            # if not width:
            #     errors.append({'status': 'error', 'message': 'width is required.'})
            # if not gsm:
            #     errors.append({'status': 'error', 'message': 'gsm is required.'})
            # if not length:
            #     errors.append({'status': 'error', 'message': 'length is required.'})
            # if not breaks:
            #     errors.append({'status': 'error', 'message': 'breaks is required.'})
            # if not grade:
            #     errors.append({'status': 'error', 'message': 'grade is required.'})
            # if not profile_name:
            #     errors.append({'status': 'error', 'message': 'consumption profile name is required.'})
            # if not username:
            #     errors.append({'status': 'error', 'message': 'username is required.'})
            # If there are any errors, return them in the response
            # if errors:
            #     return JsonResponse({'status': 'error', 'errors': errors})



            # Create a new Products record
            new_product = Products(
                location='Anbar_Salon_Tolid',
                status='In-stock',
                qr_code=qr_code,
                reel_number=reel_number,
                width=width,
                gsm=gsm,
                length=length,
                breaks=breaks,
                grade=grade,
                username=username,
                comments=commnet,
                profile_name=profile_name,
                receive_date=get_time(),
                logs=log_generator(username, 'Created') + append_log({'comments': commnet}, 'add New Reel')
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
                username=username,
                comments=commnet,
                profile_name=profile_name,
                receive_date=get_time(),
                logs=log_generator(username, 'Created') + append_log({'comments': commnet}, 'add New Reel')
            )
            new_anbar_record.save()

            # Get all table names from the database
            all_table_names = connection.introspection.table_names()
            anbar_table_names = [name for name in all_table_names if name.startswith('Anbar_')]
            profile_list = ConsumptionProfile.objects.filter(profile_name=profile_name)
            isExist = True # Initialize isExist as True, assuming no records are found initially
            # Initialize a dictionary to keep track of profile existence in 'Anbar_' tables.
            # Each key will represent an Anbar table name, and the default value is False, indicating the profile is not found.
            anbar_profile_found = {anbar_name: False for anbar_name in anbar_table_names}

            for each_line in profile_list:

                for anbar_name in anbar_table_names:
                    AnbarModel = apps.get_model('myapp', anbar_name)
                    anbar_records = AnbarModel.objects.filter(
                        supplier_name=each_line.supplier_name,
                        material_name=each_line.material_name,
                        status='In-stock').order_by('receive_date')[:each_line.quantity]


                    if anbar_records.exists():
                        # If records are found in the AnbarModel, set the corresponding dictionary value to True.
                        anbar_profile_found[anbar_name] = True
                        isExist = False # Set isExist to False if records are found
                        isEnough = len(anbar_records) < int(each_line.quantity)
                        # Iterate over the source records and create new instances of the target model
                        for record in anbar_records:
                            record.status = 'Used'
                            record.location = 'Consumption DB'
                            record.profile_name = profile_name
                            record.last_date = get_time()
                            if isEnough:
                                log_message = log_generator(record.profile_name, 'Used') + not_enough_log_generator('Consumption DB')
                            else:
                                log_message = log_generator(record.profile_name, 'Used')
                            record.logs = record.logs + log_message
                            record.save()
                            c = Consumption(
                                shipment_id=record.shipment_id,
                                status='Used',
                                location='Consumption DB',
                                reel_number=reel_number,
                                profile_name=profile_name,
                                unit=record.unit,
                                supplier_name=record.supplier_name,
                                material_name=record.material_name,
                                material_type=record.material_type,
                                receive_date=get_time(),
                                grade=record.grade,
                                username=username,
                                comments=commnet,
                                logs=log_message + append_log({'comments': commnet}, 'add New Reel')
                            )
                            c.save()

                        if isEnough:
                            required = abs(len(anbar_records) - int(each_line.quantity))
                            msg = not_enough_message(
                                location=anbar_name,
                                inventory=len(anbar_records),
                                amount=str(each_line.quantity),
                                required=required,
                                transferred=len(anbar_records),
                                action='مصرف شد'
                            )
                            # msg = f"انبار {anbar_name} مقدار کمتری از {str(each_line.quantity)} دارد با این حال {len(anbar_records)} مقدار مصرف شد"
                            not_enough_alert(msg)
                            warning.append({'status': 'warning', 'message': msg})

                # Check if the profile is not found in any Anbar table by examining the values in the dictionary.
                if all(value == False for value in anbar_profile_found.values()):
                    msg = f"درهیچ انباری بروفایل مصرفی با اطلاعات ذکر شده یافت نشد!اسم پروفایل مصرف: {each_line.profile_name}, اسم فروشنده: {each_line.supplier_name}, اسم ماده: {each_line.material_name}, تعداد: {each_line.quantity}"
                    not_enough_alert(msg)
                    warning.append({'status': 'warning', 'message': msg})


                # Reset the dictionary for the next profile in the list.
                anbar_profile_found = {anbar_name: False for anbar_name in anbar_table_names}
            # If there are any errors, return them in the response
            if errors:
                return JsonResponse({'status': 'error', 'errors': errors})
            if isExist:
                msg = 'در هیچ یک از انبار ها چیزی یافت نشد.'
                not_enough_alert(msg)
                warning.insert(0, {'status': 'warning', 'message': msg})

            # Return a success response
            return JsonResponse({'status': 'success', 'message': 'Reel number has been added', 'warning': warning}, status=200)

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
            # print(request.GET)
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
        if not license_number:
            errors.append({'status': 'error', 'message': 'پلاک را انتخاب کنید'})
        if not shipment_type:
            errors.append({'status': 'error', 'message': 'نوع بار نامه را انخاب کنید'})
        if shipment_type == "Incoming":
            if not supplier_name:
                errors.append({'status': 'error', 'message': 'سام تامین کننده را انتخاب کنید'})
            if not material_type:
                errors.append({'status': 'error', 'message': 'نوع ماده را انتخاب کنید'})
            if not material_name:
                errors.append({'status': 'error', 'message': 'اسم ماده را انتخاب کنید'})
        else:
            if not customer_name:
                errors.append({'status': 'error', 'message': 'اسم مشتری را انخاب کنید'})
        if not username:
            errors.append({'status': 'error', 'message': 'نام کاربری را وارد کنید'})

        if errors:
            # print(errors)
            return JsonResponse({'status': 'error', 'errors': errors})

        else:
            # print('dooooooo')
            # Create new shipment
            if shipment_type == "Incoming":
                shipment = Shipments(
                    license_number=license_number,
                    supplier_name=supplier_name,
                    material_type=material_type,
                    material_name=material_name,
                    shipment_type=shipment_type,
                    status='Registered',
                    location='Entrance',
                    username=username,
                    date=get_time(),
                    entry_time=get_time(),
                    receive_date=get_time(),
                    logs=log_generator(username, 'Created')
                )
            else:
                shipment = Shipments(
                    license_number=license_number,
                    shipment_type=shipment_type,
                    customer_name=customer_name,
                    status='Registered',
                    location='Entrance',
                    username=username,
                    entry_time=get_time(),
                    receive_date=get_time(),
                    logs=log_generator(username, 'Created')
                )

            # change Truck status to Busy
            try:
                # Use update to change the status atomically
                Truck.objects.filter(license_number=license_number).update(status='Busy')
            except Truck.DoesNotExist:
                errors.append({'status': 'error', 'message': 'هیچ کامیونی با این پلاک وجود ندارد.'})
                return JsonResponse({'status': 'error', 'errors': errors}, status=404)

            # Save the new Shipment object to the database
            try:
                shipment.save()
                return JsonResponse({'status': 'success', 'message': 'بار نامه با موفقیت اضافه شد.'})

            except Exception as e:
                errors.append({'status': 'error', 'message': f'Error adding shipment: {str(e)}'})
                # Handle any exceptions that occur during the save operation
                return JsonResponse({'status': 'error', 'errors': errors})
    else:
        return render(request, 'add_shipment.html')


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
            shipment_type = request.GET.get('shipment_type')
            if shipment_type:
                shipments = Shipments.objects.filter(status=status, location=location, shipment_type=shipment_type)
            else:
                # Query the Shipments model for records with status
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
                shipment = Shipments.objects.filter(license_number=license_number, status='Office',location='Office', shipment_type='Incoming').first()
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
        weight1 = int(weight1)
        if weight1 < 9 or weight1 > 38000:
            errors.append('وزن وارد شده باید بین 9 تا 38000 کیلوگرم باشد.')

        if errors:
            return JsonResponse({'status': 'error', 'errors': errors})
        else:
            try:
                ship = Shipments.objects.filter(license_number=license_number, status='Registered', location='Entrance').first()
                Shipments.objects.filter(license_number=license_number, status='Registered', location='Entrance').update(
                    weight1=weight1,
                    weight1_time=get_time(),
                    status='LoadingUnloading',
                    location='Weight1',
                    logs=ship.logs + log_generator(username, 'Weight1')
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
        status = request.GET.get('status')
        location = request.GET.get('location')
        # print(license_number)
        if license_number:
            # Filter Shipments based on the license_number
            shipment = Shipments.objects.filter(status=status, location=location, license_number=license_number).first()
            if shipment:
                # Return the weight1 of the shipment
                return JsonResponse({'weight1': shipment.weight1})
            else:
                return JsonResponse({'error': 'هیج بار نامه ای با شماره پلاک مورد نظر یافت نشد.'}, status=404)
        else:
            return JsonResponse({'error': 'شماره پلاک مورد نیازاست'}, status=400)

@csrf_exempt
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
            weight1 = int(weight1)
            weight2 = int(weight2)
            net_weight = int(net_weight)
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
                ship = Shipments.objects.filter(license_number=license_number, status='LoadedUnloaded', location='Weight2')
                ship.update(
                    weight1=weight1,
                    weight2=weight2,
                    net_weight=net_weight,
                    weight2_time=get_time(),
                    status='Office',
                    location='Office',
                    logs=ship[0].logs+log_generator(username, 'Weight2')
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
            price_per_kg = request.GET.get('price_pre_kg')
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
            if not price_per_kg:
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
                try:

                    # Update truck status and location
                    Truck.objects.filter(license_number=license_number).update(
                        status='Free',
                        location='Entrance'
                    )
                    ship = Shipments.objects.filter(license_number=license_number, status='Office', location='Office')
                    purchase = Purchases(
                        date=get_time(),
                        receive_date=get_time(),  # Assuming you want to set the current date/time
                        # supplier_id=Supplier.objects.get(supplier_name=supplier_name),
                        license_number=license_number,
                        # material_id=MaterialType.objects.get(material_type=material_type),
                        shipment_id=ship[0],
                        supplier_name=supplier_name,
                        material_type=material_type,
                        material_name=material_name,
                        unit=unit,
                        quantity=quantity,
                        quality=quality,
                        penalty=penalty,
                        weight1=int(weight1),
                        weight2=int(weight2),
                        net_weight=int(net_weight),
                        price_per_kg=int(price_per_kg),
                        vat=vat,
                        total_price=int(total_price),
                        extra_cost=int(extra_cost),
                        invoice_status=invoice_status,
                        invoice_number=supplier_invoice,
                        status=payment_status,
                        document_info=document_info,
                        comments=commnet,
                        username=username,
                        logs=log_generator(username, 'Created PO') + append_log({'comments': commnet, 'quality':quality, 'penalty':penalty}, 'PO')
                    )
                    # Save the new purchase object to the database
                    purchase.save()
                    ship.update(
                        purchase_id=purchase.id,
                        vat=vat,
                        penalty=penalty,
                        price_per_kg=price_per_kg,
                        total_price=total_price,
                        extra_cost=extra_cost,
                        invoice_status=invoice_status,
                        payment_status=payment_status,
                        document_info=document_info,
                        exit_time=get_time(),
                        status='Delivered',
                        location='Delivered',
                        comments=commnet,
                        logs=ship[0].logs + log_generator(username, 'Created PO') + append_log({'comments': commnet, 'penalty':penalty}, 'PO')
                    )
                    return JsonResponse({'status': 'success', 'message': 'purchase added successfully.'})
                except Exception as e:
                    # Handle any exceptions that occur during the save operation
                    return JsonResponse({'status': 'error', 'message': f'Error adding purchase: {str(e)}'})
            # Return success response
            return JsonResponse({'status': 'success', 'message': 'Purchase Order created successfully.'})

        except Exception as e:
            # print(e)
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
        comments = request.GET.get('commnet')
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

        if not username:
            errors.append({'status':'error', 'message': 'فرم نام کاربری را پر کنید'})
        if errors:
            return JsonResponse({'status': 'error', 'errors': errors})
        else:
            try:
                ship = Shipments.objects.filter(license_number=license_number, status='Office', location='Office', shipment_type='Outgoing')
                # Create a new instance of the Sales model
                sale = Sales(
                    customer_name=customer_name,
                    license_number=license_number,
                    list_of_reels=list_of_reels,
                    profile_name=consuption_profile_name,
                    weight1=weight1,
                    weight2=weight2,
                    net_weight=net_weight,
                    price_per_kg=price_pre_kg,
                    vat=vat,
                    width=ship[0].width,
                    total_price=total_price,
                    extra_cost=extra_cost,
                    invoice_status=invoice_status,
                    invoice_number=invoice_number,
                    status=payment_status,
                    document_info=document_info,
                    comments=comments,
                    username=username,
                    shipment=ship[0],
                    date=get_time(),  # Assuming you want to set the current date and time
                    logs=log_generator(username, 'Created SO') + append_log({'comments': comments}, 'SO')
                )
                # Save the instance
                sale.save()

                # Retrieve the shipment instance

                ship.update(
                    status='Delivered',
                    location='Delivered',
                    sales_id=sale.id,
                    price_per_kg=price_pre_kg,
                    total_price=total_price,
                    vat=vat,
                    extra_cost=extra_cost,
                    invoice_status=invoice_status,
                    payment_status=payment_status,
                    document_info=document_info,
                    exit_time=get_time(),
                    comments=comments,
                    logs=ship[0].logs + log_generator(username, 'Created SO') + append_log({'comments': comments}, 'SO')
                )
                # Update truck status and location
                Truck.objects.filter(license_number=license_number).update(
                    status='Free',
                    location=customer_name
                )
                list_of_reels = list(map(int, list_of_reels.split(',')))
                # print(list_of_reels)
                for reel in list_of_reels:
                    products = Products.objects.filter(reel_number=reel)
                    products.update(
                        status='Delivered',
                        location=customer_name,
                        last_date=get_time(),
                        logs=products[0].logs + log_generator(username, 'Created SO')
                    )
                    # Dynamically get the model based on the anbar_name
                    AnbarModel = apps.get_model('myapp', loading_location)
                    anbar = AnbarModel.objects.filter(reel_number=reel)
                    anbar.update(
                        status='Delivered',
                        location=customer_name,
                        last_date=get_time(),
                        logs=anbar[0].logs + log_generator(username, 'Created SO')
                    )
                # Return a success response
                return JsonResponse({'status': 'success', 'message': 'Sales Order created successfully.'})

            except Shipments.DoesNotExist:
                return JsonResponse({'status': 'error', 'message': 'Shipments not found.'}, status=404)
            except Exception as e:
                # print(e)
                errors.append({'status': 'error', 'message': str(e)})
                return JsonResponse({'status': 'error', 'errors': errors})
                # return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
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
                # Check if the queryset is empty
                if not shipment.exists():
                    return JsonResponse({'status': 'error', 'message': 'Shipments not found.'}, status=404)

                # Now it's safe to access the first element
                material_name = shipment.first().material_name
                material_type = shipment.first().material_type
                supplier_name = shipment.first().supplier_name
                shipment_id = shipment.first()
                shipment_log = shipment.first().logs


                shipment.update(
                    unload_location=unloading_location,
                    unit=unit,
                    quantity=quantity,
                    quality=quality,
                    location='Weight2',
                    status='LoadedUnloaded',
                    logs=shipment_log + log_generator(forklift_driver, 'Unloaded') + append_log({'quality': quality}, 'unload')
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
                        material_type=material_type,
                        shipment_id=shipment_id,
                        unit=unit,
                        grade=quality,
                        status='In-stock',
                        location=unloading_location,
                        receive_date=get_time(),
                        username=forklift_driver,
                        logs=shipment_log + log_generator(forklift_driver, 'Unloaded') + append_log({'grade': quality}, 'unload')
                    )


                # Return a success response
                return JsonResponse({'status': 'success','message': f' {quantity_to_unload}واحد به {license_number} اضافه شد.'})

            except Shipments.DoesNotExist:
                return JsonResponse({'status': 'error', 'message': 'Shipments not found.'}, status=404)
            except Exception as e:
                print(e)
                return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method.'}, status=400)



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

        model_class = apps.get_model('myapp', anbar_location)
        # Fetch widths from the specified anbar location where the status is "In-stock"
        widths = model_class.objects.filter(status='In-stock').values_list('width', flat=True).distinct()
        # Return the widths as a JSON response
        return JsonResponse({'widths': list(widths)}, status=200)
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
                # material_name = shipment[0].material_name
                # supplier_name = shipment[0].supplier_name
                # print(shipment)
                # Dynamically import the model class
                AnbarModel = apps.get_model('myapp', loading_location)
                for reel_number in reel_numbers:
                    anbar=AnbarModel.objects.filter(reel_number=reel_number, width=width, )
                    logs = anbar[0].logs + log_generator(forklift_driver, 'Loaded')

                    anbar.update(
                        shipment_id=shipment[0],
                        status='Sold',
                        location=license_number,
                        # supplier_name=supplier_name,
                        # material_name=material_name,
                        # receive_date=get_time(),
                        # last_date=get_time(),
                        logs=logs,
                    )

                    product = Products.objects.filter(reel_number=reel_number, width=width,)
                    logs = product[0].logs + log_generator(forklift_driver, 'Loaded')
                    product.update(
                        shipment_id=shipment[0],
                        status='Sold',
                        location=license_number,
                        # receive_date=get_time(),
                        # last_date=get_time(),
                        logs=logs,
                    )
                profile_name = product[0].profile_name
                # print(profile_name)
                shipment.update(
                    profile_name=profile_name,
                    unload_location=loading_location,
                    list_of_reels=','.join(reel_numbers),
                    location='Weight2',
                    status='LoadedUnloaded',
                    width=width,
                    logs=shipment[0].logs + log_generator(forklift_driver, 'Loaded'),
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
            supplier_name = anbar_model.objects.exclude(supplier_name__isnull=True).exclude(
                supplier_name__exact='').values_list('supplier_name', flat=True).distinct()
            material_name = anbar_model.objects.exclude(material_name__isnull=True).exclude(
                material_name__exact='').values_list('material_name', flat=True).distinct()
            unit = anbar_model.objects.exclude(unit__isnull=True).exclude(unit__exact='').values_list('unit',
                                                                                                      flat=True).distinct()
            supplier_names = list(set(supplier_name))
            material_names = list(set(material_name))
            units = list(set(unit))

            # Return the widths as a JSON response
            return JsonResponse({'supplier_names': supplier_names, 'material_names': material_names, 'units':units}, status=200)
        except Exception as e:
            # Handle any exceptions that occur during the process
            return JsonResponse({'error': str(e)}, status=500)


def get_unit_and_materialName_based_supplierNmae_andbar(request):
    if request.method == 'GET':
        anbar_location = request.GET.get('anbar_location')
        supplier_name = request.GET.get('supplier_name')
        try:
            anbar_model = apps.get_model('myapp', anbar_location)
            anbar = anbar_model.objects.filter(supplier_name=supplier_name, status='In-stock', location=anbar_location)
            units = []
            material_names = []
            for record in anbar:
                units.append(record.unit)
                material_names.append(record.material_name)
            # Return the widths as a JSON response
            return JsonResponse({'material_names': list(set(material_names)), 'units':list(set(units))}, status=200)
        except Exception as e:
            # Handle any exceptions that occur during the process
            return JsonResponse({'error': str(e)}, status=500)


def get_supplierNames_based_consumtioon(request):
    if request.method == 'GET':
        profile_name = request.GET.get('profile_name')
        try:
            # Further filter by profile_name if provided
            if profile_name:
                used_records = Consumption.objects.filter(profile_name='')
            else:
                used_records = Consumption.objects.filter(status='Used').exclude(profile_name__isnull=True).exclude(profile_name='')

            # If you want to get all unique supplier_names from these records
            supplier_names = used_records.values_list('supplier_name', flat=True).distinct()
            supplier_names = list(set(supplier_names))
            # Return the widths as a JSON response
            return JsonResponse({'supplier_names': supplier_names}, status=200)
        except Exception as e:
            # Handle any exceptions that occur during the process
            return JsonResponse({'error': str(e)}, status=500)


def get_unit_and_materialName_based_supplierNmae_consumption(request):
    if request.method == 'GET':
        supplier_name = request.GET.get('supplier_name')
        try:
            used_records = Consumption.objects.filter(supplier_name=supplier_name, status='Used')
            units = used_records.values_list('unit', flat=True).distinct()
            material_names = used_records.values_list('material_name', flat=True).distinct()

            # Return the widths as a JSON response
            return JsonResponse({'material_names': list(set(material_names)), 'units':list(set(units))}, status=200)
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
            # print(unit_names)
            # Return the widths as a JSON response
            return JsonResponse({'unit_names': unit_names}, status=200)
        except Exception as e:
            # Handle any exceptions that occur during the process
            return JsonResponse({'error': str(e)}, status=500)


def get_unit_names_based_on_license_of_shipment(request):
    if request.method == 'GET':
        lic_number = request.GET.get('lic_number')
        shipment = Shipments.objects.get(license_number=lic_number, status='LoadingUnloading', location='Weight1')
        supplier_name = shipment.supplier_name
        units = Unit.objects.filter(supplier_name=supplier_name)
        unit_names = [unit.unit_name for unit in units]
        return JsonResponse({'unit_names':unit_names}, safe=False)
    else:
        return JsonResponse({"error": "Invalid request method"}, status=400)

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
            # filtered anbar based on quantity:
            # Dynamically get the model based on the anbar_name
            AnbarModel = apps.get_model('myapp', unloading_location)
            anbar = AnbarModel.objects.filter(
                supplier_name=supplier_name,
                material_name=material_name,
                unit=unit,
                status='In-stock'
            ).order_by('receive_date')[:quantity_to_unload]
            # get material type form rawMaterial
            raw = RawMaterial.objects.filter(
                supplier_name=supplier_name,
                material_name=material_name,
            )
            material_type = raw[0].material_type
            isEnough = len(anbar) < quantity_to_unload

            for record in anbar:
                # update anbar:
                record.status='Used'
                record.location='Consumption DB'
                record.logs=record.logs+log_generator(forklift_driver, 'Used')
                if isEnough:
                    log_message = log_generator(forklift_driver, 'Used') + not_enough_log_generator('Consumption DB')
                else:
                    log_message = log_generator(forklift_driver, 'Used')

                record.last_date=get_time()
                record.save()
                consumption = Consumption(
                        shipment_id=record.shipment_id,
                        receive_date=get_time(),
                        supplier_name=supplier_name,
                        material_name=material_name,
                        material_type=material_type,
                        location='Consumption DB',
                        unit=unit,
                        status='Used',
                        grade=record.grade,
                        comments=record.comments,
                        username=forklift_driver,
                        logs=log_message + append_log({'comments': record.comments}, 'used')
                )
                consumption.save()

            if isEnough:
                # Alert here
                required = abs(len(anbar) - quantity_to_unload)
                msg = not_enough_message(
                    location=unloading_location,
                    inventory=len(anbar),
                    amount=quantity_to_unload,
                    required=required,
                    transferred=len(anbar),
                    action='مصرف شد'
                )
                # msg = 'انبار' + 'Consumption DB' + f'از مقدار که شما انتخاب کردید ( {quantity_to_unload} ) ' + 'مقدار کمتری دارد' + str(
                #     len(anbar)) + 'تا منتقل شد'
                not_enough_alert(msg)
                errors = [{'status': 'error', 'message': msg}]
                return JsonResponse({'status': 'error', 'errors': errors})

            # Return a success response

            return JsonResponse({'status': 'success', 'message': f'{quantity} units of {material_name} have been marked as used.'})

        except Exception as e:
            print(e)
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method.'}, status=400)

@csrf_exempt
def load_data_for_moved(request):
    try:
        # Extract the anbar_location from the query parameters
        anbar_location = request.GET.get('anbar_location')
        real_or_raw = request.GET.get('real_or_raw')
        if not anbar_location:
            return JsonResponse({'error': 'Anbar location is required'}, status=400)

        # Dynamically import the model class
        anbar_model = apps.get_model('myapp', anbar_location)

        # Query the model to get reel numbers where the width matches the specified width,
        # the status is "In-stock", and sort the results by receive_date (old to new)
        # anbar = anbar_model.objects.filter(status='In-stock')
        # print(anbar)
        if real_or_raw == 'Raw':
            supplier_name = anbar_model.objects.values_list('supplier_name', flat=True).distinct()
            material_name = anbar_model.objects.values_list('material_name', flat=True).distinct()
            unit = anbar_model.objects.values_list('unit', flat=True).distinct()
            supplier_names = list(supplier_name)
            material_names = list(material_name)
            units = list(unit)
            data = {'supplier_names': supplier_names, 'material_names': material_names, 'units':units}
        if real_or_raw == 'Reel':
            widths = anbar_model.objects.filter(status='In-stock').values('width').distinct()
            reel_numbers = anbar_model.objects.filter(status='In-stock').values('reel_number').distinct()

            data = {
                "width": [item['width'] for item in widths],
                # "reel_number": [item['reel_number'] for item in reel_numbers],
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
        from_anbar = request.GET.get('from_anbar')
        reel = request.GET.get('reel')
        supplier_name = request.GET.get('supplier_name')
        material_name = request.GET.get('material_name')
        unit = request.GET.get('unit')
        Quantity = request.GET.get('Quantity')
        width = request.GET.get('width')
        to_anbar = request.GET.get('to_anbar')
        forklift_driver = request.GET.get('forklift_driver')
        real_or_raw = request.GET.get('real_or_raw')

        errors = []

        try:
            AnbarModel1 = apps.get_model('myapp', from_anbar)
            AnbarModel2 = apps.get_model('myapp', to_anbar)
            # Update source AnbarGeneric items
            if real_or_raw == 'Raw':
                sourse = AnbarModel1.objects.filter(
                    location=from_anbar,
                    supplier_name=supplier_name,
                    material_name=material_name,
                ).order_by('receive_date')[:int(Quantity)]
                isEnough = len(sourse) < int(Quantity)
                if isEnough:
                    log_message = log_generator(forklift_driver, 'Moved') + not_enough_log_generator(to_anbar)
                else:
                    log_message = log_generator(forklift_driver, 'Moved')

                # Iterate over the records and update each one
                for record in sourse:
                    record.status = 'Moved'
                    record.location = to_anbar
                    record.last_date = get_time()
                    record.logs = record.logs + log_message
                    # Create new entries in the destination AnbarGeneric location
                    new_item = AnbarModel2(
                        receive_date=get_time(),
                        location=to_anbar,
                        status='In-stock',
                        supplier_name=supplier_name,
                        material_name=material_name,
                        material_type=record.material_type,
                        unit=unit,
                        grade=record.grade,
                        shipment_id=record.shipment_id,
                        username=forklift_driver,
                        logs=log_message
                    )
                    # Save the updated record
                    record.save()
                    new_item.save()


                if isEnough:
                    required = abs(len(sourse) - int(Quantity))
                    msg = not_enough_message(
                        location=from_anbar,
                        inventory=len(sourse),
                        amount=int(Quantity),
                        required=required,
                        transferred=len(sourse),
                        action=f'به {str(to_anbar)} انتقال یافت'
                    )
                    # msg = 'انبار' + str(to_anbar) + f'از مقدار که شما انتخاب کردید ( {Quantity} ) ' + 'مقدار کمتری دارد' + str(len(sourse)) +' تا منتقل شد'
                    not_enough_alert(msg)
                    errors.append({'status': 'error', 'message': msg})
                    return JsonResponse({'status': 'error', 'errors': errors})

                # Return a success response
                return JsonResponse({'status': 'success', 'message': f'{Quantity} units of {material_name} have been moved from {from_anbar} to {to_anbar}.'})

            if real_or_raw == 'Reel':
                sourse = AnbarModel1.objects.filter(
                    location=from_anbar,
                    width=width,
                    status='In-stock',
                    reel_number=reel,
                ).order_by('receive_date')

                products = Products.objects.filter(
                    location=from_anbar,
                    width=width,
                    status='In-stock',
                    reel_number=reel,
                ).order_by('receive_date')

                for record in sourse:
                    # update anbar a
                    record.last_date = get_time()
                    record.status = 'Moved'
                    record.location = to_anbar
                    record.logs =record.logs + log_generator(forklift_driver, 'Moved')
                    # insert to anbar 2
                    new_item = AnbarModel2(
                        receive_date=get_time(),
                        location=to_anbar,
                        status='In-stock',
                        width=width,
                        unit=record.unit,
                        reel_number=reel,
                        gsm=record.gsm,
                        length=record.length,
                        grade=record.grade,
                        breaks=record.breaks,
                        qr_code=record.qr_code,
                        comments=record.comments,
                        profile_name=record.profile_name,
                        shipment_id=record.shipment_id,
                        username=forklift_driver,
                        logs=log_generator(forklift_driver, 'Moved') + append_log({'comments': record.comments}, 'Moved')
                    )
                    record.save()
                    new_item.save()
                for record in products:
                    record.location=to_anbar
                    record.logs =record.logs + log_generator(forklift_driver, 'Moved')
                    record.save()

                # Return a success response
                return JsonResponse({'status': 'success', 'message': f'1 units of {material_name} have been moved from {from_anbar} to {to_anbar}.'})

        except Exception as e:
            print(e)
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method.'}, status=400)


def get_returned_data(request):
    if request.method == 'GET':
        try:

            # Filter the queryset to include only records with status 'Used'
            used_consumptions = Consumption.objects.filter(status='Used')

            # Get distinct values for 'supplier_name', 'material_name', and 'unit'
            supplier_names = used_consumptions.values_list('supplier_name', flat=True).distinct()
            material_names = used_consumptions.values_list('material_name', flat=True).distinct()
            units = used_consumptions.values_list('unit', flat=True).distinct()

            supplier_names = list(set(supplier_names))
            material_names = list(set(material_names))
            units = list(set(units))

            # Return the widths as a JSON response
            return JsonResponse({'supplier_names': supplier_names, 'material_names': material_names, 'units': units},
                                status=200)
        except Exception as e:
            # Handle any exceptions that occur during the process
            return JsonResponse({'error': str(e)}, status=500)


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
        material_name = request.GET.get('material_name')
        unit = request.GET.get('unit')
        quantity = request.GET.get('Quantity')
        to_anbar = request.GET.get('to_anbar')
        reason = request.GET.get('reason')
        forklift_driver = request.GET.get('forklift_driver')

        errors = []

        # Check if all required fields are provided
        if not supplier_name:
            errors.append({'status': 'error', 'message': 'supplier name is required.'})
        if not material_name:
            errors.append({'status': 'error', 'message': 'material type is required.'})
        if not unit:
            errors.append({'status': 'error', 'message': 'unit_name is required.'})
        if not quantity:
            errors.append({'status': 'error', 'message': 'quantity is required.'})
        if not to_anbar:
            errors.append({'status': 'error', 'message': 'anbar location is required.'})
        if not reason:
            errors.append({'status': 'error', 'message': 'reason is required.'})
        if not forklift_driver:
            errors.append({'status': 'error', 'message': 'forklift_driver is required.'})

        # If there are any errors, return them in the response
        if errors:
            return JsonResponse({'status': 'error', 'errors': errors})
        else:
            try:
                # print(supplier_name, material_name, unit)
                AnbarModel = apps.get_model('myapp', to_anbar)
                consumption = Consumption.objects.filter(
                    supplier_name=supplier_name,
                    material_name=material_name,
                    unit=unit,
                    profile_name=None
                ).order_by('receive_date')[:int(quantity)]
                isEnough = len(consumption) < int(quantity)

                if isEnough:
                    # Alert here
                    # print('not enough', len(consumption), int(quantity))
                    required = abs(len(consumption) - int(quantity))
                    msg = not_enough_message(
                        location='(Consumption DB)',
                        inventory=len(consumption),
                        amount=int(quantity),
                        required=required,
                        transferred=len(consumption),
                        action=f'به {str(to_anbar)} انتقال یافت'
                    )
                    # msg = 'انبار' + str(to_anbar) + f'از مقدار که شما انتخاب کردید ( {int(quantity)} ) ' + 'مقدار کمتری دارد' + str(len(consumption)) + ' تا منتقل شد'
                    not_enough_alert(msg)
                    errors.append({'status': 'error', 'message': msg})
                    return JsonResponse({'status': 'error', 'errors': errors})

                for record in consumption:
                    record.comments = reason
                    record.status = 'Returned'
                    record.location = to_anbar
                    record.last_date = get_time()
                    record.logs =record.logs + log_generator(forklift_driver, 'Returned')
                    if isEnough:
                        log_message = log_generator(forklift_driver, 'Returned') + not_enough_log_generator(to_anbar)
                    else:
                        log_message =log_generator(forklift_driver, 'Returned')

                    # Create new entries in the destination AnbarGeneric location
                    new_item = AnbarModel(
                        shipment_id=record.shipment_id,
                        receive_date=get_time(),
                        location=to_anbar,
                        status='In-stock',
                        supplier_name=supplier_name,
                        material_name=material_name,
                        material_type=record.material_type,
                        unit=unit,
                        username=forklift_driver,
                        comments=reason,
                        logs=log_message + append_log({'comments': reason}, 'Returned')
                    )
                    # Save the updated record
                    record.save()
                    new_item.save()

                return JsonResponse(
                    {'status': 'success', 'message': f'ok'})
            except ValidationError as e:
                # print(e)
                # Return a validation error response
                return JsonResponse({'error': str(e)}, status=400)
            except Exception as e:
                # print(e)
                # Return a general error response
                return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})


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
                    'material_name', 'reel_number', 'status', 'location', 'last_date', 'width', 'gsm', 'length',
                    'grade',
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
            isExist = MaterialType.objects.filter(supplier_name=supplier_name,material_type=material_type,).exists()
            # Load existing customer names from DB Check for duplicate name
            if isExist:
                error_message = f"در حال حاضر یک مشتری با نام {supplier_name} و نوع ماده {material_type} در سیستم وجود دارد."
                errors.append({'status': 'error', 'message': error_message})

            # If there are any errors, return them in the response
            if errors:
                return JsonResponse({'status': 'error', 'errors': errors})

            # Create a new MaterialType instance
            new_material_type = MaterialType(
                supplier_name=supplier_name,
                material_type=material_type,
                username=username,
                status='Active',
                logs=log_generator(username, 'Created')
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

        isExist = Unit.objects.filter(supplier_name=supplier_name,material_type=material_type,unit_name=unit_name).exists()
        # Load existing customer names from DB Check for duplicate name
        if isExist:
            error_message = f"در حال حاضر یک مشتری با نام {supplier_name} و نوع ماده {material_type} و واحد {unit_name} در سیستم وجود دارد."
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
                date=get_time(),
                status='Active',
                logs=log_generator(username, 'Created')
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
            raw = RawMaterial.objects.filter(supplier_name=supplier_name, material_name=material_name, status='Active')
            material_type = raw[0].material_type
            unit = profile['unit']
            quantity = profile['quantity']
            # Create a new ConsumptionProfile instance
            new_consumption = ConsumptionProfile(
                profile_name=profile_name,
                supplier_name=supplier_name,
                material_name=material_name,
                material_type=material_type,
                unit=unit,
                quantity=int(quantity),
                receive_date=get_time(),
                status="Active",
                username=username,
                logs=log_generator(username, 'Created')
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
def cancel(request):
    if request.method == 'POST':
        license_number = request.GET.get('license_number')
        shipment_obj = request.GET.get('shipment')
        shipment_obj = json.loads(shipment_obj)
        anbar_location = request.GET.get('unloading_location')
        cancellation_reason = request.GET.get('reason')
        username = request.GET.get('username')

        status = 'Cancelled'
        location = 'Cancelled'
        action = 'Cancelled'
        # print(shipment_obj)
        shipment = Shipments.objects.get(id=shipment_obj['id'])
        # Update the attributes of the shipment instance
        shipment.status = status
        shipment.location = location
        shipment.cancellation_reason = cancellation_reason
        shipment.logs = shipment.logs + log_generator(username, action)
        # Save the updated instance to the database
        shipment.save()

        # Update truck status and location
        Truck.objects.filter(license_number=license_number).update(
            status='Free',
            location='Entrance'
        )

        if shipment.shipment_type == "Incoming":
            purchases = Purchases.objects.filter(shipment_id=shipment)

            if purchases.exists():
                purchases.update(
                    status=status,
                    cancellation_reason=cancellation_reason,
                    logs=purchases[0].logs + log_generator(username, action)
                )

            if shipment.unload_location:
                AnbarModel = apps.get_model('myapp', shipment.unload_location)
                anbar = AnbarModel.objects.filter(
                    # supplier_name=shipment.supplier_name,
                    # material_name=shipment.material_name,
                    # status="In-stock",
                    shipment_id=shipment
                )
                if anbar.exists():
                    anbar = anbar.order_by('receive_date')[:int(shipment.quantity)]
                    for record in anbar:
                        record.status = status
                        record.location = location
                        record.last_date = get_time()
                        record.logs = record.logs + log_generator(username, action)
                        record.save()
        else:
            sales = Sales.objects.filter(shipment=shipment)
            if sales.exists():
                sales.update(
                    status=status,
                    cancellation_reason=cancellation_reason,
                    logs=sales[0].logs + log_generator(username, action)
                )
            if shipment.list_of_reels:
                # print(shipment.list_of_reels)
                list_of_reel = shipment.list_of_reels.split(',')
                for reel in list_of_reel:
                    # print(reel)
                    # reel = int(reel)
                    product = Products.objects.get(reel_number=reel)
                    # print(product)
                    product.location = anbar_location
                    product.status = 'In-stock'
                    product.last_date = None
                    product.logs = product.logs + log_generator(username, action)
                    product.save()

                    AnbarModel = apps.get_model('myapp', anbar_location)
                    anbar_a = AnbarModel(
                        reel_number=reel,
                        width=product.width,
                        gsm=product.gsm,
                        length=product.length,
                        grade=product.grade,
                        breaks=product.breaks,
                        comments=product.comments,
                        qr_code=product.qr_code,
                        profile_name=product.profile_name,
                        username=product.username,
                        status='In-stock',
                        location=anbar_location,
                        receive_date=get_time(),
                        logs=log_generator(username, 'Cancelled and Added') + append_log({'comments': product.comments}, 'Cancel')
                    )
                    anbar_a.save()
                    if shipment.unload_location:
                        AnbarModel = apps.get_model('myapp', shipment.unload_location)
                        anbar = AnbarModel.objects.filter(
                            reel_number=reel,
                            shipment_id=shipment
                        )
                        if anbar.exists():
                            # anbar = anbar.order_by('receive_date')[:int(shipment.quantity)]
                            for record in anbar:
                                record.status = status
                                record.location = location
                                # record.last_date = get_time()
                                record.logs = record.logs + log_generator(username, action)
                                record.save()

        # Return a success response
        return JsonResponse({'status': 'success', 'message': ''})

    else:
        return render(request, 'cancell_shipment.html')


@csrf_exempt
def load_shipments_baesd_license_number_for_canceling(request):
    # Check if the request method is POST
    if request.method == 'POST':
        # Extract the license number from the request data
        license_number = request.GET.get('license_number')

        shipments = Shipments.objects.filter(license_number=license_number).exclude(status='Cancelled')
        shipments = shipments.order_by('-id')
        if shipments.exists():
            shipment_list = shipments.values(
                'id',
                'receive_date',
                'supplier_name',
                'customer_name',
                'net_weight',
                'shipment_type',
                'unload_location'
            )
            # Convert the queryset to a list of dictionaries
            shipment_list = list(shipment_list)
            # Convert datetime objects to strings
            for shipment in shipment_list:
                if shipment['receive_date']:
                    # Convert Django datetime to Shamsi date
                    shamsi_date = jdatetime.datetime.fromgregorian(datetime=shipment['receive_date'])

                    shipment['receive_date'] = shamsi_date.strftime('%Y-%m-%d %H:%M')

            json_data = json.dumps(shipment_list)

            return JsonResponse({'isExists': 'false', 'message': 'shipments exists.', 'shipment_list': json_data}, status=200)
        else:
            return JsonResponse({'isExists': 'true', 'message': 'License number does not exist.'})

    else:
        # If the request method is not POST, return an error response
        return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})


def loadReportData(request):
    if request.method == 'GET':
        data = {}
        datetime_fields = ['receive_date', 'entry_time', 'weight1_time', 'weight2_time', 'exit_time', 'date', 'payment_date']

        # shipments = Shipments.objects.all().exclude(status='Cancelled').values()
        # if shipments.exists():
        #     # Convert each datetime field to Shamsi date
        #     for shipment in shipments:
        #         for field in datetime_fields:
        #             if field in shipment and shipment[field] is not None:
        #                 # Convert to Shamsi date
        #                 shamsi_date = jdatetime.datetime.fromgregorian(datetime=shipment[field])
        #                 # Update the field in the dictionary
        #                 shipment[field] = shamsi_date.strftime('%Y-%m-%d %H:%M')
        #
        #     field_names = [k for k in list(shipments)[0]]
        #     data['shipments'] = {'values':list(shipments), 'fields': field_names, 'title': 'لیست بارنامه',}

        sales = Sales.objects.all().exclude(status='Cancelled').values()
        if sales.exists():
            for sale in sales:
                for field in datetime_fields:
                    if field in sale and sale[field] is not None:
                        # Convert to Shamsi date
                        shamsi_date = jdatetime.datetime.fromgregorian(datetime=sale[field])
                        # Update the field in the dictionary
                        sale[field] = shamsi_date.strftime('%Y-%m-%d %H:%M')

            field_names = [k for k in list(sales)[0]]
            data['sales'] = {'values':list(sales), 'fields': field_names, 'title': 'لیست فروش',}

        purchases = Purchases.objects.all().exclude(status='Cancelled').values()
        if purchases.exists():
            for purchase in purchases:
                for field in datetime_fields:
                    if field in purchase and purchase[field] is not None:
                        # Convert to Shamsi date
                        shamsi_date = jdatetime.datetime.fromgregorian(datetime=purchase[field])
                        # Update the field in the dictionary
                        purchase[field] = shamsi_date.strftime('%Y-%m-%d %H:%M')

            field_names = [k for k in list(purchases)[0]]
            data['purchases'] = {'values':list(purchases), 'fields': field_names, 'title': 'لیست خرید',}

        rawMaterial = RawMaterial.objects.filter(status='In-stock').values()
        if rawMaterial.exists():
            for raw in rawMaterial:
                for field in datetime_fields:
                    if field in raw and raw[field] is not None:
                        # Convert to Shamsi date
                        shamsi_date = jdatetime.datetime.fromgregorian(datetime=raw[field])
                        # Update the field in the dictionary
                        raw[field] = shamsi_date.strftime('%Y-%m-%d %H:%M')
            field_names = [k for k in list(rawMaterial)[0]]
            data['rawMaterial'] = {'values':list(rawMaterial), 'fields': field_names, 'title': 'لیست مواد',}

        products = Products.objects.filter(status='In-stock').values()
        if products.exists():
            for product in products:
                for field in datetime_fields:
                    if field in product and product[field] is not None:
                        # Convert to Shamsi date
                        shamsi_date = jdatetime.datetime.fromgregorian(datetime=product[field])
                        # Update the field in the dictionary
                        product[field] = shamsi_date.strftime('%Y-%m-%d %H:%M')
            field_names = [k for k in list(products)[0]]
            data['products'] = {'values':list(products), 'fields': field_names, 'title': 'لیست محصولات',}

        consumption = Consumption.objects.all().values()
        if consumption.exists():
            for con in consumption:
                for field in datetime_fields:
                    if field in con and con[field] is not None:
                        # Convert to Shamsi date
                        shamsi_date = jdatetime.datetime.fromgregorian(datetime=con[field])
                        # Update the field in the dictionary
                        con[field] = shamsi_date.strftime('%Y-%m-%d %H:%M')
            field_names = [k for k in list(consumption)[0]]
            data['consumption'] = {'values':list(consumption), 'fields': field_names, 'title': 'لیست مصرف',}

        return JsonResponse({'status': 'succese', 'data': data})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method.'}, status=400)

@csrf_exempt
def report_page(request):
    if request.method == 'POST':
        pass
    else:
        return render(request, 'report_page.html')


@csrf_exempt
def generate_excel_report(request):
    model_name = request.GET.get('model_name')
    models = {
        'shipments': Shipments.objects.all().exclude(status='Cancelled').values(),
        'sales': Sales.objects.all().exclude(status='Cancelled').values(),
        'purchases': Purchases.objects.all().exclude(status='Cancelled').values(),
        'rawMaterial': RawMaterial.objects.all().values(),
        'products': Products.objects.all().values(),
        'consumption': Consumption.objects.all().values(),
        'alerts': Alert.objects.all().values()
    }
    model = models[model_name]
    # Creating DataFrames
    df = pd.DataFrame(list(model))
    # Convert datetime fields to timezone-naive format
    for col in ['receive_date', 'entry_time', 'weight1_time', 'weight2_time', 'exit_time', 'date', 'payment_date']:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col]).dt.tz_localize(None)


    # Generate a timestamp
    timestamp = timezone.now().strftime('%Y%m%d_%H%M%S')

    # Create a filename with the timestamp
    filename = f'{model_name}_{timestamp}.xlsx'
    qrcode_dir = 'reports'
    if not os.path.exists(qrcode_dir):
        os.makedirs(qrcode_dir)

    # Writing the DataFrame to an Excel file
    df.to_excel(os.path.join(qrcode_dir, filename), index=False, engine='openpyxl')
    # Open the file in binary mode
    file = open(os.path.join(qrcode_dir, filename), 'rb')

    # Create a FileResponse object
    response = FileResponse(file)

    # Set the Content-Disposition header to signal the browser to download the file
    response['Content-Disposition'] = f'{filename}'

    return response



@csrf_exempt
def generate_qrCode(request):
    # print(json.loads(dict(request.GET)))
    # Data to encode
    data = dict(request.GET)
    d =json.loads(data['data'][0])
    timestamp = timezone.now().strftime('%Y%m%d_%H%M%S')
    filename = f"reel_number_{d['reel_number']}_{timestamp}.png"

    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    my_string = data['d'][0]
    qr.add_data(my_string)
    qr.make(fit=True)
    # Create an image from the QR Code instance
    img = qr.make_image(fill_color="black", back_color="white")
    # Ensure the 'qrcode' directory exists
    qrcode_dir = 'qrcode'
    if not os.path.exists(qrcode_dir):
        os.makedirs(qrcode_dir)

    file_path = os.path.join(qrcode_dir, filename)
    # Save the image
    img.save(file_path)

    buffer = BytesIO()
    img.save(buffer)
    buffer.seek(0)
    # Encode the binary data to base64
    image_base64 = base64.b64encode(buffer.read()).decode('utf-8')

    return JsonResponse({'status': 'succeses', 'filename': file_path, 'file':image_base64})



@csrf_exempt
def report_shipment(request):
    try:
        if request.method == 'POST':
            filter_type = request.GET.get('filter')
            current_time = timezone.now()


            if filter_type == 'year':
                shipments = Shipments.objects.filter(receive_date__year=current_time.year).exclude(status='Cancelled').exclude(status='Delivered').values()
            elif filter_type == 'month':
                shipments = Shipments.objects.filter(receive_date__month=current_time.month).exclude(status='Cancelled').exclude(status='Delivered').values()
            elif filter_type == 'week':
                start_of_last_week = current_time - timedelta(days=6)
                end_of_last_week = current_time
                shipments = Shipments.objects.filter(receive_date__range=(start_of_last_week, end_of_last_week)).exclude(status='Cancelled').exclude(status='Delivered').values()
            elif filter_type == 'day':
                hours_ago = current_time - timedelta(hours=24)
                shipments = Shipments.objects.filter(receive_date__gte=hours_ago, receive_date__lt=current_time).exclude(status='Cancelled').exclude(status='Delivered').values()
            else:
                return JsonResponse({'status': 'error', 'message': 'Invalid filter type'}, status=400)

            if shipments.exists():
                for shipment in shipments:
                    for field in datetime_fields:
                        if field in shipment and shipment[field] is not None:
                            # Convert to Shamsi date
                            shamsi_date = jdatetime.datetime.fromgregorian(datetime=shipment[field])
                            # Update the field in the dictionary
                            shipment[field] = shamsi_date.strftime('%Y-%m-%d %H:%M')
                # field_names = [k for k in list(shipments)[0]]
                # print(field_names)
                field_names = [
                    'status',
                    'location',
                    'license_number',
                    'unload_location',
                    'quality',
                    'shipment_type',
                    'customer_name',
                    'supplier_name',
                    'entry_time',
                    'weight1',
                    'weight1_time',
                    'unit',
                    'quantity',
                    'width',
                    'list_of_reels',
                    'weight2',
                    'weight2_time',
                    'net_weight',
                    'price_per_kg',
                    'vat',
                    'total_price',
                    'penalty',
                    'extra_cost',
                    'exit_time',
                    'receive_date',
                    'date',
                    'profile_name',
                    'material_type',
                    'material_name',
                    'invoice_status',
                    'payment_status',
                    'document_info',
                    'comments',
                    'cancellation_reason',
                    'sales_id',
                    'purchase_id_id',
                    'username',
                    'logs']


                data = {'values': list(shipments), 'fields': field_names, 'title': 'لیست بارنامه',}
                return JsonResponse(data=data, status=200)
            else:
                return JsonResponse({'status': 'error', 'message': 'No shipment records found'}, status=404)
        else:
            return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)


@csrf_exempt
def report_Sales(request):
    try:
        if request.method == 'POST':
            filter_type = request.GET.get('filter')
            current_time = timezone.now()


            if filter_type == 'year':
                sales = Sales.objects.filter(date__year=current_time.year).exclude(status='Cancelled').values()
            elif filter_type == 'month':
                sales = Sales.objects.filter(date__month=current_time.month).exclude(status='Cancelled').values()
            elif filter_type == 'week':
                start_of_last_week = current_time - timedelta(days=6)
                end_of_last_week = current_time
                sales = Sales.objects.filter(date__range=(start_of_last_week, end_of_last_week)).exclude(status='Cancelled').values()
            elif filter_type == 'day':
                hours_ago = current_time - timedelta(hours=24)
                sales = Sales.objects.filter(date__gte=hours_ago, date__lt=current_time).exclude(status='Cancelled').values()
            else:
                return JsonResponse({'status': 'error', 'message': 'Invalid filter type'}, status=400)

            if sales.exists():
                for sale in sales:
                    for field in datetime_fields:
                        if field in sale and sale[field] is not None:
                            # Convert to Shamsi date
                            shamsi_date = jdatetime.datetime.fromgregorian(datetime=sale[field])
                            # Update the field in the dictionary
                            sale[field] = shamsi_date.strftime('%Y-%m-%d %H:%M')
                field_names = [k for k in list(sales)[0]]
                data = {'values': list(sales), 'fields': field_names, 'title': 'لیست فروش',}
                return JsonResponse(data=data, status=200)
            else:
                return JsonResponse({'status': 'error', 'message': 'No sale records found'}, status=404)
        else:
            return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)
    except Exception as e:
        print(e)
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)


@csrf_exempt
def report_Purchases(request):
    try:
        if request.method == 'POST':
            filter_type = request.GET.get('filter')
            current_time = timezone.now()


            if filter_type == 'year':
                purchases = Purchases.objects.filter(date__year=current_time.year).exclude(status='Cancelled').values()
            elif filter_type == 'month':
                purchases = Purchases.objects.filter(date__month=current_time.month).exclude(status='Cancelled').values()
            elif filter_type == 'week':
                start_of_last_week = current_time - timedelta(days=6)
                end_of_last_week = current_time
                purchases = Purchases.objects.filter(date__range=(start_of_last_week, end_of_last_week)).exclude(status='Cancelled').values()
            elif filter_type == 'day':
                hours_ago = current_time - timedelta(hours=24)
                purchases = Purchases.objects.filter(date__gte=hours_ago, date__lt=current_time).exclude(status='Cancelled').values()
            else:
                return JsonResponse({'status': 'error', 'message': 'Invalid filter type'}, status=400)

            if purchases.exists():
                for purchase in purchases:
                    for field in datetime_fields:
                        if field in purchase and purchase[field] is not None:
                            # Convert to Shamsi date
                            shamsi_date = jdatetime.datetime.fromgregorian(datetime=purchase[field])
                            # Update the field in the dictionary
                            purchase[field] = shamsi_date.strftime('%Y-%m-%d %H:%M')
                # field_names = [k for k in list(purchases)[0]]
                field_names = [
                     'date',
                     'status',
                     'payment_date',
                     'supplier_name',
                     'material_type',
                     'material_name',
                     'unit',
                     'license_number',
                     'receive_date',
                     'quantity',
                     'quality',
                     'penalty',
                     'weight1',
                     'weight2',
                     'net_weight',
                     'price_per_kg',
                     'vat',
                     'total_price',
                     'extra_cost',
                     'invoice_status',
                     'payment_details',
                     'invoice_number',
                     'document_info',
                     'comments',
                     'cancellation_reason',
                     'shipment_id_id',
                     'username',
                     'logs'
                ]
                data = {'values': list(purchases), 'fields': field_names, 'title': 'لیست خرید',}
                return JsonResponse(data=data, status=200)
            else:
                return JsonResponse({'status': 'error', 'message': 'No purchase records found'}, status=404)
        else:
            return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)


@csrf_exempt
def report_RawMaterial(request):
    try:
        if request.method == 'POST':
            filter_type = request.GET.get('filter')
            current_time = timezone.now()

            field_names = [
                 'date',
                 'location',
                 'supplier_name',
                 'material_type',
                 'material_name',
                 'unit',
                 'grade',
                 'status',
                 'receive_date',
                 'last_date',
                 'description',
                 'comments',
                 'shipment_id_id',
                 'qr_code',
                 'username',
                 'logs'
            ]
            field_names = ['unit', 'location', 'supplier_name', 'material_type', 'material_name',]
            # Get all table names from the database
            all_table_names = connection.introspection.table_names()
            anbar_table_names = [name for name in all_table_names if name.startswith('Anbar_')]
            mavad = []
            for anbar_name in anbar_table_names:
                AnbarModel = apps.get_model('myapp', anbar_name)

                if filter_type == 'year':
                    rawMaterial = AnbarModel.objects.filter(receive_date__year=current_time.year, status='In-stock', reel_number__isnull=True, supplier_name__isnull=False)
                elif filter_type == 'month':
                    rawMaterial = AnbarModel.objects.filter(receive_date__month=current_time.month, status='In-stock', reel_number__isnull=True, supplier_name__isnull=False)
                elif filter_type == 'week':
                    start_of_last_week = current_time - timedelta(days=6)
                    end_of_last_week = current_time
                    rawMaterial = AnbarModel.objects.filter(receive_date__range=(start_of_last_week, end_of_last_week), status='In-stock', reel_number__isnull=True, supplier_name__isnull=False)
                elif filter_type == 'day':
                    hours_ago = current_time - timedelta(hours=24)
                    rawMaterial = AnbarModel.objects.filter(receive_date__gte=hours_ago, receive_date__lt=current_time, status='In-stock', reel_number__isnull=True, supplier_name__isnull=False)
                else:
                    return JsonResponse({'status': 'error', 'message': 'Invalid filter type'}, status=400)
                anbar_records = rawMaterial.values(*field_names).annotate(quantity=Count('id')).order_by('location')
                if anbar_records.exists():
                    for raw in anbar_records:
                    #     for field in datetime_fields:
                    #         if field in raw and raw[field] is not None:
                    #             # Convert to Shamsi date
                    #             shamsi_date = jdatetime.datetime.fromgregorian(datetime=raw[field])
                    #             # Update the field in the dictionary
                    #             raw[field] = shamsi_date.strftime('%Y-%m-%d %H:%M')

                        mavad.append(raw)

            if mavad:
                field_names = ['unit', 'location','quantity', 'supplier_name', 'material_type', 'material_name',]
                data = {'values': mavad, 'fields': field_names , 'title': 'لیست مواد اولیه',}
                return JsonResponse(data=data, status=200)
            else:
                return JsonResponse({'status': 'error', 'message': 'No raw material records found'}, status=404)
        else:
            return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)
    except Exception as e:
        print(e)
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)


@csrf_exempt
def report_Products(request):
    try:
        if request.method == 'POST':
            filter_type = request.GET.get('filter')
            current_time = timezone.now()

            if filter_type == 'year':
                products = Products.objects.filter(receive_date__year=current_time.year, status='In-stock').order_by('-width').values()
            elif filter_type == 'month':
                products = Products.objects.filter(receive_date__month=current_time.month, status='In-stock').order_by('-width').values()
            elif filter_type == 'week':
                start_of_last_week = current_time - timedelta(days=6)
                end_of_last_week = current_time
                products = Products.objects.filter(receive_date__range=(start_of_last_week, end_of_last_week), status='In-stock').order_by('-width').values()
            elif filter_type == 'day':
                hours_ago = current_time - timedelta(hours=24)
                products = Products.objects.filter(receive_date__gte=hours_ago, receive_date__lt=current_time, status='In-stock').order_by('-width').values()
            else:
                return JsonResponse({'status': 'error', 'message': 'Invalid filter type'}, status=400)

            if products.exists():
                for product in products:
                    for field in datetime_fields:
                        if field in product and product[field] is not None:
                            # Convert to Shamsi date
                            shamsi_date = jdatetime.datetime.fromgregorian(datetime=product[field])
                            # Update the field in the dictionary
                            product[field] = shamsi_date.strftime('%Y-%m-%d %H:%M')
                # field_names = [k for k in list(products)[0]]
                field_names =[
                     'date',
                     'location',
                     'width',
                     'reel_number',
                     'gsm',
                     'length',
                     'grade',
                     'breaks',
                     'status',
                     'receive_date',
                     'last_date',
                     'comments',
                     'qr_code',
                     'profile_name',
                     'shipment_id_id',
                     'username',
                     'logs'
                 ]

                data = {'values': list(products), 'fields': field_names, 'title': 'لیست محصولات',}
                return JsonResponse(data=data, status=200)
            else:
                return JsonResponse({'status': 'error', 'message': 'No product records found'}, status=404)
        else:
            return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)


@csrf_exempt
def report_Consumption(request):
    try:
        if request.method == 'POST':
            filter_type = request.GET.get('filter')
            current_time = timezone.now()

            if filter_type == 'year':
                consumption = Consumption.objects.filter(receive_date__year=current_time.year).exclude(status='Cancelled').values()
            elif filter_type == 'month':
                consumption = Consumption.objects.filter(receive_date__month=current_time.month).exclude(status='Cancelled').values()
            elif filter_type == 'week':
                start_of_last_week = current_time - timedelta(days=6)
                end_of_last_week = current_time
                consumption = Consumption.objects.filter(receive_date__range=(start_of_last_week, end_of_last_week)).exclude(status='Cancelled').values()
            elif filter_type == 'day':
                hours_ago = current_time - timedelta(hours=24)
                consumption = Consumption.objects.filter(receive_date__gte=hours_ago, receive_date__lt=current_time).exclude(status='Cancelled').values()
            else:
                return JsonResponse({'status': 'error', 'message': 'Invalid filter type'}, status=400)

            if consumption.exists():
                for con in consumption:
                    for field in datetime_fields:
                        if field in con and con[field] is not None:
                            # Convert to Shamsi date
                            shamsi_date = jdatetime.datetime.fromgregorian(datetime=con[field])
                            # Update the field in the dictionary
                            con[field] = shamsi_date.strftime('%Y-%m-%d %H:%M')
                # field_names = [k for k in list(consumption)[0]]
                field_names =[
                     'date',
                     'supplier_name',
                     'status',
                     'location',
                     'receive_date',
                     'shipment_id_id',
                     'material_type',
                     'material_name',
                     'unit',
                     'reel_number',
                     'profile_name',
                     'grade',
                     'comments',
                     'cancelling_reason',
                     'username',
                     'logs'
                ]

                data = {'values': list(consumption), 'fields': field_names, 'title': 'لیست مصرف',}
                return JsonResponse(data=data, status=200)
            else:
                return JsonResponse({'status': 'error', 'message': 'No consumption records found'}, status=404)
        else:
            return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)


@csrf_exempt
def report_Alert(request):
    try:
        if request.method == 'POST':
            filter_type = request.GET.get('filter')
            current_time = timezone.now()

            if filter_type == 'year':
                alert = Alert.objects.filter(date__year=current_time.year).order_by('-id').values()
            elif filter_type == 'month':
                alert = Alert.objects.filter(date__month=current_time.month).order_by('-id').values()
            elif filter_type == 'week':
                start_of_last_week = current_time - timedelta(days=6)
                end_of_last_week = current_time
                alert = Alert.objects.filter(date__range=(start_of_last_week, end_of_last_week)).order_by('-id').values()
            elif filter_type == 'day':
                hours_ago = current_time - timedelta(hours=24)
                alert = Alert.objects.filter(date__gte=hours_ago, date__lt=current_time).order_by('-id').values()
            else:
                return JsonResponse({'status': 'error', 'message': 'Invalid filter type'}, status=400)

            if alert.exists():
                for con in alert:

                    # Convert to Shamsi date
                    shamsi_date = jdatetime.datetime.fromgregorian(datetime=con['date'])
                    # Update the field in the dictionary
                    con['date'] = shamsi_date.strftime('%Y-%m-%d %H:%M')
                field_names = ['date', 'status', 'message']
                data = {'values': list(alert), 'fields': field_names, 'title': 'هشدار ها',}
                return JsonResponse(data=data, status=200)
            else:
                return JsonResponse({'status': 'error', 'message': 'No alert records found'}, status=404)
        else:
            return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)


def all_pages(request):
    if request.method == 'GET':
        return render(request, 'all_pages.html')

@csrf_exempt
def products_page(request):
    try:
        if request.method == 'POST':
            filter_type = request.GET.get('filter')
            current_time = timezone.now()
            # Get all table names from the database
            all_table_names = connection.introspection.table_names()
            anbar_table_names = [name for name in all_table_names if name.startswith('Anbar_')]
            all_results = []

            for anbar_table_name in anbar_table_names:
                model = apps.get_model('myapp', anbar_table_name)

                if filter_type == 'year':
                    products = model.objects.filter(receive_date__year=current_time.year,status='In-stock', width__isnull=False)
                elif filter_type == 'month':
                    products = model.objects.filter(receive_date__month=current_time.month, status='In-stock', width__isnull=False)
                elif filter_type == 'week':
                    start_of_last_week = current_time - timedelta(days=6)
                    end_of_last_week = current_time
                    products = model.objects.filter(receive_date__range=(start_of_last_week, end_of_last_week), status='In-stock', width__isnull=False)
                elif filter_type == 'day':
                    hours_ago = current_time - timedelta(hours=24)
                    products = model.objects.filter(receive_date__gte=hours_ago, receive_date__lt=current_time, status='In-stock', width__isnull=False)
                else:
                    return JsonResponse({'status': 'error', 'message': 'Invalid filter type'}, status=400)

                result = products.values('width', 'location', 'status').annotate(quantity=Count('id')).order_by('-width')
                all_results.extend(result)

            field_names = ['width', 'location', 'quantity', 'status',]
            # Now sort all_results by 'location' and then by 'width'
            # Sorting function
            def sorting_key(d):
                # Handling None as the smallest possible value
                width = d['width'] if d['width'] is not None else float('-inf')
                return (d['location'], width)

            sorted_results = sorted(all_results, key=sorting_key)

            # print(sorted_results)
            # all_results = sorted(all_results, key=lambda x: x['width'])
            data = {'values': sorted_results, 'fields': field_names, 'title': 'لیست محصولات', }
            return JsonResponse(data=data, status=200)
            # Group by 'width', count the number of products in each group, and order by 'location'

            #
            # if products.exists():
            #     # for product in products:
            #     #     for field in datetime_fields:
            #     #         if field in product and product[field] is not None:
            #     #             # Convert to Shamsi date
            #     #             shamsi_date = jdatetime.datetime.fromgregorian(datetime=product[field])
            #     #             # Update the field in the dictionary
            #     #             product[field] = shamsi_date.strftime('%Y-%m-%d %H:%M')
            #     #
            #     field_names =['width','grade', 'location', 'status']
            #
            #     data = {'values': list(products), 'fields': field_names, 'title': 'لیست محصولات',}
            #     return JsonResponse(data=data, status=200)
            # else:
            #     return JsonResponse({'status': 'error', 'message': 'No product records found'}, status=404)
        else:
            return render(request, 'products_page.html')
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
