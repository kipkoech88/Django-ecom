from django.urls import path
from .views import store, cart, checkout

urlpatterns =[
    path('', store, name='store'),
    path('/checkout', checkout, name='checkout'),
    path('/cart', cart, name='cart')
]