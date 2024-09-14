from django.db import models

class Order(models.Model):
    order_number = models.CharField(max_length=20)
    customer_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.order_number} by {self.customer_name}"
