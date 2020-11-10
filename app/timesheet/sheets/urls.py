"""Defines URL patterns for sheets."""
from django.urls import path
from . import views

app_name = 'timesheets'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    #path('timesheets/', views.timesheet, name='timesheet'),
    path('new_timesheet/', views.newtimesheet, name='newtimesheet'),
    path('view_timesheet/', views.view_timesheet, name='view_timesheet'),
    ]
