from django.conf.urls.defaults import patterns, include, url


# Our stuff
from timeclock.views import TimeclockView, ClockPunchView, ClockPunchSums

urlpatterns = patterns('',
    url(r'^$', ClockPunchView.as_view(), name='clockpunch-view'),
    url(r'summary', ClockPunchSums.as_view(), name='clockpunchsums'),
    # Examples:
    # url(r'^$', 'jobclockproj.views.home', name='home'),
    # url(r'^jobclockproj/', include('jobclockproj.foo.urls')),
)
