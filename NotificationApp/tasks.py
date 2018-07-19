from __future__ import absolute_import
from celery import shared_task
from NotificationApp.models import *
from OrderManagement.EmailEngine.EmailEngine.CeleryTasks import send_mail
from OrderManagement.SmsEngine.SmsEngine.CeleryTasks import send_sms
from django.forms.models import model_to_dict

@shared_task(name='tasks.NotifyTask')
class NotifyTask:

	def __init__(self,customer, invoice):
		self.customer   = customer
		self.invoice   = invoice
		self.notify()

	def notify(self):
		print "Notifying user"
		obj = NotificationRetry(customer=self.customer, invoice=self.invoice)
		obj.save()
		send_mail.apply_async(args=[obj.id],)
		send_sms.apply_async(args=[obj.id],)

		


