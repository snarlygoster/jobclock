import datetime

from django.views.generic import ListView, CreateView, TemplateView
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

# Create your views here.

from timeclock.models import Worker, Activity, ClockPunch, ClockPunchForm, ClockPunchMatches

class TimeclockView(ListView):
  model = Worker
  context_object_name = 'worker_list'


class ClockPunchView(CreateView):
  form_class = ClockPunchForm
  template_name = 'timeclock/clockpunch_form.html'


  def get_form(self, form_class):
    form = super(ClockPunchView, self).get_form(form_class)
    form.fields['activity'].queryset = Activity.objects.filter(on_work_queue=True)
    form.fields['worker'].queryset = Worker.objects.filter(can_work=True)
    return form

  def get_context_data(self, **kwargs):
    context = super(ClockPunchView,self).get_context_data(**kwargs)
    last_ten_punches = ClockPunch.objects.all()[0:9]
    context['last_ten_punches'] = [ {'worker': p.worker.name, 'job' : p.activity.ticket , 'tstamp': p.timestamp} for p in last_ten_punches ]
    return context

#  success_url = reverse_lazy('clockpunch-view')
  def get_success_url(self):
    return reverse('clockpunch-view')

  def form_valid(self,form):
    form.save()
    return HttpResponseRedirect(self.get_success_url())

# def form_invalid(self,form):
#     return HttpResponseRedirect(self.get_success_url())


class ClockPunchSums(TemplateView):
  template_name = 'timeclock/clockpunchsums.html'
  work_periods = ClockPunchMatches().work_periods
  object_list = []
  
  for job, work_sessions in work_periods.iteritems():
    session_total = datetime.timedelta(0)
    for session in work_sessions:
      session_total = session_total + session[1]
    session_total_seconds = (session_total.days * 24 * 60 * 60) + session_total.seconds
    hours,remainder = divmod(session_total_seconds,3600)
    minutes, seconds = divmod(remainder, 60)
    job_time = "%2d:%02d" % (hours, minutes)
    object_list.append({'ticket' : job.ticket, 'description' : job.description, 'complete' : job.job_complete, 'time' : job_time})
  
  def get_context_data(self,**kwargs):
    context = super(ClockPunchSums,self).get_context_data(**kwargs)
    context['object_list'] = self.object_list
    return context
    
#   def get_context_data(self,**kwargs):
#     work_periods = ClockPunchMatches().work_periods
#     context = super(ClockPunchSums,self).get_context_data(**kwargs)
#     context['work_periods'] = work_periods
#     return context