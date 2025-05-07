from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def invoice_page(request):
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

    return render(request, 'templates/invoice.html')