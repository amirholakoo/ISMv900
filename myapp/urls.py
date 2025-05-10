from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

from invoice.views import *

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
    path("api/getUnitNamesBasedOnLicenseOfShipment", get_unit_names_based_on_license_of_shipment),
    path("api/getWidths", get_widths_view),
    path("api/showWeight1/", show_weight1),
    path("api/getUnitNames", get_unit_names),
    path("api/getUnitNamesBasedOnSupplier", get_unit_names_based_on_supplier),
    path("api/unload", unload),
    path("api/loaded", loaded),
    path("api/used", used),
    path("api/moved", moved),
    path("api/retuned", retuned),
    path("api/getSupplierNamesBasedAndbar", get_supplierNames_based_andbar),
    path("api/getUnitAndMaterialNameBasedSupplierNmaeAndbar", get_unit_and_materialName_based_supplierNmae_andbar),
    path("api/getUnitBasedSupplierName", get_unit_based_supplier_name),
    path("api/getReelNumber", get_reel_number),
    path("api/loadDataForMoved", load_data_for_moved),
    path("api/getSupplierNamesBasedConsumtioon", get_supplierNames_based_consumtioon),
    path("api/getUnitAndMaterialNameBasedSupplierNmaeConsumption", get_unit_and_materialName_based_supplierNmae_consumption),
    path("api/loadShipmentsBaesdLicenseNumberForCanceling", load_shipments_baesd_license_number_for_canceling),
    path("api/loadReportData", loadReportData),
    path("api/generateExcelReport", generate_excel_report),
    path("api/generateQrCode", generate_qrCode),
    path("api/reportShipment", report_shipment),
    path("api/reportSales", report_Sales),
    path("api/reportPurchases", report_Purchases),
    path("api/reportRawMaterial", report_RawMaterial),
    path("api/reportProducts", report_Products),
    path("api/reportConsumption", report_Consumption),
    path("api/reportAlert", report_Alert),
    path("api/generate-purchase-order-pdf/", generate_purchase_order_pdf),
    path("ProductsPage/", products_page),

    # Following paths are related to Pages:

    path("", all_pages),
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
    path("cancel/", cancel),
    path("report/", report_page),

    
    path("api/havaleh-pdf/", havaleh, name='havaleh-pdf'),
    

    path("invoice/", invoice_page),
    path("invoice/havaleh", havaleh),
    path("api/sales-order-pdf/", sales_order, name='sales-order-pdf'),
    path("invoice/sales-order", sales_order),
    path("invoice/Purchases/", Purchases),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

