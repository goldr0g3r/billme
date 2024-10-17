from django.contrib import admin
from .models import Invoice, Bill, Sale, Product

# Register your models here.


class InvoiceAdmin(admin.ModelAdmin):
    list_display = ("customer_name", "date", "payment_status")
    search_fields = ("customer_name",)
    list_filter = ("payment_status",)


admin.site.register(Invoice, InvoiceAdmin)


class BillAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


admin.site.register(Bill, BillAdmin)


class SaleAdmin(admin.ModelAdmin):
    list_display = ("name", "quantity", "total_price")
    search_fields = ("product_name",)


admin.site.register(Sale, SaleAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price")
    search_fields = ("name",)


admin.site.register(Product, ProductAdmin)
