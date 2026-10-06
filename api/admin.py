from django.contrib import admin
from django.utils.html import format_html

from .models import Category, Product, ProductImage


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    fields = ('image', 'file')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image_preview')
    search_fields = ('name',)
    ordering = ('name',)

    @admin.display(description='Image')
    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="60" height="60" style="object-fit: cover; border-radius: 6px;" />',
                obj.image.url,
            )
        return '-'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'price')
    list_filter = ('category',)
    search_fields = ('name', 'description')
    ordering = ('-id',)
    inlines = (ProductImageInline,)


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'image_preview', 'file')
    list_filter = ('product',)
    search_fields = ('product__name',)
    ordering = ('-id',)

    @admin.display(description='Product')
    def product_name(self, obj):
        return obj.product.name if obj.product else '-'

    @admin.display(description='Image')
    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="60" height="60" style="object-fit: cover; border-radius: 6px;" />',
                obj.image.url,
            )
        return '-'