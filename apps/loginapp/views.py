from django.shortcuts import render,redirect, HttpResponse
from .models import Userlog
from django.contrib import messages
from ..demoapp.models import Trip
from datetime import datetime
import bcrypt
def index(request):
	return render(request,'loginapp/index.html')
def register(request):
	return render(request,'loginapp/register.html')
def success(request):
	context={
	'travels' : Trip.objects.filter(user__name=request.session['user']),
	'joiners' : Trip.objects.filter(traveller__name=request.session['user']),
    'trips': Trip.objects.exclude(user__name=request.session['user']).exclude(traveller__name=request.session['user']),
    }
	print request.session['user']
	return render(request,'demoapp/success.html',context)
def user(request):
	errors = False
	check1 = Userlog.UserManager.first_name(request.POST['name'])
	check2 = Userlog.UserManager.user_name(request.POST['username'])
	check3 = Userlog.UserManager.password(request.POST['password'])
	check3_char = Userlog.UserManager.password_charcheck(request.POST['password'])
	print request.POST['password'] 
	print bcrypt.gensalt()  
	check4 = Userlog.UserManager.confirm_password(request.POST['password'],request.POST['confirm_password'])
	if check1[0] == False:
		messages.add_message(request, messages.INFO, "Invalid name", extra_tags="regtag")
		errors = True
	if check2[0] == False:
		messages.add_message(request, messages.INFO, "Invalid username", extra_tags="regtag")
		errors = True
	if check3[0] == False:
		messages.add_message(request, messages.INFO, "Invalid password", extra_tags="regtag")
		print check4[1]
		errors = True
	if check3_char[0] == False:
		messages.add_message(request, messages.INFO, "Invalid characters in password", extra_tags="regtag")
		errors = True
	if check4[0] == False:
		messages.add_message(request, messages.INFO, "Please confirm your password correctly", extra_tags="regtag")
		errors = True
	if Userlog.objects.filter(username = request.POST['username']):
	    messages.add_message(request, messages.INFO, "This username already existed!", extra_tags="regtag")
	    errors = True
	# Errors Route
	if errors == True:
		return redirect('/register')
	elif (check1[0] == True & check2[0] == True  & check3[0] == True ):
		Userlog.UserManager.create(name=check1[1], username=check2[1], password=check3[1])
		request.session['user'] = check1[1]
		print 
		return redirect('/travels')

def login(request):
	check5 = Userlog.UserManager.log(request.POST['username'], request.POST['password'])
	if check5[0] == False:
		messages.add_message(request, messages.INFO, check5[1], extra_tags='logtag')
		print check5[1]
		return redirect('/')
	else:
		request.session['user'] = check5[1]
		return redirect('/travels')

def logout(request):
	del request.session['user']
	return redirect('/')







