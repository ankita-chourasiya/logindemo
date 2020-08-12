from django.shortcuts import render,redirect
from django.http import HttpResponse
from demo.models import Data

def login(request):
	return render(request,'demo/login.html')

def registration(request):
	return render(request,'demo/registartion.html')

def addData(request):
	d = Data(name=request.POST['name'],email=request.POST['email'],contact=int(request.POST['contact']),password=request.POST['psw'])
	d.save()
	return render(request,'demo/login.html',{'msg':'Registration successfully'})

def viewData(request):
	s=Data.objects.all()
	return render(request,'demo/viewdata.html',{'key':s})

def editData(request):
	s=Data.objects.get(pk=int(request.GET['q']))
	return render(request,'demo/editdata.html',{'key':s})

def deleteData(request):
	s=Data.objects.get(pk=int(request.GET['q']))
	s.delete()
	return HttpResponse("Record delete successfully")

def loginD(request):
	s=Data.objects.filter(email=request.POST["email"],password=request.POST["psw"])
	if (s.count()==0):
		return render(request,'demo/login.html',{'key':'Invalid Email or password'})
	else:
		request.session['ses']=request.POST['email']
		return render(request,'demo/loginDashboard.html')
	
def Dashboard(request):
	if('ses' not in request.session):
		return render(request,'demo/login.html')

	return render(request,'demo/loginDashboard.html')

def logout(request):
    del request.session['ses']
    return render(request,'demo/login.html')		