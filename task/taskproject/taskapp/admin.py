from django.contrib import admin

from .models import orders


# Register your models here.

class ordersAdmin(admin.ModelAdmin):
    list_display = ('name','description')

admin.site.register(orders,ordersAdmin,)