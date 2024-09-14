from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django.urls import reverse
from network_objects.models import Product, Supplier


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("pk", "name")


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ("pk", "name", "purveyor_link", "debt", "supplier_level")
    actions = ['clean_debt']
    list_filter = ['city', 'country']

    def purveyor_link(self, obj):
        if obj.purveyor:
            return format_html('<a href="{0}">{1} {2}</a>'.format(
                reverse('admin:network_objects_supplier_change', args=(f'{obj.purveyor.pk}')), obj.purveyor,
                obj.purveyor.pk))
        return obj.purveyor

    def clean_debt(self, request, queryset):
        for supplier in queryset:
            supplier.debt = 0
            supplier.save()
        self.message_user(request, f'Задолженность очищена.')

    clean_debt.short_description = 'Очистить задолженность'

    purveyor_link.short_description = "ссылка на поставщика"
