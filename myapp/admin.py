from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Truck)
class TruckAdmin(admin.ModelAdmin):

    list_display = ('license_number', 'driver_name', 'phone', 'status', 'location')

    search_fields = ('license_number', 'driver_name')

    list_filter = ('status', 'location')

    ordering = ['-license_number']


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):

    list_display = ('customer_name', 'address', 'phone', 'status')

    search_fields = ('customer_name', 'phone')

    list_filter = ('status',)


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):

    list_display = ('supplier_name', 'address', 'phone', 'status')

    search_fields = ('supplier_name', 'phone')

    list_filter = ('status',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = ('reel_number', 'width', 'gsm', 'length', 'grade', 'status')

    search_fields = ('reel_number', 'grade')

    list_filter = ('status', 'grade')

@admin.register(RawMaterial)
class RawMaterialAdmin(admin.ModelAdmin):

    list_display = ('material_name', 'supplier', 'material_type', 'status')

    search_fields = ('material_name', 'material_type')

    list_filter = ('status', 'material_type')


@admin.register(Purchases)
class PurchasesAdmin(admin.ModelAdmin):

    list_display = ('MaterialID', 'SupplierID', 'TruckID', 'Quantity', 'Status')

    search_fields = ('MaterialID__material_name', 'SupplierID__supplier_name')

    list_filter = ('Status',)


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):

    list_display = ('customer', 'truck', 'date', 'total_price')

    search_fields = ('customer__customer_name', 'truck__license_number')

    list_filter = ('customer', 'truck')



# Consider registering other models like AnbarSangin, AnbarSalonTolid, etc., in a similar fashion.
