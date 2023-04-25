from django.core.mail import EmailMessage
# from .serilalizers import * 
# from .templates import * 
# import json, os
from .models import *
from django.http import FileResponse, HttpResponse, JsonResponse
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import date,datetime


class LoginAPI(APIView):
    
    def post(self,request):
        
        try: 
            email = request.data['email']
            password=request.data['password']
            
            objects = Users.objects.filter(email=email)
            if len(objects)==0:
                return Response({
                    "status":"error",
                    "errorMessage":"Invalid Credentials"
                })
            
                
        
            user_object=objects.first()
            if not user_object.password==password:
                return Response({
                    "status":"error",
                    "errorMessage":"Invalid Credentials"
                })
            return Response({
                "status" : "success",
                "data":{
                    'username':user_object.username,
                    'is_donor':user_object.is_donor,
                    'is_orphanage':user_object.is_orphanage,

                },
            })
        except:
            return Response({
                "status" : "error",
                "errorMessage": "Please Contact Administrator"
            })


class SignupAPI(APIView):
    def post(self,request):
        username = request.data['username']
        password = request.data['password']
        email = request.data['email']
        is_donor=request.data['is_donor']
        is_orphanage=request.data['is_orphanage']
       
        objects= Users(
                    username= username,
                    password=password,
                    email=email,
                    is_donor=is_donor,
                    is_orphanage=is_orphanage,
                )
        objects.save() 
        
        return Response({
            "status" : "success",
            "statusResponse":"Added Successfully"
        })
    