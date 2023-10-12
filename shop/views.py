from django.shortcuts import render, get_object_or_404
from .models import *
from cart.forms import AddProductForm
from allauth.account.signals import user_signed_up
from django.dispatch import receiver

# Create your views here.
def waiting(product):
    return Product.objects.filter(order_products__order__status='조리중',
                                  name=product.name).annotate(total=Count('order_products'))
    
def waiting_time(item):
    return item['people_total'] * 5
    
def product_in_category(request, category_slug=None):
    current_category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available_display=True)
    
    if category_slug:
        current_category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=current_category)
    
    waiting_people = []
     
    for product in products:
        people = waiting(product)
        
        if people:
            people_total = people[0].total
        else:
            people_total = 0
        
        waiting_people.append({'product': product, 'people_total': people_total})
        
    for item in waiting_people:
        item['waiting_time'] = waiting_time(item)

    return render(request, 'shop/list.html', {'current_category': current_category,
                                              'categories': categories,
                                              'products': products,
                                              'waiting_people': waiting_people,
                                              'waiting_time' : waiting_time})
    
    
def product_detail(request, id, product_slug=None):
    product = get_object_or_404(Product, id=id, slug=product_slug)
    add_to_cart = AddProductForm(initial={'quantity': 1})
    return render(request, 'shop/detail.html', {'product': product,
                                                'add_to_cart':add_to_cart})


