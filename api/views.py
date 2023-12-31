from django.shortcuts import render
from rest_framework import viewsets

from api.serializers import PersonSerializer,SpeciesSerializer
from api.models import Person, Species

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class SpeciesViewSet(viewsets.ModelViewSet):
    queryset= Species.objects.all()
    serializer_class = SpeciesSerializer