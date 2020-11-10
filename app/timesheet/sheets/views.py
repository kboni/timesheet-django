from django.shortcuts import render, redirect
from .models import Timesheet, Project, Client, Activity
from .forms import TimesheetForm


# Create your views here.
def index(request):
    """The home page for time sheets."""
    return render(request, 'timesheets/index.html')


# def timesheet(request):
#     """Default Time sheet table"""
#     time_sheet = Timesheet.objects.all()
#     clients = Client.objects.all()
#     projects = Project.objects.all()
#     activities = Activity. objects.all()
#     context = {'time_sheet': time_sheet,
#                'clients': clients,
#                'projects': projects,
#                'activities': activities}
#     return render(request, 'timesheets/timesheet.html', context)


def newtimesheet(request):
    """Adds new time sheet to the database"""
    if request.method != 'POST':
        form = TimesheetForm()
    else:
        # POST data submitted; process data.
        form = TimesheetForm(data=request.POST)
        if form.is_valid():
            new_timesheet = form.save(commit=False)
            new_timesheet.save()
            return redirect('timesheets:view_timesheet')

        # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'timesheets/new_timesheet.html', context)


def view_timesheet(request):
    """Views all time sheets from the database. """
    ts_view = Timesheet.objects.all()
    context = {'ts_view': ts_view}
    return render(request, 'timesheets/view_timesheet.html', context)
