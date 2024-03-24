import pandas as pd
from .models import Purchases, Shipments

def generate_purchase_order_excel(purchase_id, filename="purchase_order.xlsx"):
    # Fetch the purchase and associated shipment details
    purchase = Purchases.objects.get(id=purchase_id)
    shipment = Shipments.objects.get(id=purchase.shipment_id) if purchase.shipment_id else None

    # Create a DataFrame for purchase information
    purchase_info_dict = {
        "Purchase ID": [purchase.id],
        "Date": [purchase.date.strftime('%Y-%m-%d')],
        "Supplier": [purchase.supplier_name],
        "Material Type": [purchase.material_type],
        "Material Name": [purchase.material_name],
        "Quality": [purchase.quality],
        "Penalty": [purchase.penalty],
        "Comments": [purchase.comments],
        "Logs": [purchase.logs]
    }

    if shipment:
        purchase_info_dict["Shipment Logs"] = [shipment.logs]

    purchase_info_df = pd.DataFrame(purchase_info_dict)

    # Create a DataFrame for financial summary
    financial_data = {
        "Description": ["Weight1 (kg)", "Weight2 (kg)", "Net Weight (kg)", "Quantity", "Price Per Unit ($)", "Subtotal ($)", "VAT ($)", "Extra Costs ($)", "TOTAL ($)"],
        "Amount": [
            purchase.weight1, purchase.weight2, purchase.net_weight, purchase.quantity,
            purchase.price_per_kg, purchase.total_price, purchase.vat,
            shipment.extra_cost if shipment else 0,
            purchase.total_price + purchase.vat + (shipment.extra_cost if shipment else 0)
        ]
    }
    financial_summary_df = pd.DataFrame(financial_data)

    # Save to Excel
    with pd.ExcelWriter(filename, engine='openpyxl') as writer:
        purchase_info_df.to_excel(writer, sheet_name='Purchase Info', index=False)
        financial_summary_df.to_excel(writer, sheet_name='Financial Summary', index=False)

# To generate the Excel, call this function with the actual purchase ID
# generate_purchase_order_excel(actual_purchase_id, "actual_purchase_order.xlsx")
