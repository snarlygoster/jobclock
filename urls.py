from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

# Our stuff
from timeclock.views import TimeclockView, ClockPunchView, ClockPunchSums

urlpatterns = patterns('',
    url(r'^$', ClockPunchView.as_view(), name='clockpunch-view'),
    url(r'summary', ClockPunchSums.as_view(), name='clockpunchsums'),
    # Examples:
    # url(r'^$', 'jobclockproj.views.home', name='home'),
    # url(r'^jobclockproj/', include('jobclockproj.foo.urls')),


    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
