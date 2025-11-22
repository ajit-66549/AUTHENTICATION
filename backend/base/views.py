from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import Note
from .serializers import NoteSerializer


# Create your views here.
@api_view(['GET'])
@permission_classes([IsAuthenticated])       # Need to be authenticated to access this view function (endpoint)
def getnote(request):          # Getting request from the user
    user = request.user        # Taking user                           
    notes = Note.objects.filter(author=user)  # Taking notes whose author is user
    serializer = NoteSerializer(notes, many=True)  # To convert JSON data in python object
    return Response(serializer.data)   # Returning final serialized data (Python data)