from django.shortcuts import render, redirect
from .models import *
from .forms import CustomerForm, SupplierForm
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

