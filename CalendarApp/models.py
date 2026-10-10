from django.db import models
from django.utils import timezone

days_of_week=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']

class CalendarEntryModel(models.Model):
    type=models.CharField(default='One Time')
    start_date = models.DateField(default=timezone.now)
    title=models.CharField(default='Class')
    color=models.CharField(default='Black')
    which_days=models.IntegerField(default=0)

    def get_which_days_list(self):

        index=6
        which_days=self.which_days
        return_values=[]
        for index in range(6,-1,-1):

            if which_days>=(2**index):
                return_values.insert(0,days_of_week[index])
                which_days-=(2**index)

        return return_values
