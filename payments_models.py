from django.db import models
from orders.models import Order

class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)  # Відносини між посилкою і оплатою
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment of {self.amount} for order {self.order.order_number}"
