from django.contrib import messages
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.views.generic import *
from django.apps import apps

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser

from .modelsBase import *

class BaseList(generics.ListCreateAPIView):
    model = None
    queryset = []
    serializer_class = None
    permission_classes = [IsAdminUser]
    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        #queryset = self.get_queryset()
        #serializer = UserSerializer(queryset, many=True)
        #self.model = apps.get_model(kwargs['app'], kwargs['model'])
        self.model = apps.get_model('core', 'User')
        class ListSerializer(Base_Serializer):
            class Meta(Base_Serializer.Meta):
                model = self.model
                fields = ('__all__')
        self.serializer_class = ListSerializer
        self.queryset = self.model.objects.all()
        serializer = ListSerializer(self.queryset, many=True)
        return Response(serializer.data)
