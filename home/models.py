from django.db import models
from django.contrib.auth.models import User

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('PREPARING', 'Preparing'),
        ('READY', 'Ready'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled')
    ]

    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Orders')
    total_amount = models.decimalField(max_digits=10, decimal_places=2, default=0)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.pk} by {self.customer.username}"

    def update_total(self):
        self.total_amount = sum(item.menu.item.price * item.quantity for item in self.items.all())
        self.save()

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.menu_item.name}"