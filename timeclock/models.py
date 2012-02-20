from django.db import models
from django.utils.translation import ugettext as _

# Create your models here.

class ClockPunch(models.Model):
    """an event with a date-timestamp signifying a Worker changing from one Activity to another"""

    timestamp = models.DateTimeField(_('Moment in Time'), blank=False, null=False, auto_now_add=True)
    activity = models.ForeignKey('Activity')
    worker = models.ForeignKey('Worker')

    class Meta:
        ordering = ['timestamp',]

    def __unicode__(self):
        return "%s - %s" % (self.activity, self.timestamp)

    @models.permalink
    def get_absolute_url(self):
        return ('')


class Worker(models.Model):
    """A person that can book time spent on an Activity, or log an Event"""
    
    
    name = models.CharField(_('name'), max_length=50, blank=False, null=False,)
    

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
    
    ticket = models.CharField(_('ticket'), max_length=40, blank=False, null=False)

    description = models.CharField(_('Description'), max_length=120, blank=True, null=True)

    class Meta:
        ordering = ['ticket',]
        verbose_name, verbose_name_plural = "Job", "Jobs"

    def __unicode__(self):
        return "%s - %s" % (self.ticket, self.description)

    @models.permalink
    def get_absolute_url(self):
        return ('')        