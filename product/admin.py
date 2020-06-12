from django.contrib import admin

# Register your models here.
from . models import Category, Product, Brand, ProductImages

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Brand)
admin.site.register(ProductImages)