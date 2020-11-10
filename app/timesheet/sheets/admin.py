from django.contrib import admin
from.models import Project, Activity, Client, User, Timesheet

# Register your models here.
admin.site.register(Project)
admin.site.register(Activity)
admin.site.register(Client)
admin.site.register(User)
admin.site.register(Timesheet)
