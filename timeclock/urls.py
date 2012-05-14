from django.conf.urls.defaults import patterns, include, url


# Our stuff
from timeclock.views import ClockPunchView, ClockPunchSums, WorkPeriodView

urlpatterns = patterns('',
    url(r'^$', ClockPunchView.as_view(), name='clockpunch-view'),
    url(r'summary', ClockPunchSums.as_view(), name='clockpunchsums'),
    url(r'workperiods/(?P<workername>\w*)/$', WorkPeriodView.as_view(), name='workperiods'),
    url(r'workperiods/(?P<workername>\w*)/(?P<startdate>\d{8}/$)', WorkPeriodView.as_view(), name='workperiod_startdate'),
    # Examples:
    # url(r'^$', 'jobclockproj.views.home', name='home'),
    # url(r'^jobclockproj/', include('jobclockproj.foo.urls')),
)
