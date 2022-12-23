from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
# Create your views here.
from django.http.response import JsonResponse
from django.http import HttpResponseRedirect

def home(request):
    trending_products = Product.objects.filter(trending = 1)
    advertisement = Advertisement.objects.all()[:3]
    advertisement_last = Advertisement.objects.last()
    context = {'trending_products':trending_products,'advertisement': advertisement,
        'advertisement_last': advertisement_last,}

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
        messages.warning(request, "No such category found")
        return redirect('collections')


def productview(request, cate_slug, prod_slug):
    if (Category.objects.filter(slug=cate_slug, status=0)):
        if (Product.objects.filter(slug=prod_slug, status=0)):
            products = Product.objects.filter(slug=prod_slug, status=0).first
            context = {'products':products}
        else:
            messages.error(request, "No such product found")
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
                messages.info(request, "No product matched your search")
                return redirect(request.META.get('HTTP_REFERER'))




    return redirect(request.META.get('HTTP_REFERER'))

def about_us(request):
    return render(request, "store/about_us.html")

def questions(request):
    return render(request, "store/questions.html")

def orderss(request):
    return render(request, "store/order.html")

def news(request):
    return render(request, "store/news.html")

def partner(request):
    return render(request, "store/partner.html")

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