from django.contrib import admin
from .models import Animal

@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'available', 'created_at')
    list_filter = ('available',)
    search_fields = ('name', 'description')