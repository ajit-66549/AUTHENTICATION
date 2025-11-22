from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import Note
from .serializers import NoteSerializer

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

class CustomTokenObtain(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        try:
            response = super().post(request, *args, **kwargs)
            tokens = response.data
            
            access_token = tokens['access']
            refresh_token = tokens['refresh']
            
            res = Response()
            
            res.data({'success': True})
            
            res.set_cookie(
                key= 'access_token',
                value= access_token,
                httponly= True,
                secure= True,
                samesite="None",
                path='/',
            )
            
            res.set_cookie(
                key= 'refresh_token',
                value= refresh_token,
                httponly= True,
                secure= True,
                samesite="None",
                path='/',
            )
            
            return res
            
        except:
            return Response({'success': False})

class CustomRefreshToken(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.COOKIES.get('refresh_token')
            
            request.data['refresh'] = refresh_token
            
            response = super().post(self, request, *args, **kwargs)
            
            tokens = response.data
            access_token = tokens['access']
            
            res = Response()
            
            res.data({'refresh': True})
            
            res.set_cookie(
                key= 'access_token',
                value= access_token,
                httponly= True,
                secure= True,
                samesite= "None",
                path= '/',
            )
            
            return res
            
        except:
            return Response({'refresh': False})

@api_view(['GET'])
@permission_classes([IsAuthenticated])       # Need to be authenticated to access this view function (endpoint)
def getnote(request):          # Getting request from the user
    user = request.user        # Taking user                           
    notes = Note.objects.filter(author=user)  # Taking notes whose author is user
    serializer = NoteSerializer(notes, many=True)  # To convert JSON data in python object
    return Response(serializer.data)   # Returning final serialized data (Python data)