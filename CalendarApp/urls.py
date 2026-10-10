from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('new-calendar-entry/', NewCalendarEntry.as_view(), name='new-calendar-entry'),
    path('get-all-calendar-entries/', CalendarEntry.as_view(), name='get-all-calendar-entries'),
    path('get-repeating-calendar/', CalendarEntryCurrentRepeating.as_view(), name='get-repeating-calendar'),
    path('delete-entry/<int:id>/', CalendarEntryDelete.as_view(), name='delete-entry'),
    path('get-calendar-days/<int:month>/<int:year>/', GetCalendarDays.as_view(), name='get-calendar-days'),

    
]