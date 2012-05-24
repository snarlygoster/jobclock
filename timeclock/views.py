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

#  success_url = reverse_lazy('clockpunch_view')
  def get_success_url(self):
    return reverse('clockpunch_view')

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

class WorkTotals(TemplateView):
  template_name = 'timeclock/work_totals.html'

  def _start_date(self, **kwargs):
    start_year = int(self.kwargs.get('start_year', 2012))
    start_month = int(self.kwargs.get('start_month', 01))
    start_day = int(self.kwargs.get('start_day', 01))
    return datetime.date(start_year,start_month,start_day)

  def _end_date(self, **kwargs):
    end_year = int(self.kwargs.get('end_year', datetime.date.today().year))
    end_month = int(self.kwargs.get('end_month', datetime.date.today().month))
    end_day = int(self.kwargs.get('end_day', datetime.date.today().day))
    return datetime.date(end_year, end_month, end_day)


  def _get_work_periods(self, **kwargs):
    start_date = self._start_date()
    end_date = self._end_date()
    return WorkPeriod.objects.filter(start_punch__timestamp__range=(start_date,end_date))

  work_periods = property(_get_work_periods)

  def _get_worker_summary(self, **kwargs):
    worker = {}
    for wp in self.work_periods:
      if wp.worker in worker:
        worker[wp.worker]['total'] = worker[wp.worker]['total'] + wp.duration
        worker[wp.worker]['work_periods'].append(wp)
      else:
        worker[wp.worker] = {'total': wp.duration, 'work_periods': [wp]}
    return worker   
      
  def _get_job_summary(self, **kwargs):
    job = {}
    for wp in self.work_periods:
      if wp.job in job:
        job[wp.job]['total'] = job[wp.job]['total'] + wp.duration
        job[wp.job]['work_periods'].append(wp)
      else:
        job[wp.job] = {'total': wp.duration, 'work_periods': [wp]}
    return job
     
  def get_context_data(self, **kwargs):
    context = super(WorkTotals, self).get_context_data(**kwargs)
    params = context['params']
    context['bugs'] = params
    worker_total = {}
    job_total = {}
    for wp in self.work_periods:
      if wp.worker in worker_total:
        worker_total[wp.worker] = worker_total[wp.worker] + wp.duration
      else:
        worker_total[wp.worker] = wp.duration
      if wp.job in job_total:
        job_total[wp.job] = job_total[wp.job] + wp.duration
      else:
        job_total[wp.job] = wp.duration
    context['start_date'] = self._start_date()
    context['end_date'] = self._end_date()

    context['worker_total'] = worker_total
    context['job_total'] = job_total
    
    context['jobs'] = self._get_job_summary
    context['workers'] = self._get_worker_summary
    
    return context
