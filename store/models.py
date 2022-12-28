from django.db import models
import datetime
import os

from django.contrib.auth.models import User
# Create your models here.

def get_file_path(request, filename):
    original_filename = filename
    nowTime = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (nowTime, original_filename)
    return os.path.join('uploads/', filename)



class Category(models.Model):
    slug = models.CharField(max_length=150, null=False, blank=False,verbose_name='Слаг')
    name = models.CharField(max_length=150, null=False, blank=False,verbose_name='Имя Категории')
    image = models.ImageField(upload_to=get_file_path, null=True, blank=True,verbose_name='Изображение Категории ')
    description = models.TextField(max_length=500, null=False, blank=False,verbose_name='Описание Категории ')
    status = models.BooleanField(default=False, help_text="0=default, 1=Hidden",verbose_name='Статус Категории ')
    trending = models.BooleanField(default=False, help_text="0=default, 1=trending",verbose_name='В тренде')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='Время')


    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category,  on_delete=models.CASCADE,verbose_name='Категория')
    slug = models.CharField(max_length=150, null=False, blank=False,verbose_name='Слаг')
    name = models.CharField(max_length=150, null=False, blank=False,verbose_name='Имя товара')  
    sender_name = models.CharField(max_length=150, null=False, blank=False,verbose_name='Отправитель товара')  
    product_image = models.ImageField(upload_to=get_file_path, null=True, blank=True,verbose_name='Изображение продукта')
    small_description = models.CharField(max_length=250, null=False, blank=False,verbose_name='Небольшое описание')
    size_of_product = models.CharField(max_length=150, null=False, blank=False,verbose_name='Размер товара ')  
    quantity = models.IntegerField(null=False, blank=False,verbose_name='Количество')
    description = models.TextField(max_length=500, null=False, blank=False,verbose_name='Описание')
    original_price = models.FloatField(null=False, blank=False,verbose_name='Первоначальная цена')
    selling_price = models.FloatField(null=False, blank=False,verbose_name='Цена продажи')
    status = models.BooleanField(default=False, help_text="0=default, 1=Hidden",verbose_name='Статус')
    trending = models.BooleanField(default=False, help_text="0=default, 1=trending",verbose_name='В тренде')
    tag = models.CharField(max_length=150, null=False, blank=False,verbose_name='Тег')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='Дат добавление')


    def __str__(self):
        return self.name



class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='Пользователь')
    product = models.ForeignKey(Product, on_delete=models.CASCADE,verbose_name='Товар')
    product_qty = models.IntegerField(null=False, blank=False,verbose_name='Количество продукта')
    created_at = models.DateField(auto_now_add=True,verbose_name='Время')




class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='Пользователь')
    product = models.ForeignKey(Product, on_delete=models.CASCADE,verbose_name='Товар')
    created_at = models.DateField(auto_now_add=True,verbose_name='Время')



class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='Пользователь')
    fname = models.CharField( max_length=150, null=False,verbose_name='Имя')
    lname = models.CharField( max_length=150, null=False,verbose_name='Фамилия')
    email = models.CharField( max_length=150, null=False,verbose_name='Электронная почта')
    phone = models.CharField( max_length=150, null=False,verbose_name='Телефон номер')
    address = models.TextField(null=False,verbose_name='Адрес')
    city = models.CharField( max_length=150, null=False,verbose_name='Город')
    state = models.CharField( max_length=150, null=False,verbose_name='Область')
    country = models.CharField( max_length=150, null=False,verbose_name='Страна')
    pincode = models.CharField( max_length=150, null=False,verbose_name='Зип код')
    total_price = models.FloatField(null=False,verbose_name='Итоговая цена')
    payment_mode = models.CharField(max_length=150, null=False,verbose_name='Режим оплаты')
    payment_id = models.CharField(max_length=250, null=True,verbose_name='идентификатор платежа')
    orderstatuses = (
        ('Pending','Pending'),
        ('Out For Shipping', 'Out For Shipping'),
        ('Completed', 'Completed'),
    )
    status = models.CharField(max_length=150, choices=orderstatuses, default='Pending',verbose_name='Статус')
    message = models.TextField(null=True,verbose_name='Сообщение')
    tracking_no = models.CharField(null=True, max_length=150,verbose_name='Номер отслеживания')
    created_at = models.DateField(auto_now_add=True,verbose_name='Время')
    updated_at = models.DateField(auto_now=True,verbose_name='Время')

    def __str__(self):
        return '{} - {}'.format(self.id, self.tracking_no)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE,verbose_name='Заказ')
    product = models.ForeignKey(Product, on_delete=models.CASCADE,verbose_name='Товар')
    price = models.FloatField(null=False,verbose_name='Цена')
    quantity =  models.IntegerField(null=False,verbose_name='Количество')

    def __str__(self):
        return '{} - {}'.format(self.order.id, self.order.tracking_no)
    


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,verbose_name='Пользователь')
    phone = models.CharField( max_length=150, null=False,verbose_name='Телефон номер')
    address = models.TextField(null=False,verbose_name='Адрес')
    city = models.CharField( max_length=150, null=False,verbose_name='Город')
    state = models.CharField( max_length=150, null=False,verbose_name='Область')
    country = models.CharField( max_length=150, null=False, verbose_name='Страна')
    pincode = models.CharField( max_length=150, null=False,verbose_name='Зип код')
    created_at = models.DateField(auto_now_add=True,verbose_name='Время')

    def __str__(self):
        return self.user.username
        


class Advertisement(models.Model):
    name = models.CharField(verbose_name='Name', max_length=150, blank=False)
    image = models.ImageField(verbose_name='Image', upload_to='advertisement/')
    created_at = models.DateTimeField(verbose_name='Date', auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'advertisement_product'


class Contacts(models.Model):
    name = models.CharField(max_length=150, verbose_name='Имя',null=False)
    gmail = models.CharField(max_length=150, verbose_name='Е-мейл',null=False)
    number = models.CharField(max_length=150, verbose_name='Телефон',null=False)
    message = models.CharField(max_length=150, verbose_name='Сообщение',null=False)
    created_at = models.DateTimeField(verbose_name='Date', auto_now=True, auto_now_add=False)




class news_email(models.Model):
    email = models.CharField(max_length=150, verbose_name='Е-мейл',null=False)
    created_at = models.DateField(auto_now_add=True,verbose_name='Время')


class ForAdmin(models.Model):
    report_per_day = models.CharField(null=False, max_length=150, verbose_name='Прибыль за один день') 
    report_per_week = models.CharField(null=False, max_length=150, verbose_name='Прибыль за одну неделю') 
    report_per_month = models.CharField(null=False, max_length=150, verbose_name='Прибыль за один месяц') 
    report_per_season = models.CharField(null=False, max_length=150, verbose_name='Прибыль за один сезон') 
    report_per_year = models.CharField(null=False, max_length=150, verbose_name='Прибыль за один год') 
    created_at = models.DateField(auto_now_add=True,verbose_name='Время')
