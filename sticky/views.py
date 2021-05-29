from django.shortcuts import render
from rest_framework import viewsets
from .models import StickyNote
from .serializers import StickyNoteSerializer

# Create your views here.
class StickNoteViewSet(viewsets.ModelViewSet):
    queryset = StickyNote.objects.all()
    serializer_class = StickyNoteSerializer