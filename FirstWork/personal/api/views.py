from rest_framework.generics import *
from rest_framework.views import APIView
from rest_framework import status, viewsets
from personal.models import Personal
from rest_framework.response import Response
from .serializers import PersonalSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly,AllowAny
from rest_framework.decorators import action
from .encryption_util import *
from rest_framework import renderers
from .permissions import *


class SimpleApiView(APIView):

    def get(self,request):
        data={
            'foo':'bar'
        }
        enc = encrypt(data)
        return Response(enc)

class PersonalViewSet(viewsets.ModelViewSet):
    queryset = Personal.objects.all()
    serializer_class = PersonalSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,PostOwnPersonal)
    def list(self , request):
        snippets = Personal.objects.all()
        serializer = PersonalSerializer(snippets, many=True)
        return Response(encrypt(serializer.data))

    def perform_create(self, serializer):
        serializer.save(user_profile=self.request.user)
     
    def retrieve(self, request, pk=None):
        queryset = Personal.objects.all()
        msg = get_object_or_404(queryset, pk=pk)
        serializer = PersonalSerializer(msg)
        return Response(encrypt(serializer.data))

        #for i in range( len(serializer.data) ):
        #    for (k,v) in serializer.data[i].items():
        #        serializer.data[i][str(k)]=encrypt(v)
        
    
    
