from django import forms

from .models import Timesheet


class TimesheetForm(forms.ModelForm):
    class Meta:
        model = Timesheet
        fields = ['user', 'client', 'project', 'activity', 'monday', 'tuesday', 'wednesday', 'thursday',
                  'friday', 'saturday', 'sunday']
