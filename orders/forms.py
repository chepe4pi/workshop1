from django import forms

from orders.models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        fields = ['name', 'user', 'value', 'is_delivered']
        model = Order
