# Create your views here.
from django.views.generic import ListView

from timeclock.models import Worker

class TimeclockView(ListView):
  model = Worker
  context_object_name = 'worker_list'
  