from django.contrib.auth.models import Group
from area2076.models import User
from api.models import Task, Policy
from rest_framework import serializers


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ('id','created_at', 'client_name', 'client_number', 'client_dob', 'status', 'user')        

class PolicySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Policy
        fields = ('id', 'start_date', 'end_date', 'end_date', 'status', 'type', 'term', 'premium', 'sum_assured', 'client')                


class UserSerializer(serializers.HyperlinkedModelSerializer):
	tasks = TaskSerializer(many=True, read_only=True)
	class Meta:
		model = User
		fields = ('url', 'code', 'email', 'name', 'avatar', 'tasks', 'parent')