# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from shop.models import Product
from .forms import AddProductForm
from .cart import Cart
from coupon.forms import AddCouponForm


@require_POST
#골뱅이 함수를 실행 후 다음 함수 실행함
#POST 매소드로만 접속이 가능함 
def add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)

    #클라이언트에서 서버로 데이터를 전달
    #유효성 검사, injection 전처리 해주는 form
    form = AddProductForm(request.POST)
    if form.is_valid(): 
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'], is_update=cd['is_update'])

    return redirect('cart:detail')


def remove(request, product_id): #제품을 카트에서 지움
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id) 
    #제품이 있으면 지우고 없으면 상세페이지로 옮김
    cart.remove(product)

    return redirect('cart:detail')


def detail(request):
    cart = Cart(request)
    add_coupon = AddCouponForm()

    for product in cart:
        product['quantity_form'] = AddProductForm(initial={'quantity': product['quantity'], 'is_update': True})
    return render(request, 'cart/detail.html', {'cart': cart,
                                                'add_coupon':add_coupon})
