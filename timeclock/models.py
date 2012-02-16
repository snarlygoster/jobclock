from django.db import models

# Create your models here.

class ClockPunch(models.Model):
    """an event with a date-timestamp signifying a Worker changing from one Activity to another"""

    timestamp = models.DateTimeField(_('Moment in Time'), blank=False, null=False, auto_now_add=True)

    worker = models.ForeignKey('Worker')

    class Meta:
        ordering = ['timestamp',]

    def __unicode__(self):
        return "%s" % (self.timestamp)

    @models.permalink
    def get_absolute_url(self):
        return ('')


class Worker(models.Model):
    """A person that can book time spent on an Activity, or log an Event"""


    class Meta:
        ordering = ['name',]
        verbose_name, verbose_name_plural = "Worker", "Workers"

    def __unicode__(self):
        return "%s" % (self.name)

    @models.permalink
    def get_absolute_url(self):
        return ('')