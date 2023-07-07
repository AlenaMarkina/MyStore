from django.contrib import admin
from .models import Category, Product, Discount, Wishlist


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Discount)
admin.site.register(Wishlist)
