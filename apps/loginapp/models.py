from __future__ import unicode_literals
from django.db import models
from django.contrib import messages
import re
from datetime import datetime
import bcrypt
class UserManager(models.Manager):
	def first_name(self,name):
		if not len(name) > 3:
			return(False,"Invalid Firstname") 
		else:
			return(True,name)
	def name_charcheck(self,name):
		if not name.isalpha():
			return(False,"Invalid characters")
		else:
			return(True,name)
	def user_name(self,username):
		if not len(username) > 3:
			return(False,"Invalid lastname") 
		else:
			return(True,username)
	def password_charcheck(self,password):
		if not password.isalpha():
			return(False,"Password should have characters")
		else:
			return(True,"password")
	def password(self,password):
		if not len(password) > 5:
			return(False,"Invalid password") 
		else:
				# BCRYPT PASSWORD
			password = password.encode()
			hashed = bcrypt.hashpw(password, bcrypt.gensalt())
			return (True, hashed)
	def confirm_password(self,password,confirm_password):
		if not password == confirm_password:
			return(False,"confirm password")
		else:
			return(True,"password confirmed")
  	def log(self,username,password):
  		# print email, password
  		# users = self.all()
  		# for auser in users:
  		# 	print auser.email
  		# print self.filter(email=email)
  		try:
  			user = self.get(username = username)
  			# print user.password
  		except:
  			return (False, "User Does not Exist")
		password = password.encode()
		user_password = user.password.encode()
		print user_password
		if user and bcrypt.hashpw(password, user_password) == user_password:
			return (True, user.name)
		else:
			return (False, "Password doesnot match")	

class Userlog(models.Model):
  name = models.CharField(max_length=30)
  username = models.CharField(max_length=30)
  password = models.CharField(max_length=300)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  UserManager = UserManager()
  objects = models.Manager()











