from django.contrib import admin
from .models import Cake

@admin.register(Cake)
class CakeAdmin(admin.ModelAdmin):
    list_display = ('cakeName', 'cakeFlavour', 'cakeEggOptions')  # You can customize
