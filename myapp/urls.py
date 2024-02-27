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
]
