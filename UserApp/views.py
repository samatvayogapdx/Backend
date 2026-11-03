from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail

class SubmitForm(APIView):
    def post(self, request, *args, **kwargs):
        try:
            send_mail(
                subject='You have a new student!',
                message='{} {}\nphone:{}\nemail:{}\nAbout me:{}'.format(
                    request.data['first_name'],
                    request.data['last_name'],
                    request.data['email'],
                    request.data['phone'],                    
                    request.data['personal_info']),
                from_email='deepa@samatvayogapdx.com',
                recipient_list= ['deepa@samatvayogapdx.com '],
            )
            return Response({'status':'OK'}, status=status.HTTP_201_CREATED)        
        except Exception as e:
            print(e)
            return Response({'error':'Form not processed'}, status=status.HTTP_400_BAD_REQUEST)
