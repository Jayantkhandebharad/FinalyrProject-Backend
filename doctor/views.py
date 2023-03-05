from django.shortcuts import render
from .models import doctor
import datetime

# Create your views here.

def register_doctor(request):
	return render(request,'register_doctor.html')

def findby_spec(request):
	return render(request,'finddoc.html')

def register_request_doctor(request):
	if(request.method=='get'):
		return render(request,'register_request_denied.html',{'message':'Improper request'})
	else:
		print("proper request")
	email_id=request.POST.get('email')
	if(doctor.objects.filter(email_id=email_id)):
		u=doctor.objects.filter(email_id=email_id)       
		return render(request,'register_request_denied.html',{'message':'User already exist'})
	names=request.POST.get('fname')
	lastname=request.POST.get('lname')	
	address=request.POST.get('addr')
	mob=request.POST.get('phone')
	password=request.POST.get('pasw')
	doct=doctor(password=password,name=names,lname=lastname,email_id=email_id,address=address,mob_no=mob,date=datetime.date.today())
	doct.save()
    #return render(request,'register_request_denied.html',{'message':'Improper request'})
	return render(request,'register_request.html',{'name':names})
    

def doc_list(request):
    docts=list(doctor.objects.all())
    doc=[]
    for e in docts:
        doc.append(e)
    return render (request,'doc_list.html',{'docts':docts})

def listby_spec(request):
	spec=request.POST.get('speciality')
	docts=list(doctor.objects.all())
	doc=[]
	for d in docts:
		if(d.Speciality==spec):
			doc.append(d)
	return render (request,'doc_list.html',{'docts':doc})