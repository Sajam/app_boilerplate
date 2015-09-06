from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from rest_framework import viewsets
from serializers import PartySerializer
from models import Party


class PartyViewSet(viewsets.ModelViewSet):
    queryset = Party.objects.all()
    serializer_class = PartySerializer


class PartyView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Parties!')

