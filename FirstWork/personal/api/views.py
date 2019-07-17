from rest_framework.generics import (
    ListAPIView, 
    RetrieveAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView
)
from rest_framework.views import APIView
from rest_framework import status, viewsets
from personal.models import Personal
from rest_framework.response import Response
from .serializers import PersonalSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly,AllowAny
from rest_framework.decorators import action
from .encryption_util import *
from rest_framework import renderers

class PersonalListView(APIView):
    def get(self, request):
        snippets = Personal.objects.all()
        serializer = PersonalSerializer(snippets, many=True)
        for i in range( len(serializer.data) ):
            for (k,v) in serializer.data[i].items():
                serializer.data[i][str(k)]=encrypt(v)
        return Response(serializer.data)

class PersonalRetrieveView(RetrieveAPIView):
    queryset = Personal.objects.all()
    serializer_class = PersonalSerializer

class PersonalCreateView(CreateAPIView):
    queryset = Personal.objects.all()
    serializer_class = PersonalSerializer

class PersonalDestroyView(DestroyAPIView):
    queryset = Personal.objects.all()
    serializer_class = PersonalSerializer

class PersonalUpdateView(UpdateAPIView):
    queryset = Personal.objects.all()
    serializer_class = PersonalSerializer


class SimpleApiView(APIView):

    def get(self,request):
        data={
            'foo':'bar'
        }
        print(data)
        enc = encrypt(data)
        print(enc)
        return Response(enc)

class PersonalViewSet(viewsets.ModelViewSet):
    queryset = Personal.objects.all()
    serializer_class = PersonalSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    def list(self , request):
        snippets = Personal.objects.all()
        serializer = PersonalSerializer(snippets, many=True)
        #for i in range( len(serializer.data) ):
        #    for (k,v) in serializer.data[i].items():
        #        serializer.data[i][str(k)]=encrypt(v)
        return Response(encrypt(serializer.data))
    

    