import datetime
from django.shortcuts import  render, redirect
# from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.http import HttpResponse
from .models import Users

def register(request):
	return render(request,'register.html')


def login_page(request):
	return render(request,'login_page.html')



def login_request(request):
	if(request.method=='get'):
		return render(request,'register_request_denied.html',{'message':'Improper request'})
	else:
		print("hello post")
	email_id=request.POST.get('email')
	print(email_id)
	password=request.POST.get('pasw')
	print(password)
	if(Users.objects.filter(email_id=email_id)):
		u=Users.objects.filter(email_id=email_id)
		if(u[0].password==password):
			return render(request,'register_request.html',{'name':u[0].name})
		else:
			return render(request,'register_request_denied.html',{'message':'User credentials are invalid'})
        
		
	else:
		return render(request,'register_request_denied.html',{'message':'User didnt exits with this email id'})





def register_request(request):
	if(request.method=='get'):
		return render(request,'register_request_denied.html',{'message':'Improper request'})
	else:
		print("proper request")
	email_id=request.POST.get('email')
	if(Users.objects.filter(email_id=email_id)):
		u=Users.objects.filter(email_id=email_id)
		print(u[0].age)
		return render(request,'register_request_denied.html',{'message':'User already exist'})
	names=request.POST.get('fname')
	lastname=request.POST.get('lname')
	medical_history=request.POST.get('med_hist')
	age=request.POST.get('age')
	weight=request.POST.get('wgt')
	blood_grp=request.POST.get('bgrp')	
	address=request.POST.get('addr')
	mob=request.POST.get('phone')
	password=request.POST.get('pasw')
	user=Users(password=password,name=names,lname=lastname,medical_history=medical_history,age=age,weight=weight,blood_grp=blood_grp,email_id=email_id,address=address,mob_no=mob,date=datetime.date.today())
	user.save()
	return render(request,'register_request.html',{'name':names})










# def register_request(request):
# 	if request.method == "POST":
# 		form = NewUserForm(request.POST)
# 		if form.is_valid():
# 			user = form.save()
# 			login(request, user)
# 			messages.success(request, "Registration successful." )
# 			return redirect("main:homepage")
# 		messages.error(request, "Unsuccessful registration. Invalid information.")
# 	form = NewUserForm()
# 	return render (request=request, template_name="main/register.html", context={"register_form":form})

# Create your views here.
