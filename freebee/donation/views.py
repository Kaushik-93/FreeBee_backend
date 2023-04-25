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

class DonorAPI(APIView):
    def get(self,request):
        pass
    
    
    def post(self,request):
        name = request.data['name']
        address = request.data['address']
        city = request.data['city']
        state = request.data['state']
        pincode = request.data['pincode']
        mobile_no = request.data['mobile_no']
        alt_mobile_no = request.data['alt_mobile_no']
        email=request.data['email']
        items=request.data['items']
        vehicle_type=request.data['vehicle_type']
        objects= Donor(
                    name= name,
                    address=address,
                    city=city,
                    state=state,
                    pincode=pincode,
                    mobile_no=mobile_no,
                    alt_mobile_no=alt_mobile_no,
                    email=email,
                    items=items,
                    vehicle_type=vehicle_type,
                )
        objects.save()
        return Response({
            "status" : "success",
            "statusResponse":"Added Successfully"
        }) 
class OrphanageAPI(APIView):
    def get(self,request):
        pass
    
    
    def post(self,request):
        name = request.data['name']
        address = request.data['address']
        city = request.data['city']
        state = request.data['state']
        pincode = request.data['pincode']
        mobile_no = request.data['mobile_no']
        landline_no = request.data['landline_no']
        email=request.data['email']
        image=request.data['image']
        objects= Orphanage(
                    name= name,
                    address=address,
                    city=city,
                    state=state,
                    pincode=pincode,
                    mobile_no=mobile_no,
                    landline_no=landline_no,
                    email=email,
                    image=image,
                )
        objects.save()
        return Response({
            "status" : "success",
            "statusResponse":"Added Successfully",
            "data":{
                    'image':objects.name,
                    
                },
        })
        

