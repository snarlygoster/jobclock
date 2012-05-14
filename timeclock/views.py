import datetime

from django.views.generic import ListView, CreateView, TemplateView
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

# Create your views here.

from timeclock.models import Worker, Activity, ClockPunch, ClockPunchForm, WorkPeriod

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
  cp = ClockPunch()
  cp.matches()
  work_periods = WorkPeriod.objects.all()

  def get_context_data(self,**kwargs):
    context = super(ClockPunchSums,self).get_context_data(**kwargs)
    context['work_periods'] = self.work_periods
    return context


class WorkPeriodView(TemplateView):
  template_name = 'timeclock/work_period_view.html'
  cp = ClockPunch()
  cp.matches()

  def _get_work_periods(self, **kwargs):
    #workername = self.kwargs['workername']
    work_periods = WorkPeriod.objects.all()
    #wp_by_worker =
    return work_periods


  def get_context_data(self, **kwargs):
    context = super(WorkPeriodView, self).get_context_data(**kwargs)
    context['workername'] = self.kwargs['workername']
    context['work_periods'] = self._get_work_periods() #workername=self.kwargs['workername'])
    return context
