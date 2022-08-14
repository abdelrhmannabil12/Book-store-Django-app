from msilib.schema import AdminExecuteSequence
from django.contrib import admin

from .views import register
from .models import *
# Register your models here.
admin.site.register(Customer)
admin.site.register(OrderItem)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title','author','price']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','itemsTotal','orderTotal']
