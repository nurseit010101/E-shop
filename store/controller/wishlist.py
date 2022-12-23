from django.shortcuts import render, redirect
from django.contrib import messages
from django.http.response import JsonResponse
from store.models import Wishlist, Product
from django.contrib.auth.decorators import login_required


@login_required(login_url='loginpage')
def index(request):
    wishlist = Wishlist.objects.filter(user=request.user)
    context = {'wishlist':wishlist}
    return render(request,'store/wishlist.html', context)

def addToWishlist(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            prod_id = int(request.POST.get('product_id'))
            product_check = Product.objects.get(id=prod_id)
            if(product_check):
                if(Wishlist.objects.filter(user=request.user,product_id=prod_id)):
                    return JsonResponse({'status':"Товар уже в списке желаний"})
                else:
                    Wishlist.objects.create(user=request.user,product_id=prod_id)
                    return JsonResponse({'status':"Товар добавлен в список желаний"})

            else:
                return JsonResponse({'status':"Такой товар не найден"})

        else:
            return JsonResponse({'status':"Войдите, чтобы продолжить"})

    return redirect('/')


def deletewishlistitem(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            prod_id = int(request.POST.get('product_id'))

            if(Wishlist.objects.filter(user=request.user,product_id=prod_id)):
                wishlistitem = Wishlist.objects.get(product_id=prod_id)
                wishlistitem.delete()
                return JsonResponse({'status':"Товар удален из списка желаний"})
            else:
                return JsonResponse({'status':"Товар не найден"})

        else:
            return JsonResponse({'status':"Войдите, чтобы продолжить"})
    return redirect('/')