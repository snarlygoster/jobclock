# python lib
import datetime

# django lib
from django.db import models
from django.forms import ModelForm
from django.utils.translation import ugettext as _
# from django.forms.widgets import RadioSelect
from django.contrib.localflavor.us.models import PhoneNumberField
from django.contrib.localflavor.us.forms import USPhoneNumberField

# third party lib
# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Submit

from timeclock.models import Activity

class Customer(models.Model):
  """Customer: contact information for a Customer"""

  name = models.CharField(_('name'), max_length=255, blank=False, null=False, help_text="what should we call you?")
  email = models.EmailField()
  telephone = PhoneNumberField()

  class Meta:
    ordering = ['name',]

  def __unicode__(self):
    return "%s" % (self.name)

  @models.permalink
  def get_absolute_url(self):
    return ('')

class CustomerForm(ModelForm):
  telephone = USPhoneNumberField()

  class Meta:
    model = Customer

class WorkOrderItem(models.Model):
  """WorkOrderItem: quantity, materials, stamping text and locations etc. for job_complete"""

  number = models.PositiveIntegerField(blank=True, null=True)
  notes = models.TextField(blank=True)
  ticket = models.ForeignKey(Activity)

  class Meta:
    ordering = ['number',]
    #verbose_name, verbose_name_plural = "Work Order Item", "Work Order Items"

  def __unicode__(self):
    return "%s" % (self.type)

  @models.permalink
  def get_absolute_url(self):
    return ('')

class WorkOrder(models.Model):
  """WorkOrder: traces a customer's initial inquiry for work to the jobs completion .

    customer fills in estimate questionnaire,
      provides email address, system returns ticket number
      no email/contact info, system discards
    new estimate ticket shows in job management list as "estimate request"
    work manager reviews job with customer,
      job is accepted and queued for clockpunch
      estimate is closed (no job).
    job collects clock punches until complete.
    work manager marks job as complete, system moves job data to next report and archive.

    """

  creation_date = models.DateTimeField(_('creation date'), blank=True, null=True, auto_now_add=True)
  customer = models.ForeignKey(Customer)

  class Meta:
    ordering = ['creation_date',]
    verbose_name, verbose_name_plural = "Work Orders", "Work Orders"

  def __unicode__(self):
    return "%s" % (self.ticket)

  @models.permalink
  def get_absolute_url(self):
    return ('')