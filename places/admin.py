from django.contrib import admin
from .models import Place, Image
from adminsortable2.admin import SortableStackedInline, SortableAdminBase
from django.utils.html import format_html
from django.utils.safestring import mark_safe


class StackedInlineImage(SortableStackedInline):
    model = Image
    fields = ['image', 'get_preview', 'order']
    readonly_fields = ['get_preview']

    def get_preview(self, obj):
        if obj.image:
            return format_html(
                "<img src='{}' style='max-height:200px; max-width:300px' />",
                mark_safe(obj.image.url)
                )


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    raw_id_fields = ['place']


@admin.register(Place)
class SortablePlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [StackedInlineImage]
