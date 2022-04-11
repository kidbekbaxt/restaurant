from django.contrib import admin
from .models import Restaurant,Menu


@admin.register(Restaurant)
class RestaurantAdminModel(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(Menu)
class MenuAdminModel(admin.ModelAdmin):
        list_display = ['id', 'name']
