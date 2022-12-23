from django.contrib import admin
from .models import *
# Register your models here.



class OrderAdmin(admin.ModelAdmin):
    search_fields = ('fname',)

class Contacts_Admin(admin.ModelAdmin):
    list_display = ('id', 'name', 'gmail', 'number', 'message')

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Order,OrderAdmin)
admin.site.register(OrderItem)
admin.site.register(Profile)
admin.site.register(Advertisement)
admin.site.register(Contacts, Contacts_Admin)
