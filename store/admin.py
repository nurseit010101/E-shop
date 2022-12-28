from django.contrib import admin
from .models import *
# Register your models here.

class Cart_Admin(admin.ModelAdmin):
    list_display = ('id', 'user','product', 'product_qty','created_at')

class OrderAdmin(admin.ModelAdmin):
    search_fields = ('fname',)
    list_display = ('id', 'fname', 'lname', 'email', 'phone', 'address','city','total_price','payment_mode','tracking_no','created_at')

class Contacts_Admin(admin.ModelAdmin):
    list_display = ('id', 'name', 'gmail', 'number', 'message','created_at')

class email_Admin(admin.ModelAdmin):
    list_display = ('id','email','created_at')

class profile_Admin(admin.ModelAdmin):
    list_display = ('id', 'user', 'phone', 'address', 'city', 'state', 'created_at')

class product_Admin(admin.ModelAdmin):
    list_display = ('id', 'category', 'name', 'sender_name', 'size_of_product', 'quantity','original_price','selling_price','trending', 'created_at')

class report_Admin(admin.ModelAdmin):
    list_display = ('id','report_per_day','report_per_week','report_per_month','report_per_season','report_per_year','created_at')

admin.site.register(Category)
admin.site.register(Product,product_Admin)
admin.site.register(Cart,Cart_Admin)
admin.site.register(Order,OrderAdmin)
admin.site.register(OrderItem)
admin.site.register(Profile,profile_Admin)
admin.site.register(Advertisement)
admin.site.register(news_email,email_Admin)
admin.site.register(Contacts, Contacts_Admin)
admin.site.register(ForAdmin, report_Admin)
