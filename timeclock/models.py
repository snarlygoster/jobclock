from django.db import models
from django.forms import ModelForm
from django.utils.translation import ugettext as _
from django.forms.widgets import RadioSelect
# Create your models here.


class Worker(models.Model):
    """A person that can book time spent on an Activity, or log an Event"""
    
    
    name = models.CharField(_('name'), max_length=50, unique=True, blank=False, null=False,)
    

    class Meta:
        ordering = ['name',]
        verbose_name, verbose_name_plural = "Worker", "Workers"

    def __unicode__(self):
        return "%s" % (self.name)

    @models.permalink
    def get_absolute_url(self):
        return ('')


class Activity(models.Model):
    """Bucket to log work time against"""
    
    ticket = models.CharField(_('ticket'), max_length=40, unique=True, blank=False, null=False)

    description = models.CharField(_('Description'), max_length=120, blank=True, null=True)

    class Meta:
        ordering = ['ticket',]
        verbose_name, verbose_name_plural = "Job", "Jobs"

    def __unicode__(self):
        return "%s" % (self.ticket)

    @models.permalink
    def get_absolute_url(self):
        return ('')        

class ClockPunch(models.Model):
    """an event with a date-timestamp signifying a Worker changing from one Activity to another"""

    timestamp = models.DateTimeField(_('Moment in Time'), blank=False, null=False, auto_now_add=True)
    activity = models.ForeignKey(Activity)
    worker = models.ForeignKey(Worker)

    class Meta:
        ordering = ['-timestamp',]

    def __unicode__(self):
        return "%s punched %s at %s" % (self.worker, self.activity, self.timestamp)

    @models.permalink
    def get_absolute_url(self):
        return ('')


class ClockPunchForm(ModelForm):

    class Meta:
        model = ClockPunch
        fields = ('worker', 'activity')
        widgets = {'worker': RadioSelect, 'activity': RadioSelect }

      