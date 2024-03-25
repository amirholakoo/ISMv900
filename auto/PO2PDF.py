from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from .models import Purchases, Shipments

def generate_purchase_order_pdf(purchase_id, filename="purchase_order.pdf"):
    # Fetch purchase and shipment data
    purchase = Purchases.objects.get(id=purchase_id)
    shipment = Shipments.objects.get(id=purchase.shipment_id) if purchase.shipment_id else None

    doc = SimpleDocTemplate(filename, pagesize=letter)
    story = []
    styles = getSampleStyleSheet()

    # Title
    title = Paragraph("Purchase Order", styles['Title'])
    story.append(title)
    story.append(Spacer(1, 12))

    # Purchase Information
    purchase_info_section = Paragraph("<b>Purchase Information</b>", styles['Heading2'])
    story.append(purchase_info_section)

    purchase_details = f"""
    <b>Purchase ID:</b> {purchase.id}<br/>
    <b>Date:</b> {purchase.date.strftime('%Y-%m-%d')}<br/>
    <b>Supplier:</b> {purchase.supplier_name}<br/>
    <b>Material Type:</b> {purchase.material_type}<br/>
    <b>Material Name:</b> {purchase.material_name}<br/>
    <b>Quality:</b> {purchase.quality}<br/>
    <b>Penalty:</b> {purchase.penalty}<br/>
    <b>Comments:</b> {purchase.comments}<br/>
    <b>Logs:</b> {purchase.logs}
    """
    if shipment:
        purchase_details += f"<br/><b>Shipment Logs:</b> {shipment.logs}"

    purchase_info = Paragraph(purchase_details, styles['Normal'])
    story.append(purchase_info)
    story.append(Spacer(1, 12))

    # Financial Summary
    financial_info_section = Paragraph("<b>Financial Summary</b>", styles['Heading2'])
    story.append(financial_info_section)

    subtotal = purchase.total_price
    vat = purchase.vat
    extra_costs = purchase.extra_cost if purchase.extra_cost else 0
    total = subtotal + vat + extra_costs

    financial_data = [
        ["Weight1 (kg)", "Weight2 (kg)", "Net Weight (kg)", "Quantity", "Price Per Unit ($)", "Subtotal ($)"],
        [purchase.weight1, purchase.weight2, purchase.net_weight, purchase.quantity, purchase.price_per_kg, subtotal],
        ["VAT ($)", "", "", "", "", vat],
        ["Extra Costs ($)", "", "", "", "", extra_costs],
        ["TOTAL ($)", "", "", "", "", total]
    ]

    financial_table = Table(financial_data, colWidths=[70, 70, 70, 70, 70, 100])
    financial_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.darkblue),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -2), colors.lightgrey),
        ('BACKGROUND', (0, 4), (-1, 4), colors.lightblue),
        ('GRID', (0,0), (-1,-1), 1, colors.black),
        ('SPAN', (1, 2), (3, 2)),  # Merge cells for VAT
        ('SPAN', (1, 3), (3, 3)),  # Merge cells for Extra Costs
        ('SPAN', (1, 4), (3, 4)),  # Merge cells for TOTAL
    ]))
    story.append(financial_table)

    doc.build(story)

# To generate the PDF, call this function with the actual purchase ID
# generate_purchase_order_pdf(actual_purchase_id, "actual_purchase_order.pdf")
