# python lib
import datetime
from collections import defaultdict

# django lib
from django.db import models
from django.forms import ModelForm
from django.utils.translation import ugettext as _
from django.forms.widgets import RadioSelect

# third party lib
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

#####
##### Application Models
#####
class Worker(models.Model):
    """A person that can book time spent on an Activity, or log an Event"""

    name = models.CharField(_('name'), max_length=50, unique=True, blank=False, null=False,)
    can_work = models.BooleanField(default=True)

    class Meta:
        ordering = ['name',]
        verbose_name, verbose_name_plural = "Worker", "Workers"

    def __unicode__(self):
        return "%s" % (self.name)

    @models.permalink
    def get_absolute_url(self):
        return ('')

def get_next_ticket():
  ticket_prefix = datetime.datetime.now().strftime("%Y-%m")
  ticket_sequence = "-%04d" % (len(Activity.objects.filter(ticket__startswith=ticket_prefix)) + 1)
  return ticket_prefix + ticket_sequence

class Activity(models.Model):
    """Bucket to log work time against"""

    ticket = models.CharField(_('ticket'), max_length=40, unique=True, blank=False, null=False, default=get_next_ticket)
    description = models.CharField(_('Description'), max_length=120, blank=True, null=True)
    job_complete = models.BooleanField(_('Job Complete?'),default=False)
    on_work_queue = models.BooleanField(_('On Work Queue?'),default=False)

    def save(self, *args, **kwargs):
      if not self.ticket:
        self.ticket = get_next_ticket()
      super(Activity, self).save(*args, **kwargs)

    class Meta:
        ordering = ['ticket',]
        verbose_name, verbose_name_plural = "Job", "Jobs"

    def __unicode__(self):
        return "%s %s" % (self.ticket, self.description)

    @models.permalink
    def get_absolute_url(self):
        return ('')

class ClockPunch(models.Model):
    """an event with a date-timestamp signifying a Worker changing from one Activity to another"""

    timestamp = models.DateTimeField(_('Moment in Time'), blank=False, null=False, auto_now_add=True)
    activity = models.ForeignKey(Activity)
    worker = models.ForeignKey(Worker)
    logged = models.BooleanField(default=False)


    def log_start(self, *args, **kwargs):
      self.log()

    def log_end(self, *args, **kwargs):
      self.log()

    def log(self, *args, **kwargs):
      self.logged = True
      self.save()

    def matches(self, *args, **kwargs):
      break_event = Activity.objects.get(ticket="Break")
      open_event = Activity.objects.get(ticket="Open Shop")
      close_event = Activity.objects.get(ticket="Close Shop")

      #dates = ClockPunch.objects.dates('timestamp','day')
      #punches = ClockPunch.objects.all().order_by('timestamp')
      punches = ClockPunch.objects.filter(logged=False).order_by('timestamp')

      scoreboard = {}

      for punch in punches:
        if punch.activity == open_event:
          punch.log()
        elif punch.activity == close_event:
          if not scoreboard:
            # a close with nothing open!
            punch.log()
          for worker in scoreboard.keys():
            wp = WorkPeriod(start_punch = scoreboard[worker]['start'], end_punch=punch)
            wp.save()
            del scoreboard[worker]

        elif punch.activity == break_event:
          if punch.worker not in scoreboard:
            punch.log()
          else:
            wp = WorkPeriod(start_punch = scoreboard[punch.worker]['start'], end_punch=punch)
            wp.save()
            del scoreboard[punch.worker]
        elif punch.worker not in scoreboard:
          scoreboard[punch.worker] = {"start" : punch}
        else:
          wp = WorkPeriod(start_punch = scoreboard[punch.worker]['start'], end_punch=punch)
          wp.save()
          scoreboard[punch.worker] = {"start" : punch}
    
    def save(self, *args, **kwargs):
      super(ClockPunch, self).save(*args, **kwargs)
      self.matches(*args, **kwargs)
      
    class Meta:
        ordering = ['-timestamp',]

    def __unicode__(self):
        return "%s punched %s at %s" % (self.worker, self.activity, self.timestamp)

    @models.permalink
    def get_absolute_url(self):
        return ('')

class ClockPunchForm(ModelForm):

  def __init__(self, *args, **kwargs):
    self.helper = FormHelper()
    self.helper.add_input(Submit('submit','Submit'))
    # initialize
    super(ClockPunchForm, self).__init__(*args, **kwargs)
    for fieldname in ('worker','activity'):
      self.fields[fieldname].empty_label = None

  class Meta:
    model = ClockPunch
    fields = ('worker', 'activity')
    widgets = {'worker': RadioSelect, 'activity': RadioSelect }


class WorkPeriod(models.Model):
    """a span of time when work on a job is done by a Worker"""


    start_punch = models.ForeignKey(ClockPunch, related_name='workperiod_start_punch', unique=True)
    end_punch = models.ForeignKey(ClockPunch, related_name='workperiod_end_punch')

    def _get_worker(self):
      return self.start_punch.worker

    def _get_job(self):
      return self.start_punch.activity

    def _get_start_time(self):
      return self.start_punch.timestamp

    def _get_end_time(self):
      return self.end_punch.timestamp

    def _get_duration(self):
      return self.end_time - self.start_time

    worker = property(_get_worker)
    job = property(_get_job)
    start_time = property(_get_start_time)
    end_time = property(_get_end_time)
    duration = property(_get_duration)


    ## TODO: add save method to set start-punch as logged
    def save(self, *args, **kwargs):
      self.start_punch.log_start()
      self.end_punch.log_end()

      super(WorkPeriod, self).save(*args, **kwargs)


    class Meta:
      pass
      #ordering = ['start_time',]

    def __unicode__(self):
        return "%s - %s %s" % (self.worker, self.start_time, self.job)

    @models.permalink
    def get_absolute_url(self):
        return ('')