from django.shortcuts import get_object_or_404, render
from .models import Order
from django.http import JsonResponse

def order_list(request):
    orders = Order.objects.all()
    data = [{"order_number": order.order_number, "customer_name": order.customer_name} for order in orders]
    return JsonResponse(data, safe=False)

def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    data = {
        "order_number": order.order_number,
        "customer_name": order.customer_name,
        "created_at": order.created_at
    }
    return JsonResponse(data)
