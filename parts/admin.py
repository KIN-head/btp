
from django.contrib import admin
from .models import Order, Category, Product, OrderItem

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'slug', 'price', 'stock', 'created', 'updated']
    list_filter = ['category', 'created', 'updated']
    list_editable = ['price', 'stock']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Product, ProductAdmin)

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'owner', 'paid',
                    'created', 'updated']
    list_filter = ['owner', 'paid', 'created', 'updated']
    inlines = [OrderItemInline]

admin.site.register(Order, OrderAdmin)
