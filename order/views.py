# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from cart.cart import Cart
from django.views.generic.base import View
from django.http import JsonResponse
from django.contrib.admin.views.decorators import staff_member_required
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

#한 페이지 안에서 get과 post 둘 다 일어날 때 
#입력받은 주소가 똑같지만 매소드가 달라 정보 구분 가능

from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from .models import Order, OrderStatus

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        order = Order()
        if cart.coupon:
            order.coupon = cart.coupon
            order.discount = cart.get_discount_total()
        order.user = request.user
        order.save()
        for item in cart:
            OrderItem.objects.create(order=order,
                                     product=item['product'],
                                     price=item['price'],
                                     quantity=item['quantity']
                                     )
        cart.clear()
        messages.success(request, '주문이 성공적으로 이루어졌습니다.')
        return redirect('order:order_complete', order_id=order.id)
    return render(request, 'order/create.html', {'cart': cart})


# 자바스크립트가 동작하지 않는 환경에서도 주문은 가능해야한다
# 따라서 위에서 order 창이 있어도 아래 order_complete가 필요함
def order_complete(request, order_id):
    order = get_object_or_404(Order, id=order_id)  # order 없으면 404 에러 출력
    return render(request, 'order/complete.html', {'order': order})

@login_required        
def order_history(request):
    orders = Order.objects.filter(user=request.user).order_by('-created')
    
    context = {
       'orders': orders,
    }
    
    return render(request, 'order/order_history.html', {'orders': orders})


"""def change_status(request, order_id, new_status):
    order = Order.objects.get(pk=order_id)
    
    # Check if the status changed from '조리중' to '조리 완료'
    if order.status == '조리중' and new_status == '조리 완료':
        order.status = new_status
        order.save()
        
        # Update the status_changed field in OrderStatus
        order_status = OrderStatus.objects.filter(order=order).latest('timestamp')
        order_status.status_changed = True
        order_status.save()
        
        # Return a JSON response to trigger the popup
        return JsonResponse({'popup': True})
    
    return JsonResponse({'popup': False})

"""
@staff_member_required 
#url에서 order_id로 이름을 받아줘서 변수명을 그렇게 설정함
def admin_order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'order/admin/detail.html', {'order': order})