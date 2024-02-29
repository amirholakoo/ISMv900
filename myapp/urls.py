from django.urls import path
from .views import *

urlpatterns = [
    # path("api/<str:api>", apiHandler),
    path("api/checkLicenseNumber", check_license_number),
    path("api/addTruck", add_truck),
    path("api/addSupplier", add_supplier),
    path("api/addCustomer", add_customer),
    path("api/getMaterialTypes", get_materialTypes),
    path("api/getSupplierNames", get_supplierNames),
    path("api/addRawMaterial", add_rawMaterial),
    path("api/getConsumptionProfileNames", get_consumption_profile_names),
    path("api/addNewReel", add_new_reel),
    path("api/getLicenseNumbers", get_license_numbers),
    path("api/getMaterialNames", get_material_names),
    path("api/addShipment", add_shipment),
    path("api/updateWeight1", update_weight1),
    path("api/updateWeight2", update_weight2),
    path("api/createPurchaseOrder", create_purchase_order),
    path("api/createSalesOrder", create_sales_order),
    path("api/unload", unload),
    path("api/loaded", loaded),
    path("api/used", used),
]
