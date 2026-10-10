from rest_framework import serializers
from .models import CalendarEntryModel

class CalendarEntryModelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CalendarEntryModel
        fields = '__all__'

class RepeatingCalendarEntryModelSerializer(serializers.ModelSerializer):
    which_days_list=serializers.SerializerMethodField()
    class Meta:
        model = CalendarEntryModel
        fields = ['id', 'start_date','title','which_days_list']

    def get_which_days_list(self, obj):
        return obj.get_which_days_list()