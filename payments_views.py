from django.shortcuts import get_object_or_404, render
from .models import Payment
from django.http import JsonResponse

def payment_list(request):
    payments = Payment.objects.all()
    data = [{"order_number": payment.order.order_number, "amount": payment.amount} for payment in payments]
    return JsonResponse(data, safe=False)

def payment_detail(request, payment_id):
    payment = get_object_or_404(Payment, id=payment_id)
    data = {
        "order_number": payment.order.order_number,
        "amount": payment.amount,
        "payment_date": payment.payment_date
    }
    return JsonResponse(data)
