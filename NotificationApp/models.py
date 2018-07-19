# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.exceptions import ValidationError
from django.db import models
from OrderApi.utils import tele_match

class NotificationRetry(models.Model):
    """This class represents the OrderLine model."""
    customer = models.TextField(null=True, Blank=True)
    invoice =models.TextField(null=True, Blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    mail_sent = models.BooleanField(default=true)
    sms_sent = models.BooleanField(default=true)


    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.customer)


