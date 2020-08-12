from django.db import models

class Data(models.Model):
	name=models.CharField(max_length=30)
	email=models.EmailField()
	contact=models.IntegerField()
	password=models.IntegerField()	
