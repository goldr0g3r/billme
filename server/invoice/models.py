from django.db import models
import uuid


# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    user = models.ForeignKey("authentication.User", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey("authentication.User", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Sale(models.Model):
    name = models.CharField(max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    @property
    def total_sales_amount(self):
        return self.product.price * self.quantity

    def __str__(self):
        return self.name


class Bill(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=255)
    items = models.ManyToManyField(Sale)
    user = models.ForeignKey("authentication.User", on_delete=models.CASCADE)

    @property
    def total_amount(self):
        return sum(item.price * item.quantity for item in self.items.all())

    def __str__(self):
        return self.name


class Invoice(models.Model):
    PAYMENT_STATUS_CHOICES = [
        ("P", "Paid"),
        ("U", "Unpaid"),
        ("O", "Overdue"),
        ("PP", "Partially Paid"),
    ]

    customer_name = models.ForeignKey(Client, on_delete=models.CASCADE)
    date = models.DateField()
    bills = models.ManyToManyField(Bill)
    sales = models.ManyToManyField(Sale)
    payment_status = models.CharField(max_length=2, choices=PAYMENT_STATUS_CHOICES)
    user = models.ForeignKey("authentication.User", on_delete=models.CASCADE)

    def __str__(self):
        return f"Invoice {self.id} for {self.customer_name}"
