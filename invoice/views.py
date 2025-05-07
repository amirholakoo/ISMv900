from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.template.loader import render_to_string
from xhtml2pdf import pisa
import io
import json

@csrf_exempt
def invoice_page(request):
    return render(request, 'invoice.html')


@csrf_exempt
def Havaleh(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            total_weight = sum(float(item['weight']) for item in data['items'] if item['weight'])

            context = {
                'date': data.get('date'),
                'serial': data.get('serial'),
                'customer': data.get('customer'),
                'address': data.get('address'),
                'note': data.get('note'),
                'items': data.get('items', []),
                'total_weight': total_weight,
            }

            html = render_to_string("havaleh.html", context)
            result = io.BytesIO()
            pisa_status = pisa.CreatePDF(html, dest=result)
            if pisa_status.err:
                return HttpResponse('خطا در تولید PDF', status=500)
            return HttpResponse(result.getvalue(), content_type='application/pdf')

        except Exception as e:
            return HttpResponse(f"خطای داخلی: {str(e)}", status=500)
    else:
        return HttpResponse("فقط POST پشتیبانی می‌شود.", status=405)
    

@csrf_exempt
def SalesOrder(request):
    return render(request, 'SalesOrder.html')

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
