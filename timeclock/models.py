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

class ClockPunchMatches():
    scoreboard = {}
    work_periods = defaultdict(list)

    def post_activity_change(self, punch):
      duration = punch.timestamp - self.scoreboard[punch.worker]['start']
      self.work_periods[self.scoreboard[punch.worker]["job"]].append((punch.worker,duration))

    def close_all_sessions(self, timestamp):
      for worker in self.scoreboard.keys():
        duration = timestamp - self.scoreboard[worker]['start']
        self.work_periods[self.scoreboard[worker]['job']].append((worker, duration))
        del self.scoreboard[worker]

    def __init__(self, *args, **options):

      break_event = Activity.objects.get(ticket="Break")
      open_event = Activity.objects.get(ticket="Open Shop")
      close_event = Activity.objects.get(ticket="Close Shop")

      dates = ClockPunch.objects.dates('timestamp','day')
      punches = ClockPunch.objects.all().order_by('timestamp')

      for punch in punches:
        if punch.activity == open_event:
          pass
        elif punch.activity == close_event:
          self.close_all_sessions(punch.timestamp)
        elif punch.activity == break_event:
          if punch.worker not in self.scoreboard:
            pass
          else:
            self.post_activity_change(punch)
            del self.scoreboard[punch.worker]
        elif punch.worker not in self.scoreboard:
          self.scoreboard[punch.worker] = {"start" : punch.timestamp, 'job' : punch.activity}
        else:
          self.post_activity_change(punch)
          self.scoreboard[punch.worker] = {"start" : punch.timestamp, 'job' : punch.activity}

class WorkPeriod(models.Model):
    """a span of time when work on a job is done by a Worker"""

    worker = models.ForeignKey(Worker)
    job = models.ForeignKey(Activity)

    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    class Meta:
        ordering = ['start_time',]

    def __unicode__(self):
        return "%s - %s" % (self.worker, self.start_time)

    @models.permalink
    def get_absolute_url(self):
        return ('')