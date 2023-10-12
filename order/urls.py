from django.urls import path
from .views import *
from . import views

app_name = 'order'

urlpatterns = [
    path('create/', order_create, name='order_create'),
    path('complete/', order_complete, name='order_complete'),
    path('complete/<int:order_id>/', order_complete, name='order_complete'),
    path('admin/order/<int:order_id>/', admin_order_detail, name='admin_order_detail'),
    path('history/', views.order_history, name='order_history'),
    
]