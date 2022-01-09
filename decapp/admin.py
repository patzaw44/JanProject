from django.contrib import admin
from .models import Car, Rate

# admin.site.register(Car)
# admin.site.register(Rate)


@admin.register(Car)
class AutoAdmin(admin.ModelAdmin):
    list_display = ['make', 'model']
    list_filter = ['make', 'model']
    search_fields = ['make', 'model']


@admin.register(Rate)
class RateAdmin(admin.ModelAdmin):
    list_display = ['id', 'car_id', 'rating']
    list_filter = ['car_id', 'rating']
    search_fields = ['car', 'rating']
