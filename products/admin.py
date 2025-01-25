from django.contrib import admin
from . import models

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'cost_price', 'selling_price')
    search_fields = ('title',)