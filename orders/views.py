# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render_to_response

from orders.models import Order


def index(request):
    orders = Order.objects.all()
    return render_to_response('index.html', {'orders': orders})
