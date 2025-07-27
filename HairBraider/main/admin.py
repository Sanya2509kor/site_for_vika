from django.contrib import admin
from .models import Products, ProductImage


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):

    inlines = [ProductImageInline]

    prepopulated_fields = {'slug': ('name', )}
    list_display = ['name', 'color', 'price', 'discount', ]
    list_editable = ['discount', 'color', 'price']
    search_fields = ['name', 'description']
    list_filter = ['discount', 'color']
    fields = [
        "name", 
        "slug", 
        "description",
        "color",
        "image",
        ("price", "discount"),
        'show',
    ]

    ordering = ('-id',)
