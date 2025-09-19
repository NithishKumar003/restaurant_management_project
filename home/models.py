from django.db import models
from django.contrib.auth.models import User

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.CharField(max_length=50)
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='menu_images/', blank=True, null=True)

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

    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.pk} by {self.customer.username}"

    def update_total(self):
        self.total_amount = sum(item.menu_item.price * item.quantity for item in self.items.all())
        self.save()

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Order"
        verbose_name_plural = "Orders"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.menu_item.name}"
    
    def get_total_price(self):
        return self.menu_item.price * self.quantity

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.order.update_total()

class ContactSubmission(models.Model):
    name = models.CharField(max_length=100)
    email  = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.email})"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return f"Profile Of {self.user.username}"   

class RestaurantLocation(models.Model):
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.address}, {self.city}, {self.state} - {self.zip_code}"

class RestaurantInfo(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    location = models.OneToOneField(
        RestaurantLocation, on_delete=models.CASCADE, related_name="restaurant_info"
    )
    image = models.ImageField(upload_to"restaurant/", blank=True, null=True)

    def __str__(self):
        return self.name

class Feedback(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    feedback_text = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback from {self.name or 'Anonymous'} on {self.created_at.strftime('%Y-%m-%d')}"


class Special(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class OpeningHour(models.Model):
    day = models.CharField(max_length=20)
    open_time = models.TimeField()
    close_time = models.TimeField()

    def __str__(self):
        return f"{self.day}: {self.open_time} - {self.close_time}"

class About(models.Model):
    description = models.TextField()

    def __str__(self):
        return "About Us Information"

class Chef(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    image = models.ImageField(upload_to='chef_images/')

    def __str__(self):
        return self.name