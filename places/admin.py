from django.contrib import admin
from .models import Place, Image
from django.utils.html import format_html
from adminsortable2.admin import SortableStackedInline, SortableAdminBase


class StackedInlineImage(SortableStackedInline):
    model = Image
    fields = ['images', 'get_preview', 'order']
    readonly_fields = ['get_preview']

    def get_preview(self, obj):
        if obj.images:
            return format_html(f"<img src='{obj.images.url}', height=200px />")


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [StackedInlineImage]
