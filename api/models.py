from django.db import models
from area2076.models import User

# Create your models here.
class Task(models.Model):
    created_at 		= models.DateTimeField(auto_now_add=True)
    client_name 	= models.CharField(max_length=200)
    client_number 	= models.CharField(max_length=200)
    client_dob 		= models.DateField(auto_now_add=True)
    status 			= models.CharField(max_length=200)
    user 			= models.ForeignKey(User, on_delete=models.CASCADE)

class Policy(models.Model):
    id 				= models.IntegerField(primary_key=True, unique=True)
    start_date 		= models.DateField(null=True)
    end_date 		= models.DateField(null=True)
    due_date 		= models.DateField(null=True)
    status 			= models.CharField(max_length=200, null=True)
    type 			= models.CharField(max_length=200, null=True)
    term 			= models.CharField(max_length=200, null=True)
    premium 		= models.IntegerField(null=True)
    sum_assured 	= models.IntegerField(null=True)
    client  		= models.ForeignKey(User, on_delete=models.CASCADE)