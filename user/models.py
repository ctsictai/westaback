from django.db import models

# Create your models here

class User(models.Model):
    username   = models.CharField(max_length=50)
    password   = models.CharField(max_length=300)
    email      = models.CharField(max_length=50, unique=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
    	db_table = 'User'



