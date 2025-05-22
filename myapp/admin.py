from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Truck)
class TruckAdmin(admin.ModelAdmin):

    list_display = ('id', 'license_number', 'driver_name', 'phone', 'status', 'location', 'username', 'logs')

    search_fields = ('license_number', 'driver_name')

    list_filter = ('status', 'location')

    ordering = ['-license_number']


@admin.register(Shipments)
class ShipmentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'shipment_type', 'status', 'location', 'license_number', 'receive_date', 'entry_time', 'customer_name', 'supplier_name', 'weight1', 'weight1_time', 'unload_location', 'unit', 'quantity', 'quality', 'penalty', 'weight2', 'weight2_time', 'net_weight', 'list_of_reels', 'profile_name', 'sales_id', 'price_per_kg', 'extra_cost', 'material_type', 'material_name', 'purchase_id', 'vat', 'invoice_status', 'payment_status', 'exit_time', 'document_info', 'comments', 'cancellation_reason', 'username', 'logs')
    search_fields = ('id', 'shipment_type', 'status', 'location', 'license_number', 'customer_name', 'supplier_name', 'username')
    list_filter = ('shipment_type', 'status', 'location')


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):

    list_display = ('supplier_name', 'address', 'phone', 'status', 'comments', 'username', 'logs')

    search_fields = ('supplier_name', 'phone')

    list_filter = ('status',)


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):

    list_display = ('reel_number', 'width', 'gsm', 'length', 'grade', 'breaks', 'comments', 'location', 'status', 'receive_date', 'last_date', 'profile_name', 'username', 'logs','qr_code')

    search_fields = ('reel_number', 'grade')

    list_filter = ('status', 'grade')


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):

    list_display = ('customer_name', 'address', 'phone', 'status', 'comments', 'username', 'logs')

    search_fields = ('customer_name', 'phone')

    list_filter = ('status',)



@admin.register(RawMaterial)
class RawMaterialAdmin(admin.ModelAdmin):

    list_display = ('material_name', 'supplier_name', 'material_type', 'status', 'description', 'comments', 'username', 'logs')

    search_fields = ('supplier_name', 'material_name', 'material_type')

    list_filter = ('status', 'material_type')
    fields = ('material_name', 'supplier_name', 'material_type', 'status', 'description', 'comments', 'username', 'logs')

@admin.register(Purchases)
class PurchasesAdmin(admin.ModelAdmin):

    list_display = ('date', 'receive_date', 'material_type', 'material_name','supplier_name', 'unit', 'quantity', 'quality', 'penalty', 'weight1', 'weight2', 'net_weight', 'price_per_kg', 'vat', 'total_price', 'extra_cost', 'invoice_status', 'status', 'payment_details', 'payment_date', 'invoice_number', 'document_info', 'comments', 'cancellation_reason', 'shipment_id', 'username', 'logs',)

    search_fields = ('material_name', 'supplier_id')

    list_filter = ('date', 'receive_date', 'material_type', 'material_name','supplier_name', 'unit', 'quantity', 'quality', 'penalty', 'weight1', 'weight2', 'net_weight', 'price_per_kg', 'vat', 'total_price', 'extra_cost', 'invoice_status', 'status', 'payment_details', 'payment_date', 'invoice_number', 'document_info', 'comments', 'cancellation_reason', 'shipment_id', 'username', 'logs',)


@admin.register(Sales)
class SaleAdmin(admin.ModelAdmin):

    list_display = ('date','customer_name','license_number','list_of_reels','profile_name','weight1','weight2','net_weight','price_per_kg','vat','total_price','extra_cost','invoice_status','invoice_number','status','payment_details','payment_date','document_info','comments','cancellation_reason','shipment','username','logs')

    list_filter = ('customer_name', 'license_number')



anbar_fields = ('receive_date', 'reel_number', 'supplier_name', 'material_type', 'material_name', 'description' ,'status', 'location', 'last_date', 'width', 'gsm', 'length', 'grade', 'breaks', 'comments', 'qr_code', 'unit', 'profile_name', 'username', 'logs',)
@admin.register(Anbar_Sangin)
class AnbarSanginAdmin(admin.ModelAdmin):

    # Specify the fields to display in the list view
    list_display = anbar_fields
    # Specify the fields to use in the search box
    search_fields = ('material_name', 'reel_number')
    # Specify the fields to use in the filter sidebar
    list_filter = ('status', 'location')
    # Specify the fields to display in the detail view
    fields = anbar_fields


@admin.register(Anbar_Salon_Tolid)
class AnbarSalonTolidAdmin(admin.ModelAdmin):
    # Specify the fields to display in the list view
    list_display = anbar_fields
    # Specify the fields to use in the search box
    search_fields = ('material_name', 'reel_number')
    # Specify the fields to use in the filter sidebar
    list_filter = ('status', 'location')
    # Specify the fields to display in the detail view
    fields = anbar_fields


