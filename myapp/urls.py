from django.urls import path
from .views import *
urlpatterns = [
    # Following paths are related to APIs:

    path("api/checkLicenseNumber", check_license_number),
    path("api/addTruck", add_truck),
    path("api/getMaterialTypes", get_materialTypes),
    path("api/getSupplierNames", get_supplierNames),
    path("api/getConsumptionProfileNames", get_consumption_profile_names),
    path("api/getLicenseNumbers", get_license_numbers),
    path("api/getAnbarTableNames", get_anbar_table_names),
    path("api/getMaterialNames", get_material_names),
    path("api/getCustomerNames", get_customer_names),
    path("api/getShipmentLicenseNumbers", get_shipment_license_numbers),
    path("api/getShipmentLicenseNumbersByStatus/<str:status>", get_shipment_license_numbers_by_status),
    path("api/getShipmentLicenseNumbersOutgoingByStatus/<str:status>", get_shipment_license_numbers_outgoing_by_status),
    path("api/getShipmentLicenseNumbersByLocation/<str:location>", get_shipment_license_numbers_by_location),
    path("api/getShipmentDetailsByLicenseNumber", get_shipment_details_by_license_number),
    path("api/getShipmentDetails2ByLicenseNumber", get_shipment_details2_by_license_number),
    path("api/getReelNumbersByWidthAndStatus", get_reel_numbers_by_width_and_status),
    path("api/getWidths", get_widths_view),
    path("api/showWeight1/", show_weight1),
    path("api/getUnitNames", get_unit_names),
    path("api/getUnitNamesBasedOnSupplier", get_unit_names_based_on_supplier),
    path("api/unload", unload),
    path("api/loaded", loaded),
    path("api/used", used),
    path("api/moved", moved),
    path("api/cancelShipment", cancel_shipment),
    path("api/getSupplierNamesBasedAndbar", get_supplierNames_based_andbar),
    path("api/getUnitBasedSupplierName", get_unit_based_supplier_name),
    path("api/getReelNumber", get_reel_number),
    path("api/loadDataForMoved", load_data_for_moved),

    # Following paths are related to Pages:

    path("addCustomer/", add_customer),
    path("addSupplier/", add_supplier),
    path("addMaterialType/", add_material_type),
    path("addUnit/", add_unit),
    path("addRawMaterial/", add_rawMaterial),
    path("addTruck/", add_truck),
    path("addNewAnbar/", add_new_anbar),
    path("addConsumptionProfile/", add_consumption_profile),
    path("addNewReel/", add_new_reel),
    path("addShipment/", add_shipment),
    path("weightStationPanel/", weight_station_panel),
    path("updateWeight1/", update_weight1),
    path("updateWeight2/", update_weight2),
    path("createPurchaseOrder/", create_purchase_order),
    path("createSalesOrder/", create_sales_order),
    path("forkliftPanel/", forklift_panel),

]

