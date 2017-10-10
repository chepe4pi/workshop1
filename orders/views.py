# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render_to_response

from orders.forms import OrderForm
from orders.models import Order


def index(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
    form = OrderForm()
    orders = Order.objects.all()
    return render_to_response('index.html', {'orders': orders, 'form': form})