@admin.register(Anbar_Parvandeh)
class AnbarParvandehAdmin(admin.ModelAdmin):
    # Specify the fields to display in the list view
    list_display = anbar_fields
    # Specify the fields to use in the search box
    search_fields = ('material_name', 'reel_number')
    # Specify the fields to use in the filter sidebar
    list_filter = ('status', 'location')
    # Specify the fields to display in the detail view
    fields = anbar_fields


@admin.register(Anbar_Koochak)
class AnbarKoochakAdmin(admin.ModelAdmin):
    # Specify the fields to display in the list view
    list_display = anbar_fields
    # Specify the fields to use in the search box
    search_fields = ('material_name', 'reel_number')
    # Specify the fields to use in the filter sidebar
    list_filter = ('status', 'location')
    # Specify the fields to display in the detail view
    fields = anbar_fields


@admin.register(Anbar_Khamir_Ghadim)
class AnbarKhamirGhadimAdmin(admin.ModelAdmin):
    # Specify the fields to display in the list view
    list_display = anbar_fields
    # Specify the fields to use in the search box
    search_fields = ('material_name', 'reel_number')
    # Specify the fields to use in the filter sidebar
    list_filter = ('status', 'location')
    # Specify the fields to display in the detail view
    fields = anbar_fields


@admin.register(Anbar_Khamir_Kordan)
class AnbarKhamirKordanAdmin(admin.ModelAdmin):
    # Specify the fields to display in the list view
    list_display = anbar_fields
    # Specify the fields to use in the search box
    search_fields = ('material_name', 'reel_number')
    # Specify the fields to use in the filter sidebar
    list_filter = ('status', 'location')
    # Specify the fields to display in the detail view
    fields = anbar_fields


@admin.register(Anbar_Muhvateh_Kardan)
class AnbarMuhvatehKardanAdmin(admin.ModelAdmin):
    # Specify the fields to display in the list view
    list_display = anbar_fields
    # Specify the fields to use in the search box
    search_fields = ('material_name', 'reel_number')
    # Specify the fields to use in the filter sidebar
    list_filter = ('status', 'location')
    # Specify the fields to display in the detail view
    fields = anbar_fields


@admin.register(Anbar_Akhal)
class AnbarAkhalAdmin(admin.ModelAdmin):
    # Specify the fields to display in the list view
    list_display = anbar_fields
    # Specify the fields to use in the search box
    search_fields = ('material_name', 'reel_number')
    # Specify the fields to use in the filter sidebar
    list_filter = ('status', 'location')
    # Specify the fields to display in the detail view
    fields = anbar_fields


@admin.register(Consumption)
class ConsumptionAdmin(admin.ModelAdmin):
    # Specify the fields to display in the list view
    list_display = ('supplier_name', 'material_type', 'material_name', 'unit', 'reel_number', 'profile_name', 'status', 'username')
    # Specify the fields to use in the search box
    search_fields = ('supplier_name', 'material_type', 'material_name')
    # Specify the fields to use in the filter sidebar
    list_filter = ('status', 'supplier_name', 'material_type')
    # Specify the fields to display in the detail view
    fields = ('receive_date', 'supplier_id', 'supplier_name', 'material_type', 'material_name', 'unit', 'reel_number', 'profile_name', 'comments', 'status', 'username', 'logs')


@admin.register(ConsumptionProfile)
class ConsumptionProfileAdmin(admin.ModelAdmin):
    list_display =['profile_name','supplier_name','material_type','material_name','unit','quantity']
    fields=list_display


@admin.register(MaterialType)
class MaterialTypeAdmin(admin.ModelAdmin):
    # Specify the fields to display in the list view
    list_display = ('supplier_name', 'material_type', 'username', 'status', 'date', 'logs',)
    # Specify the fields to use in the search box
    search_fields = ('supplier_name', 'material_type', 'username')
    # Specify the fields to use in the filter sidebar
    list_filter = ('supplier_name', 'material_type')
    # Specify the fields to display in the detail view
    fields = ('supplier_name', 'material_type', 'username', 'status', 'date', 'logs',)


@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    # Specify the fields to display in the list view
    list_display = ('supplier_name', 'material_type', 'unit_name', 'count', 'username', 'date', 'logs')
    # Specify the fields to use in the search box
    search_fields = ('supplier_name', 'material_type', 'unit_name', 'username')
    # Specify the fields to use in the filter sidebar
    list_filter = ('material_type',)
    # Specify the fields to display in the detail view
    fields = ('supplier_name', 'material_type', 'unit_name', 'count', 'username', 'date', 'logs')

