# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render_to_response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from orders.forms import OrderForm
from orders.models import Order
from orders.serializers import OrderSerializer


def index(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
    form = OrderForm()
    orders = Order.objects.all()
    return render_to_response('index.html', {'orders': orders, 'form': form})


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('category',)
