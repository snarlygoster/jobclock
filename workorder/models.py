# python lib
import datetime

# django lib
from django.db import models
from django.forms import ModelForm
from django.utils.translation import ugettext as _
from django.forms.widgets import RadioSelect
from django.contrib.localflavor.us.models import PhoneNumberField
from django.contrib.localflavor.us.forms import USPhoneNumberField

# third party lib
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


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

JOB_TYPE_CHOICES = (
  ('t1', 'type 1'),
  ('t2', 'type 2'),
  ('t3', 'type 3'),
)

class CustomerForm(ModelForm):
    telephone = USPhoneNumberField()

    class Meta:
        model = Customer

class JobDetails(models.Model):
    """JobDetails: quantity, materials, stamping text and locations etc. for job_complete"""

    number = models.PositiveIntegerField(blank=True, null=True)
    type = models.CharField(blank=False, max_length=255, choices=JOB_TYPE_CHOICES)
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ['type',]
        #verbose_name, verbose_name_plural = "Job details", "Job details"

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

    initiation_date = models.DateTimeField(_('initiation date'), blank=True, null=True, auto_now_add=True)
    ticket = models.ForeignKey(Activity)
    customer = models.ForeignKey(Customer)
    details = models.ForeignKey(JobDetails)

    class Meta:
        ordering = ['initiation_date',]
        verbose_name, verbose_name_plural = "Work Orders", "Work Orders"

    def __unicode__(self):
        return "%s" % (self.ticket)

    @models.permalink
    def get_absolute_url(self):
        return ('')