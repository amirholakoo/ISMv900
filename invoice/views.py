from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from xhtml2pdf import pisa
import io
import json


from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string
from weasyprint import HTML
import tempfile
import json
from datetime import datetime
import jdatetime  # Install with: pip install jdatetime

from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string
from weasyprint import HTML
import tempfile
import json
import jdatetime

import base64

from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string
from django.contrib.staticfiles import finders  # Add this import
from weasyprint import HTML
import tempfile
import json
import os
from django.conf import settings

@csrf_exempt
def invoice_page(request):
    return render(request, 'invoice.html')


@csrf_exempt
def havaleh(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            
            # Convert the current UTC time to Jalali
            current_time = datetime(2025, 5, 8, 13, 23, 21)  # Your provided timestamp
            jalali_datetime = jdatetime.datetime.fromgregorian(datetime=current_time)
            persian_date = jalali_datetime.strftime('%Y/%m/%d')  # Format as YYYY/MM/DD in Persian
            
            # Calculate total weight
            total_weight = 0
            for item in data.get('items', []):
                try:
                    total_weight += float(item.get('weight', 0))
                except (ValueError, TypeError):
                    pass

            context = {
                'date': persian_date,  # Use the Persian date here
                'serial': data.get('serial', ''),
                'items': data.get('items', []),
                'total_weight': f"{total_weight:,.0f}",
                'note': data.get('note', ''),
            }

            # Generate HTML
            html_string = render_to_string('havaleh.html', context)
            
            # Create PDF using WeasyPrint with base_url for static files
            html = HTML(string=html_string, base_url=request.build_absolute_uri('/'))
            pdf = html.write_pdf()
            
            # Return the PDF
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename=havaleh_{data.get("serial", "")}.pdf'
            return response

        except Exception as e:
            print(f"Error: {str(e)}")  # For debugging
            return JsonResponse({
                'error': f'Server Error: {str(e)}',
                'status': 'error'
            }, status=500)

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string
from weasyprint import HTML
import json
from datetime import datetime
import jdatetime

@csrf_exempt
def sales_order(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            current_time = datetime.now()
            jalali_datetime = jdatetime.datetime.fromgregorian(datetime=current_time)
            persian_date = jalali_datetime.strftime('%Y/%m/%d')
            total_amount = 0
            items = []
            for item in data.get('items', []):
                quantity = float(item.get('quantity', 0))
                price = float(item.get('price', 0))
                total = quantity * price
                items.append({
                    'description': item.get('description', ''),
                    'quantity': quantity,
                    'price': price,
                    'total': total
                })
                total_amount += total
            context = {
                'date': persian_date,
                'serial': data.get('serial', ''),
                'customer': data.get('customer', ''),
                'economic_code': data.get('economic_code', ''),
                'national_id': data.get('national_id', ''),
                'items': items,
                'total_amount': f"{total_amount:,.0f}",
                'note': data.get('note', ''),
            }
            html_string = render_to_string('sales_order.html', context)
            html = HTML(string=html_string, base_url=request.build_absolute_uri('/'))
            pdf = html.write_pdf()
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename=sales_order_{data.get("serial", "")}.pdf'
            return response
        except Exception as e:
            return JsonResponse({'error': f'Server Error: {str(e)}', 'status': 'error'}, status=500)

@csrf_exempt
def Purchases(request):
    if request.method == 'POST':

        items = []
        
        goods_codes = request.POST.getlist('goods_code')
        goods_comments_list = request.POST.getlist('goods_comments')
        goods_counts = request.POST.getlist('goods_count')
        units = request.POST.getlist('unit')
        unit_prices = request.POST.getlist('unit_price')

        total_price = 0
        total_taxes = 0

        for i in range(len(goods_codes)):
            try:
                count = int(goods_counts[i])
                price = float(unit_prices[i])
                subtotal = count * price
                tax = subtotal * 0.1
                total = subtotal + tax

                item = {
                    'goods_code': goods_codes[i],
                    'goods_comments': goods_comments_list[i],
                    'goods_count': count,
                    'unit': units[i],
                    'unit_price': price,
                    'subtotal': subtotal,
                    'tax': tax,
                    'total': total
                }

                items.append(item)
                total_price += subtotal
                total_taxes += tax
            except (ValueError, IndexError):
                continue  # Skip invalid input rows

        grand_total = total_price + total_taxes

        context = {
            'items': items,
            'total_price': total_price,
            'total_taxes': total_taxes,
            'grand_total': grand_total,
        }

    return render(request, 'Purchases.html')

@csrf_exempt
def generate_purchase_order_pdf(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            
            context = {
                'row': data.get('row', ''),
                'product_name': data.get('product_name', ''),
                'grammage': data.get('grammage', ''),
                'paper_width': data.get('paper_width', ''),
                'buyer_name': data.get('buyer_name', ''),
                'quantity': data.get('quantity', ''),
                'product_weight': data.get('product_weight', ''),
                'notes': data.get('notes', ''),
                'total': data.get('total', ''),
                'accounting': data.get('accounting', ''),
                'warehouse': data.get('warehouse', ''),
                'sales_manager': data.get('sales_manager', ''),
                'factory_manager': data.get('factory_manager', ''),
                'receiver': data.get('receiver', ''),
                'end_statement': data.get('end_statement', '')
            }

            html = render_to_string("purchaseorder.html", context)
            result = io.BytesIO()
            pisa_status = pisa.CreatePDF(html, dest=result)
            
            if pisa_status.err:
                return HttpResponse('خطا در تولید PDF', status=500)
                
            return HttpResponse(result.getvalue(), content_type='application/pdf')

        except Exception as e:
            return HttpResponse(f"خطای داخلی: {str(e)}", status=500)
    else:
        return HttpResponse("فقط POST پشتیبانی می‌شود.", status=405)
