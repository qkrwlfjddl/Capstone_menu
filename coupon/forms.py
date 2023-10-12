from django import forms

#쿠폰번호를 입력받아서 장바구니에 적용할 수 있도록
class AddCouponForm(forms.Form):
    code = forms.CharField(label='쿠폰 번호')