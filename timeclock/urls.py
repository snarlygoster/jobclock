from django.conf.urls.defaults import patterns, include, url


# Our stuff
from timeclock.views import ClockPunchView, ClockPunchSums, WorkPeriodView, WorkHours, JobCost

urlpatterns = patterns('',
    url(r'^$', ClockPunchView.as_view(), name='clockpunch_view'),
    url(r'summary', ClockPunchSums.as_view(), name='clockpunchsums'),
    #url(r'workperiods/(?P<workername>\w*)/$', WorkPeriodView.as_view(), name='workperiods'),
    #url(r'workperiods/(?P<workername>\w*)/(?P<startdate>\d{8}/$)', WorkPeriodView.as_view(), name='workperiod_startdate'),
    url(r'work_hours/$', WorkHours.as_view(), name='work_hours_view'),
    url(r'work_hours/(?P<start_year>\d{4})/(?P<start_month>\d{1,2})/(?P<start_day>\d{1,2})/$', WorkHours.as_view(), name='work_hours_view'),
    url(r'work_hours/(?P<start_year>\d{4})/(?P<start_month>\d{1,2})/(?P<start_day>\d{1,2})/(?P<end_year>\d{4})/(?P<end_month>\d{1,2})/(?P<end_day>\d{1,2})/$', WorkHours.as_view(), name='work_hours_view'),
    url(r'job_cost/', JobCost.as_view(), name='job_cost_view'),
    # Examples:
    # url(r'^$', 'jobclockproj.views.home', name='home'),
    # url(r'^jobclockproj/', include('jobclockproj.foo.urls')),
)
