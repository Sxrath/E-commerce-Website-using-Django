
from decimal import Decimal
from django.db.models.query import QuerySet,Q 
from django.shortcuts import get_object_or_404, render,redirect
from django.views.generic import ListView,DetailView
from .models import Products, Cart, CartItems
from django.contrib.auth.decorators import login_required

from .models import Cart, CartItems, Products
# Create your views here.
class home(ListView):
    model=Products
    template_name='home.html'

class Detail(DetailView):
    model=Products
    context_object_name='home'
    template_name='detail_view.html'

class Pay(DetailView):
    model=Products
    context_object_name='detail'
    template_name='buy.html'


class SearchResultView(ListView):
    model=Products
    template_name='search.html'
    context_object_name='home'

    def get_queryset(self):
        query=self.request.GET.get('q')
        return Products.objects.filter(Q(title=query)|Q(category=query))


@login_required
def cart(request):
    cart_qs = Cart.objects.filter(user=request.user)
    if cart_qs.exists():
        cart_obj = cart_qs.first()
        cart_items = CartItems.objects.filter(cart=cart_obj)
    else:
        cart_obj = None
        cart_items = []

    context = {
        'cart': cart_obj,
        'cart_items': cart_items
        
    }

    return render(request, 'cart/mycart.html', context)

   
@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Products, id=product_id)
    cart_qs = Cart.objects.filter(user=request.user)
    
    if cart_qs.exists():
        cart_obj = cart_qs.first()
    else:
        cart_obj, created = Cart.objects.get_or_create(user=request.user, total_price=Decimal('0.00'))
    
    cart_item, created = CartItems.objects.get_or_create(product=product, cart=cart_obj)
    
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    
    cart_obj.total_price += Decimal(str(product.price))
    cart_obj.save()
    
    return redirect('mycart')

    
def remove_from_cart(request,product_id):
    product=get_object_or_404(Products,id=product_id)
    cart_qs = Cart.objects.filter(user=request.user)
    if cart_qs.exists():
        cart_obj=cart_qs.first()
        cart_item_qs=CartItems.objects.filter(product=product, cart=cart_obj)
        if cart_item_qs.exists():
            cart_item=cart_item_qs.first()
            if cart_item.quantity>1:
                cart_item.quantity -= 1
                cart_item.save()
            else:
                cart_item.delete()
            cart_obj.total_price -= Decimal(str(product.price))
            cart_obj.save()

            return redirect('mycart')











































































































































