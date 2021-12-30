from django.contrib import admin
from .models import Auto, NewRate

# admin.site.register(Auto)
admin.site.register(NewRate)

@admin.register(Auto)
class AutoAdmin(admin.ModelAdmin):
    list_display = ['make', 'model']
    list_filter = ['make', 'model']
    search_fields = ['make', 'model']
