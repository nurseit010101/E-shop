from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
# Create your views here.
from django.http.response import JsonResponse
from django.http import HttpResponseRedirect
from datetime import datetime, timedelta



def home(request):
    trending_products = Product.objects.filter(trending = 1)
    usual_products = Product.objects.filter(trending = 0)
    advertisement = Advertisement.objects.all()[:3]
    advertisement_last = Advertisement.objects.last()

    month_report = Order.objects.filter(created_at__lte = datetime.now()-timedelta(days=30))
    year_report = Order.objects.filter(created_at__lte = datetime.now()-timedelta(days=365))
    week_report = Order.objects.filter(created_at__lte = datetime.now()-timedelta(days=7))
    day_report = Order.objects.filter(created_at__lte = datetime.now()-timedelta(days=1))
    seasons_report = Order.objects.filter(created_at__lte = datetime.now()-timedelta(days=90))
    profit_per_month = []
    profit_per_year = []
    profit_per_season = []
    profit_per_week = []
    profit_per_day = []
    for q in month_report:
        profit_per_month.append(q.total_price)
        # profit_per_day.append(w.total_price)
    print(profit_per_month)
    # send = ForAdmin()
    # send.report_per_day = sum(profit_per_day)
    # send.profit_per_year = sum(profit_per_year)
    # send.profit_per_season = sum(profit_per_season)
    # send.profit_per_week = sum(profit_per_week)
    # send.profit_per_month = sum(profit_per_month)
    # send.save()

    context = {'trending_products':trending_products,'advertisement': advertisement,
        'advertisement_last': advertisement_last,'usual_products':usual_products,}
    return render(request, 'index.html', context)





def collections(request):
    category = Category.objects.filter(status=0)
    context = {'category': category}
    return render(request, 'store/collections.html', context)


def collectionsview(request, slug):
    if (Category.objects.filter(slug=slug, status=0)):
        products = Product.objects.filter(category__slug=slug)
        category = Category.objects.filter(slug=slug).first()
        context = {'products': products, 'category': category}
        return render(request, 'store/products/index.html', context)
    else:
        messages.warning(request, "Такой категории не найдено")
        return redirect('collections')


def productview(request, cate_slug, prod_slug):
    if (Category.objects.filter(slug=cate_slug, status=0)):
        if (Product.objects.filter(slug=prod_slug, status=0)):
            products = Product.objects.filter(slug=prod_slug, status=0).first
            context = {'products':products}
        else:
            messages.error(request, "Такой товар не найден")
            return redirect('collections')

    else:
        messages.error(request, "No such category found")
        return redirect('collections')
    return render(request, "store/products/view.html", context)



def productlistAjax(request):
    products = Product.objects.filter(status=0).values_list('name', flat=True)
    productslist = list(products)

    return JsonResponse(productslist, safe = False)

def searchproduct(request):
    if request.method == 'POST':
        searchedterm = request.POST.get('productsearch')
        if searchedterm == "":
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            product = Product.objects.filter(name__contains=searchedterm).first()

            if product:
                return redirect('collections/'+product.category.slug+'/'+product.slug)
            else:
                messages.info(request, "Ни один продукт не соответствует вашему запросу")
                return redirect(request.META.get('HTTP_REFERER'))




    return redirect(request.META.get('HTTP_REFERER'))

def about_us(request):
    return render(request, "store/about_us.html")

def questions(request):
    return render(request, "store/questions.html")

def orderss(request):
    return render(request, "store/for_clients/order.html")

def news(request):
    return render(request, "store/news.html")

def partner(request):
    return render(request, "store/bussiness/partner.html")

def advertisers(request):
    return render(request, "store/bussiness/advertisers.html")

def investors(request):
    return render(request, "store/bussiness/investors.html")

def suppliers(request):
    return render(request, "store/bussiness/suppliers.html")

def delivery(request):
    return render(request, "store/for_clients/delivery.html")

def sposob(request):
    return render(request, "store/for_clients/sposob.html")

def video(request):
    return render(request, "store/for_clients/video.html")

def vozvrat(request):
    return render(request, "store/for_clients/vozvrat.html")

def contacts(request):
    return render(request, "store/contacts.html")


def message(request):
    if request.method == 'POST':
        send=Contacts()
        send.name=request.POST.get('name')
        send.gmail=request.POST.get('gmail')
        send.number=request.POST.get('number')
        send.message=request.POST.get('message')
        send.save()
        return HttpResponseRedirect('/')

def email_news(request):
    if request.method == 'POST':
        send=news_email()
        send.email=request.POST.get('search')
        send.save()
        return HttpResponseRedirect('/')