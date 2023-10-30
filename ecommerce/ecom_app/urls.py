from . import views
from django.urls import path
from .views import Detail, Pay, SearchResultView, add_to_cart, cart, home,remove_from_cart

urlpatterns=[
    path('',home.as_view(),name='home'),
    path('detail/<int:pk>/',Detail.as_view(),name='detail'),
    path('buy/<int:pk>/',Pay.as_view(),name='buy'),
    path('search/',SearchResultView.as_view(),name='search'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
  
    path('remove_from_cart/<int:product_id>',views.remove_from_cart,name='remove_from_cart'),
    path('cart/',cart,name='mycart',),
]