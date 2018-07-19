# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

class ModelTestCase(TestCase):
    """This class defines the test suite for the order model."""

    def setUp(self):
        """Define the test client and other test variables."""

        self.status = 0
        self.shipping_method = "Mail"
        self.shipping_amount = 27
        self.shipping_currency = "INR"
        self.shipping_address = "address"
        self.order_subtotal = 27
        self.spl_instruction = "Special Instruction"

        self.dummy_order = Order(status=self.status,
                               shipping_method=self.shipping_method,
                               shipping_amount=self.shipping_amount,
                               shipping_currency=self.shipping_currency,
                               shipping_address=self.shipping_address,
                               order_subtotal=self.order_subtotal,
                               spl_instruction=spl_instruction
                               )

    def test_model_can_create_a_order(self):
        """Test the Order model can create a Order."""

        old_count = Order.objects.count()
        self.dummy_order.save()

        new_count = Order.objects.count()
        self.assertNotEqual(old_count, new_count)
