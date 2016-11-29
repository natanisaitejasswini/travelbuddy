from django.shortcuts import render,redirect, HttpResponse
from ..loginapp.models import Userlog
from .models import Trip
from django.contrib import messages 
from datetime import datetime
import bcrypt
def showUser(request):
    return render(request,"demoapp/show.html")
def showdestination(request,id):
	context ={
    'trips': Trip.objects.get(id = id)
    }
	return render(request,"demoapp/show2.html", context)
def user(request):
	errors = False
	check1 = Trip.UserManager.destination(request.POST['destination'])
	check2 = Trip.UserManager.description(request.POST['description'])
	check3 = Trip.UserManager.travelstart_check(request.POST['travelstart'])
	print request.POST['travelstart']
	check4 = Trip.UserManager.travelend_check(request.POST['travelend'],request.POST['travelstart'])
	print request.POST
	# Errors Route
	if check1[0] == False:
		messages.add_message(request, messages.INFO, "Invalid description", extra_tags="regtag")
		errors = True
	if check2[0] == False:
		messages.add_message(request, messages.INFO, "Invalid destination", extra_tags="regtag")
		errors = True
	if check3[0] == False:
		messages.add_message(request, messages.INFO, "Invalid Travel Start Date", extra_tags="regtag")
		errors = True
	if check4[0] == False:
		print check4[1]
		messages.add_message(request, messages.INFO, "Invalid Travel End Date", extra_tags="regtag")
		print check4[1]
		errors = True
	if errors == True:
		return redirect('/travels/add')
	elif (check1[0] == True & check2[0] == True & check3[0] == True  & check4[0] == True):
		users = Userlog.objects.get(name = request.session['user'])
		Trip.objects.create(user = users ,destination=check1[1], description=check2[1], travelstart=check3[1], travelend=check4[1])
		return redirect('/travels')

def join(request,id): 
	trip = Trip.objects.get(id = id)
	trip.traveller.add(Userlog.objects.get(name=request.session['user']))
	trip.save()
	return redirect('/travels')

