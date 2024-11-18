from django.shortcuts import render

import requests
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import IPAddress
from .serializers import IPAddressSerializer

class IPAddressView(APIView):
    def get(self, request, *args, **kwargs):
        ip = request.query_params.get('ip')
        
        if not ip:
            return Response({"error": "IP address is required"}, status=status.HTTP_400_BAD_REQUEST)

        ip_entry = IPAddress.objects.filter(ip=ip).first()
        
        if ip_entry:
            serializer = IPAddressSerializer(ip_entry)
            return Response(serializer.data, status=status.HTTP_200_OK)

        external_api_url = f"http://ip-api.com/json/{ip}"
        response = requests.get(external_api_url)
        data = response.json()
        
        if data['status'] == 'fail':
            return Response({"error": "Invalid IP address"}, status=status.HTTP_400_BAD_REQUEST) 
        country = data.get('country', 'Unknown') 
        ip_entry = IPAddress.objects.create(ip=ip, country=country)
        serializer = IPAddressSerializer(ip_entry)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        
      
        
    
    
    
    