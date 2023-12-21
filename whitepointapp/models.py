from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class ServiceType(models.TextChoices):
    MASSAGE = 'Massage', _('Massage')
    WAXING = 'Waxing', _('Waxing')
    SKINCARE = 'Skincare', _('Skincare')

class RequestAppointment(models.Model):
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    email_address = models.CharField(max_length=50, blank=False, default='')
    phone_number = models.CharField(max_length=50, blank=False, default='') 
    service = models.CharField(max_length=50, choices=ServiceType.choices, default='')
    date = models.CharField(max_length=50, blank=False, default='')
    time = models.CharField(max_length=50, blank=False, default='')

class MessageType(models.TextChoices):
    MASSAGE = 'Massage', _('Massage')
    WAXING = 'Waxing', _('Waxing')
    SKINCARE = 'Skincare', _('Skincare')
    OTHER = 'Other', _('Other')

class MessageRequest(models.Model):
    full_name = models.CharField(max_length=80, null=False, blank=False)
    email_address = models.CharField(max_length=50, blank=False, default='')
    phone_number = models.CharField(max_length=50, blank=False, default='')
    service = models.CharField(max_length=50, choices=MessageType.choices, default='')
    text_content = models.TextField(max_length=200, null=False, blank=False)