from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import User
from django.http import HttpRequest
from django.urls import reverse
from django.utils.safestring import mark_safe 
from .models import OrderItem, Order, OrderStatus

def order_detail(obj):
    url = reverse('order:admin_order_detail', args=[obj.id])
    html = mark_safe(f"<a href='{url}'>Detail</a>")
    return html
order_detail.short_description = 'Detail'

class OrderItemInline(admin.TabularInline): 
    model = OrderItem
    raw_id_fields = ['product'] 
    
class OrderStatusInline(admin.TabularInline):
    model = OrderStatus
    extra = 1
    
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'order_status', 'product_name', order_detail, 'created', 'updated' ]
    list_filter = ['created', 'updated']
    #order 모델과 foreign 키로 연결되어있는걸 order 등록할 때 같이 등록해줌
    # 다른 모델과 연결되어있는 경우 한 페이지 표시하고 싶을 때
    #foreign 키로 연결되어있는 필드를 같이 편집할 수 있도록 함 
    inlines = [OrderItemInline, OrderStatusInline]

    def product_name(self, obj):
        return ", ".join([item.product.name for item in obj.items.all()])

    def order_status(self, obj):
       return obj.status
    order_status.short_description = '상태'

    actions = ['order_in_progress', 'order_complete']

    def order_in_progress(self, request, queryset):
        queryset.update(status='조리중')
    order_in_progress.short_description = '조리중'

    def order_complete(self, request, queryset):
        queryset.update(status='조리 완료')
    order_complete.short_description = '조리 완료'

admin.site.register(Order, OrderAdmin)
