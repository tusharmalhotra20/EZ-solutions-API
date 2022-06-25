from __future__ import absolute_import
from os import stat
from django.shortcuts import render
from rest_framework import generics
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from . models import users
from . serializers import UsersSerializers
from . utils import Util
from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.sites.shortcuts import get_current_site
from rest_framework_simplejwt.tokens import RefreshToken
from api import serializers
from django.urls import reverse
import jwt
from django.conf import settings
# Create your views here.

class usersList(APIView):    # inheriting usersList from APIView
    def get(self, request, *args, **kwargs):
        qs = users.objects.all()
        serializer = UsersSerializers(qs, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = UsersSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = users.objects.get(email=serializer.data['email'])
            token = RefreshToken.for_user(user).access_token
            current_site = get_current_site(request).domain
            relativeLink=reverse('email-verify')
            absolute_url = 'http://'+current_site+relativeLink+'?token='+str(token)
            email_body='Hi '+ user.username + ' Use below link to verify your email'+ "\n"+absolute_url
            data = {'email_body':email_body, 'to_email':user.email,'email_subject':'Verify your email'}
            Util.send_email(data)
            
            return Response({"Email verification": "Verify your email sent to the provided email address."})
        else:
            Response(serializer.errors)

class VerifyEmail(generics.GenericAPIView):
    def get(self, request):
        # pass
        token = request.GET.get('token')
        try:
            payload = jwt.decode(token, settings.SECRET_KEY)
            # print(payload)
            user = users.objects.get(id=payload['user_id'])
            # print(user)
            if not user.is_verified:
                user.is_verified = True
                user.save()
        
            return Response({"Email":"Verified"}, status=status.HTTP_200_OK)
        
        except jwt.ExpiredSignatureError as identifier:
            return Response({"error": "Activation expired"}, status=status.HTTP_400_BAD_REQUEST)
        
        except jwt.exceptions.DecodeError as identifier:
            return Response({"error": "Inavlid token"}, status=status.HTTP_400_BAD_REQUEST)
        
