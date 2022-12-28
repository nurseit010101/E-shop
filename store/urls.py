from django.urls import path
from .views import *
from store.controller import authview, cart, wishlist,checkout , order


urlpatterns = [
    path('', home, name="home"),
    path('collections', collections, name="collections"),
    path("collections/<str:slug>", collectionsview, name="collectionsview"),
    path("collections/<str:cate_slug>/<str:prod_slug>", productview, name="productview"),

    path("product-list",productlistAjax, name="productlistAjax"),
    path("searchproduct", searchproduct, name="searchproduct"),
    path("about_us", about_us, name="about_us"),
    path("questions", questions, name="questions"),
    path("orderss", orderss, name="orderss"),
    path("news", news, name="news"),
    path("partner", partner, name="partner"),
    path("contacts", contacts, name="contacts"),
    path('message/', message, name='message'),
    path('email_news/', email_news, name='email_news'),
    path('advertisers/', advertisers, name='advertisers'),
    path('investors/', investors, name='investors'),
    path('suppliers/', suppliers, name='suppliers'),
    path('delivery/', delivery, name='delivery'),
    path('sposob/', sposob, name='sposob'),
    path('video/', video, name='video'),
    path('vozvrat/', vozvrat, name='vozvrat'),

    path("register/",authview.register, name="register"),
    path("Login/",authview.loginpage, name="loginpage"),
    path("logout/",authview.logoutpage, name="logoutpage"),
    path("admin_person/",authview.admin_person, name="admin_person"),

    path("add-to-cart", cart.addtocart, name="addtocart"),
    path("cart/", cart.viewcart, name="cart"),
    path("update-cart", cart.updatecart, name="updatecart"),
    path("delete-cart-item", cart.deletedpage, name="deletedpage"),


    path("wishlist",wishlist.index, name="wishlist"),
    path("add-to-wishlist", wishlist.addToWishlist, name="addToWishlist"),
    path("delete-wishlist-item", wishlist.deletewishlistitem, name="deletewishlistitem"),


    path("checkout", checkout.index, name="checkout"),
    path("place-order", checkout.placeorder, name="placeorder"),


    path("my-orders", order.index, name="myorder"),
    path("view-order/<str:t_no>", order.vieworder, name="orderview"),


]