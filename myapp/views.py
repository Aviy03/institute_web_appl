from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from myapp.models import Course
from myapp.models import Admin
from myapp.models import Query

# Create your views here.

def index(request):
	return render(request,'index2.html')

def login(request):
	return render(request,'login.html')

@csrf_exempt
def admincourse(request):
	data = Course.objects.all()
	stu = {
	    "student_number": data
	}
	return render(request,"admincourse.html", stu)

def adminpanel(request):
	return render(request,'adminpage.html')

def coursesave(request):
	return render(request,'coursesave.html')

def coursedel(request):
	return render(request,'edelete.html')

def coursesearch(request):
	return render(request,'esearch.html')

def adminbatch(request):
	return render(request,'adminbatch.html')

def adminstudent(request):
	return render(request,'adminstudent.html')

@csrf_exempt
def adminquery(request):
	data = Query.objects.all()
	stu = {
	    "student_number": data
	}
	return render(request,"adminquery.html", stu)

def querypage(request):
	return render(request,'querypage.html')

def studentsave(request):
	return render(request,'studentsave.html')

def studentreg(request):
	data = Course.objects.all()
	stu = {
	    "student_number": data
	}
	return render(request,"studentregister.html", stu)


@csrf_exempt
def CoursedataSave(request):
	a=request.POST.get("cid")
	b=request.POST.get("cname")
	c=request.POST.get("cdur")
	d=request.POST.get("cfee")
	obj=Course(courseno=a,coursename=b,duration=c,fees=d)
	obj.save()
	msg="<script> alert('Data Saved');window.location.href='/admincourse/';</script>"
	return HttpResponse(msg)

@csrf_exempt
def showqueries(request):
	data = Query.objects.all()
	stu = {
	    "student_number": data
	}
	return render(request,"adminpage.html", stu)

@csrf_exempt
def loginverify(request):
	a=request.POST.get('adminid')
	b=request.POST.get('adminpass')
	ob=Admin.objects.filter(adminid=a, adminpass=b)
	if not ob:
		msg="<script> alert('Wrong Details');window.location.href='/login/';</script>"
	else:
		name=''
		ob1=Admin.objects.filter(adminid=a)
		for y in ob1:
			name=y.adminname
		return render(request,'adminpage.html',{"name":name})
	return HttpResponse(msg)


@csrf_exempt
def querydatasave(request):
	a=request.POST.get("name")
	b=request.POST.get("email")
	c=request.POST.get("phone")
	d=request.POST.get("message")
	obj=Query(qname=a,qemail=b,qphone=c,query=d)
	try:
		obj.save()
	except:
		msg="<script> alert('Wrong');window.location.href='/login/';</script>"
	return render(request,'index2.html')

@csrf_exempt
def Coursefind(request):
	a=request.POST.get("cid")
	data=Course.objects.filter(courseno=a)
	stu = {
	    "student_number": data
	}
	return render(request,"resultpage.html", stu)

@csrf_exempt
def coursedelete(request):
    a=request.POST.get("cid")
    obj=Course.objects.get(courseno=a)
    obj.delete()
    msg="<script> alert('Course Deleted');window.location.href='/admincourse/';</script>"
    return HttpResponse(msg)

def courseuppage(request):
	return render(request,'courseupdate.html')


@csrf_exempt
def courseupdate(request):
    a=request.POST.get("cid")
    b=request.POST.get("cname")
    c=request.POST.get("cdur")
    d=request.POST.get("cfee")
    obj=Course.objects.get(courseno=a)
    obj.coursename=b
    obj.duration=c
    obj.fees=d
    obj.save()
    msg="<script> alert('Course Updated');window.location.href='/admincourse/';</script>"
    return HttpResponse(msg)
