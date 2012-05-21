from django.conf.urls.defaults import patterns, include, url


# Our stuff
from timeclock.views import ClockPunchView, ClockPunchSums, WorkPeriodView, WorkTotals

urlpatterns = patterns('',
    url(r'^$', ClockPunchView.as_view(), name='clockpunch_view'),
    url(r'summary', ClockPunchSums.as_view(), name='clockpunchsums'),
    url(r'workperiods/(?P<workername>\w*)/$', WorkPeriodView.as_view(), name='workperiods'),
    url(r'workperiods/(?P<workername>\w*)/(?P<startdate>\d{8}/$)', WorkPeriodView.as_view(), name='workperiod_startdate'),
    url(r'work_totals/$', WorkTotals.as_view(), name='work_totals_view'),
    url(r'work_totals/(?P<startyear>\d{4})/(?P<startmonth>\d{1,2})/(?P<startday>\d{1,2})/(?P<endyear>\d{4})/(?P<endmonth>\d{1,2})/(?P<endday>\d{1,2})/$', WorkTotals.as_view(), name='work_totals_view'),
    # Examples:
    # url(r'^$', 'jobclockproj.views.home', name='home'),
    # url(r'^jobclockproj/', include('jobclockproj.foo.urls')),
)
