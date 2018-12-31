#from django.shortcuts import render

# Create your views here.

from django.contrib.auth.models import  Group
from area2076.models import User
from api.models import Task
from rest_framework import viewsets
from api.serializers import UserSerializer, GroupSerializer, TaskSerializer
from url_filter.integrations.drf import DjangoFilterBackend


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-code')
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['id', 'code', 'email', 'role' ]

    # def get_queryset(self):
    #     """
    #     Optionally restricts the returned purchases to a given user,
    #     by filtering against a `username` query parameter in the URL.
    #     """
    #     queryset = Purchase.objects.all()
    #     username = self.request.query_params.get('username', None)
    #     if username is not None:
    #         queryset = queryset.filter(purchaser__username=username)
    #     return queryset


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Tasks to be viewed or edited.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer   
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['id', 'user_id' ] 