from django.db import models
from django.utils import timezone

days_of_week=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']

class CalendarEntryModel(models.Model):
    type=models.CharField(default='One Time')
    start_date = models.DateField(default=timezone.now)
    line_one=models.CharField(default='', max_length=20, blank=True)
    line_two=models.CharField(default='', max_length=20, blank=True)
    line_three=models.CharField(default='', max_length=20, blank=True)
    color=models.CharField(default='Black')
    bg_color=models.CharField(default='White')
    which_days=models.IntegerField(default=0)
    link=models.CharField(default='', blank=True)

    def get_text(self):
        return_text=[]

        if self.line_one!='':
            return_text.append(self.line_one)

        if self.line_two!='':
            return_text.append(self.line_two)

        if self.line_three!='':
            return_text.append(self.line_three)

        return return_text     
                       
    def get_which_days_list(self):

        index=6
        which_days=self.which_days
        return_values=[]
        for index in range(6,-1,-1):

            if which_days>=(2**index):
                return_values.insert(0,days_of_week[index])
                which_days-=(2**index)

        return return_values
