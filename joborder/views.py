# Create your views here.

from django.views.generic.edit import CreateView

from jobclock.models import JobItemForm, JobItem

class CreateJobItem(CreateView):
    form_class = JobItemForm