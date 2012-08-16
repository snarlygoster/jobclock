from django import forms
from joborder.models import JobItem

class JobItemForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(JobItemForm, self).__init__(*args, **kwargs)
        for i, question in enumerate(['Cover Material', 'Height', 'Width']):
            self.fields['spec_%s' % i] = forms.CharField(label=question)
    #def save(self):

    def spec_answers(self):
        for name, value in self.cleaned_data.items():
            if name.startswith('spec_'):
                yield (self.fields[name].label, value)

    class Meta:
        model = JobItem