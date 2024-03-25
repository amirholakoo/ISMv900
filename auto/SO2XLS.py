import pandas as pd
from .models import Shipments, Sales, Products

def generate_excel_report(filename="monthly_sales_report.xlsx"):
    # Extracting data from models
    shipments_data = Shipments.objects.all().values()
    sales_data = Sales.objects.all().values()
    products_data = Products.objects.all().values()

    # Creating DataFrames
    shipments_df = pd.DataFrame(list(shipments_data))
    sales_df = pd.DataFrame(list(sales_data))
    products_df = pd.DataFrame(list(products_data))

    # Merging sales with shipments data for comprehensive information
    # Assuming 'id' in shipments corresponds to 'shipment_id' in sales
    report_df = pd.merge(sales_df, shipments_df, left_on='shipment_id', right_on='id', suffixes=('_sale', '_shipment'))

    # Merging product details
    # This step assumes there's a straightforward way to associate products with sales, such as through a 'sales_id' in products
    report_df = report_df.merge(products_df, left_on='id_sale', right_on='sales_id', suffixes=('', '_product'))

    # Selecting and renaming columns for clarity
    report_df = report_df[['date_sale', 'customer_name', 'shipment_type', 'status_shipment', 'weight1', 'weight2', 'net_weight', 'price_per_kg', 'total_price', 'vat', 'extra_cost', 'reel_number', 'width', 'gsm', 'length', 'grade']]
    report_df.columns = ['Sale Date', 'Customer Name', 'Shipment Type', 'Shipment Status', 'Weight1 (kg)', 'Weight2 (kg)', 'Net Weight (kg)', 'Price Per KG ($)', 'Total Price ($)', 'VAT ($)', 'Extra Costs ($)', 'Reel Number', 'Width', 'GSM', 'Length', 'Grade']

    # Writing the DataFrame to an Excel file
    report_df.to_excel(filename, index=False, engine='openpyxl')

# Call the function to generate the report
generate_excel_report()
