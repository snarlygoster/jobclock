from django.conf.urls.defaults import patterns, include, url


# Our stuff
from timeclock.views import ClockPunchView, ClockPunchSums, WorkPeriodView

urlpatterns = patterns('',
    url(r'^$', ClockPunchView.as_view(), name='clockpunch-view'),
    url(r'summary', ClockPunchSums.as_view(), name='clockpunchsums'),
    url(r'workperiods/(?P<workername>.*)', WorkPeriodView.as_view(), name='workperiods'),
    # Examples:
    # url(r'^$', 'jobclockproj.views.home', name='home'),
    # url(r'^jobclockproj/', include('jobclockproj.foo.urls')),
)
