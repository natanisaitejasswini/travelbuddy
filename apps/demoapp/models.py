from __future__ import unicode_literals
from django.contrib import messages
from django.db import models
from datetime import datetime
from ..loginapp.models import Userlog
class UserManager(models.Manager):
	def description(self,description):
		if not len(description) > 1:
			return(False,"Invalid Description") 
		else:
			return(True,description)
	def destination(self,destination):
		if not len(destination) > 1:
			return(False,"Invalid destination") 
		else:
			return(True,destination)
	def travelstart_check(self,travelstart):
		travel1 = travelstart
		if travel1 == "":
			return(False, "Invalid travelstartdate")
		now = datetime.now()
		print now
		travelstart_test = datetime.strptime(travelstart, '%Y-%m-%d')
		if travelstart_test < now:
			return(False, "Invalid travelstartdate")
		else:
			return(True, travelstart)
			print travelstart
	def travelend_check(self,travelend,travelstart):
		travel2 = travelend 
		travel3= travelstart
		if travel2 == "":
			return(False, "Invalid travelenddate") 
		now = datetime.now()
		print now
		travelstart_test = datetime.strptime(travelstart, '%Y-%m-%d')
		travelend_test = datetime.strptime(travelend, '%Y-%m-%d')
		if travelend_test < travelstart_test:
			return(False, "Invalid travelenddate")
		else:
			return(True, travelend)
class Trip(models.Model):
	user = models.ForeignKey('loginapp.Userlog', related_name='users')
	traveller = models.ManyToManyField('loginapp.Userlog', related_name='traveller')
	destination = models.CharField(max_length=30)
	description = models.CharField(max_length=30)
	travelstart = models.DateField()
	travelend = models.DateField()
	created_at = models.DateField(auto_now_add=True)
	updated_at = models.DateField(auto_now=True)
	UserManager = UserManager()
	objects = models.Manager()
