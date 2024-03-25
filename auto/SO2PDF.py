from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from .models import Sales, Shipments, Products

def generate_sales_order_pdf(sale_id, filename="sales_order.pdf"):
    # Fetch sale, shipment, and product data
    sale = Sales.objects.get(id=sale_id)
    shipment = Shipments.objects.get(id=sale.shipment_id)
    products = Products.objects.filter(reel_number__in=sale.list_of_reels.split(','))

    doc = SimpleDocTemplate(filename, pagesize=letter)
    story = []
    styles = getSampleStyleSheet()

    # Add Title, Sale, and Shipment Information (omitted for brevity)
    # Title
    title = Paragraph("Sales Order - Internal Record", styles['Title'])
    story.append(title)
    story.append(Spacer(1, 12))

    # Sale and Shipment Information
    sale_info_section = Paragraph("<b>Sale and Shipment Information</b>", styles['Heading2'])
    story.append(sale_info_section)

    sale_shipment_info = Paragraph(
        f"<b>Sales Order ID:</b> {sale_data['sale']['id']}<br/>"
        f"<b>Date:</b> {sale_data['sale']['date']}<br/>"
        f"<b>Customer:</b> {sale_data['sale']['customer']['name']}<br/>"
        f"<b>Shipment Type:</b> {sale_data['shipment']['type']}<br/>"
        f"<b>Status:</b> {sale_data['shipment']['status']}<br/>"
        f"<b>Location:</b> {sale_data['shipment']['location']}<br/>"
        f"<b>Logs:</b> {sale_data['shipment']['logs']}", styles['Normal'])
    story.append(sale_shipment_info)
    story.append(Spacer(1, 12))

    # Product Details
    products_section = Paragraph("<b>Product Details</b>", styles['Heading2'])
    story.append(products_section)

    product_data = [['Reel Number', 'Width', 'GSM', 'Length', 'Grade', 'Price Per KG']]
    product_data += [[product['reel_number'], product['width'], product['gsm'], product['length'], product['grade'], product['price_per_kg']] for product in sale_data['products']]
    
    product_table = Table(product_data)
    product_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.darkblue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.lightblue),
    ]))
    story.append(product_table)
    story.append(Spacer(1, 12))

    # Financial Summary in a Table Format
    financial_info_section = Paragraph("<b>Financial Summary</b>", styles['Heading2'])
    story.append(financial_info_section)

    subtotal = sale.total_price
    vat = sale.vat
    extra_costs = shipment.extra_cost
    total = subtotal + vat + extra_costs

    financial_data = [
        ["Weight1 (kg)", "Weight2 (kg)", "Net Weight (kg)", "Price Per KG ($)", "Subtotal ($)"],
        [shipment.weight1, shipment.weight2, shipment.net_weight, sale.price_per_kg, subtotal],
        ["VAT ($)", "", "", "", vat],
        ["Extra Costs ($)", "", "", "", extra_costs],
        ["TOTAL ($)", "", "", "", total]
    ]

    financial_table = Table(financial_data, colWidths=[80, 80, 80, 80, 180])
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
