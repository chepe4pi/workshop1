# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


class Order(models.Model):
    name = models.CharField(max_length=127)
    user = models.ForeignKey(User)
    value = models.IntegerField()
    is_delivered = models.BooleanField(default=False)
