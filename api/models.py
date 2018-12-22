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
