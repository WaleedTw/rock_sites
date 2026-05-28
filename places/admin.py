from django.contrib import admin
from .models import Place, PlaceImage


class PlaceImageInline(admin.TabularInline):
    model = PlaceImage
    extra = 1
    fields = ['image', 'caption_ar', 'caption_en', 'order']
    ordering = ['order']


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ['order', 'name_en', 'name_ar', 'region_en', 'created_at']
    search_fields = ['name_en', 'name_ar', 'region_en', 'region_ar']
    inlines = [PlaceImageInline]
    ordering = ['order']

    fields = [
        'order',
        'name_ar', 'name_en',
        'region_ar', 'region_en',
        'description_ar', 'description_en',
        'distance_info_ar', 'distance_info_en',
        'latitude', 'longitude',
        'main_image',
        'slug',
    ]