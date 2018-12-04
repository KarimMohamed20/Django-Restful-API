from django.db import models
from datetime import datetime
from django.utils import timezone



class Blog(models.Model):
	title=models.CharField(max_length=100,blank=True,default='')
	content=models.TextField()
	published=models.DateField(auto_now_add=False,auto_now=False)

	def __str__(self):
		return str(self.title)