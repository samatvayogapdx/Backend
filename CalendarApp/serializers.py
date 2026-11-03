from rest_framework import serializers
from .models import CalendarEntryModel

class CalendarEntryModelSerializer(serializers.ModelSerializer):
    text=serializers.SerializerMethodField()
    class Meta:
        model = CalendarEntryModel
        fields = '__all__'

    def get_text(self, obj):
        return obj.get_text()

class RepeatingCalendarEntryModelSerializer(serializers.ModelSerializer):
    which_days_list=serializers.SerializerMethodField()
    class Meta:
        model = CalendarEntryModel
        fields = '__all__'

    def get_which_days_list(self, obj):
        return obj.get_which_days_list()