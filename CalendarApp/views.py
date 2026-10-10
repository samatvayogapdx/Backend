from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework import status
import datetime

class NewCalendarEntry(APIView):
    def post(self, request, *args, **kwargs):

        try:
            serializer = CalendarEntryModelSerializer(data=request.data)
            if serializer.is_valid():

                serializer.save()

            else:
                print(serializer.errors)
            # Return the newly created object data and a 201 Created status
            return Response(serializer.data, status=status.HTTP_201_CREATED)        
        except:
            return Response({'error':'Entry not created'}, status=status.HTTP_400_BAD_REQUEST)

class CalendarEntry(APIView):
    def get(self, request, *args, **kwargs):
        these_ids=[]
        try:
            not_repeting_records = CalendarEntryModel.objects.all()
            these_ids = [one_record.id for one_record in not_repeting_records]

            serializer=CalendarEntryModelSerializer(CalendarEntryModel.objects.filter(id__in=these_ids), many=True)
            return Response(serializer.data, status =status.HTTP_200_OK)
        except:
            return Response({'error':'Difficulty getting records'}, status =status.HTTP_400_BAD_REQUEST)

class CalendarEntryCurrentRepeating(APIView):  
    def get(self,request, *args, **kwargs):
        try:

            this_record= CalendarEntryModel.objects.filter(type='Repeating').order_by('-start_date').first()
            if (this_record==None):
                return Response({'title':'$$$$'}, status =status.HTTP_200_OK)            
            
            serializer=RepeatingCalendarEntryModelSerializer(this_record, many=False)
            return Response(serializer.data, status =status.HTTP_200_OK)        
        except:
            return Response({'error':'Difficulty getting repeating records'}, status =status.HTTP_400_BAD_REQUEST)
        
class CalendarEntryDelete(APIView):
    def delete(self, request,id, *args, **kwargs):
        try:
            CalendarEntryModel.objects.get(id=id).delete()
            return Response({'message':'Record Deleted'}, status =status.HTTP_200_OK )
        except:
            return Response({'error':'Not able to delete record'}, status =status.HTTP_400_BAD_REQUEST )

class GetCalendarDays(APIView):
    def get(self, request, month, year, *args, **kwargs):
        month=month+1  #react they start at zero
        these_days=[]
        first_day_of_month = datetime.date(year,month,1)
        last_day_of_month=None

        try:
            this_time_delta =datetime.date(year,month+1,1)-first_day_of_month
            last_day_of_month = datetime.date(year,month,this_time_delta.days)
        except:
            last_day_of_month=datetime.date(year,month,31)

        these_one_time_records = CalendarEntryModel.objects.exclude(type='Repeating')

        this_repeating_record  = CalendarEntryModel.objects.filter(
            type='Repeating').filter(
                start_date__lte=first_day_of_month).order_by(
                    '-start_date').first()
                
        other_repeating_records = CalendarEntryModel.objects.filter(
            start_date__month=month, start_date__year=year).filter(
                type='Repeating').exclude(
                    id=this_repeating_record.id).order_by(
                        'start_date')

        this_day=first_day_of_month
        theses_days_of_week=[]
        if not this_repeating_record==None:
            theses_days_of_week= this_repeating_record.get_which_days_list()
        days_of_week=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

        for one_day in range(first_day_of_month.weekday()+1):
            these_days.append({
                'day':-1*one_day-1,
            })

        while last_day_of_month>=this_day:

            if len(other_repeating_records)>0:
                if this_day==other_repeating_records[0].start_date:
                    this_repeating_record=other_repeating_records[0]
                    theses_days_of_week=this_repeating_record.get_which_days_list()

            new_day={
                'day':this_day.day,
                'title':'No Class',
                'color':'black'
            }

            try:
                this_record = these_one_time_records.get(start_date=this_day)
                new_day['title']=this_record.title
                new_day['color']=this_record.color
            except:
                if days_of_week[this_day.weekday()] in theses_days_of_week:
                    new_day['title']=this_repeating_record.title
                    new_day['color']=this_repeating_record.color

            these_days.append(new_day)

            this_day += datetime.timedelta(days=1)

        return Response({'these_days':these_days}, status =status.HTTP_200_OK )
