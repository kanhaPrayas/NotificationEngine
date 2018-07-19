# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Order

# Register your models here.


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
	pass
