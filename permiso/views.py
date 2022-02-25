from django.db.models.query_utils import PathInfo
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.models import User,auth
from .forms import studentForm
from .models import Permission, Student,Lecturer
import smtplib
from email.message import EmailMessage
import pyautogui
import time
import pywhatkit
import datetime
from selenium.webdriver.common.keys import Keys
# Create your views here.
var=str()
m=str()
g=str()
def dash(request):
    a=0
    n=0
    x=Permission.objects.all()
    k=len(x)
    for i in x:
        if i.grant=="grant":
            a=a+1
        else:
            n=n+1
    data=[a,n]
    label=['Granted','Not Granted']
    return render(request,"dashboard.html",{'data':data,'label':label,'n':k})
def fun(request):
    x=Permission.objects.all()
    data=[]
    for i in x:
        data.append(
                    {
                        'stu':i.stu,
                        'subject':i.subject,
                        'req':i.req,
                        'img':i.img,
                        'grant':i.grant,
                    }
                )
    if request.method=="POST":
        y=request.POST['studentname']
        p=Permission.objects.all()
        for i in p:
            if(y==i.stu and i.grant=="Not seen"):
                i.grant="grant"
                i.save()
                break 
        
        print(request.POST['studentname'])
        return render(request,"authority.html",{'data':data})
    else:
        return render(request,"authority.html",{'data':data})
    
def login(request):
    if(request.method== "POST" ):
        username=request.POST['username']
        password=request.POST['password']
        s=Student.objects.all()
        l=Lecturer.objects.all()
        flag=0
        studata=[]
        for i in s:
            if(i.username ==username and i.password == password ):
                flag=1
                global var 
                
                var=i.name
                print(var)
        if flag==0 :
            for i in l:
                if(i.username ==username and i.password == password ):
                    flag=2
                    global var2
                    var2=i.name
                    print(var2)
                    break 
        if (flag==1):
            data=[]
            for i in l:
                data.append(
                    {   
                        'name':i.name
                         
                    }
                )
            
            for j in s:
                if(j.name==var):
                    name=j.name
                    phno=j.phno
                    email=j.username
                    dep=j.dept
                    img=i.img

                    break
    
            return render(request,"studentprofile(1).html",{'data':data,'name':name,'email':email,'phno':phno,'dep':dep,'img':img})
        elif (flag==2):
            x=Permission.objects.all()
            data=[]
            for i in x:
                if(i.grant!="grant"):
                    data.append({
                        'stu':i.stu,
                        'subject':i.subject,
                        'req':i.req,
                        'img':i.img,
                        'grant':i.grant,
                    })
            
            for j in l:

                if(j.name==var2):
                    name=j.name
                    phno=j.phno
                    email=j.username
                    dep=j.dept
                    img=i.img

                    break

            return render(request,"authority.html",{'data':data,'name':name,'phno':phno,'email':email,'dept':dep,'img':img})
        else:
            return render(request,"login.html",{'message':'Invalid Credentials'})
    else:
        return render(request,"login.html")

var=var
def student(request):
    if request.method=="POST":
        name=request.POST['username']
        username=request.POST['email']
        dept=request.POST['dept']
        phno=request.POST['ph']
        img=request.POST['img']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if(password1==password2):
            t=Student.objects.create(name=name,username=username,dept=dept,phno=phno,img=img,password=password1)
            t.save()
            return render(request,"login.html")
        else:
            return render(request,"student.html",{'message':'passwords not matching'})
             
        
    else:
        return render(request,"student.html")

def personnel(request):
    if request.method=="POST":
        name=request.POST['username']
        username=request.POST['email']
        dept=request.POST['dept']
        phno=request.POST['ph']
        img=request.POST['img']
        verify=request.POST['verify']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if(password1==password2):
            t=Lecturer.objects.create(name=name,username=username,dept=dept,phno=phno,img=img,password=password1,verify=verify)
            t.save()
            return render(request,"login.html")
        else:
            return render(request,"Personnel.html",{'message':'passwords not matching'})
             
        
    else:
        return render(request,"Personnel.html")


def middle(request):
    if(request.method=='POST'):

        # x=request.POST['medium']
        # if(x=="mail"):
        email_alert("You got a new request!","Check your Permiso inbox",m)
        return render(request, "studentprofile(1).html")
    else:
        return render(request, "studentprofile(1).html")
        



def notify(request):
    if(request.method=="POST"):
        print(request.POST['selected'])
        if(request.POST['selected'] == "email"):
            n=request.POST['adminname']
            l=Lecturer.objects.all()
            email_alert("hey", "hello world",m)
            return render(request,"studentprofile(1).html")
        else:
            current_time=datetime.datetime.now()
            hr=current_time.hour
            min=current_time.minute
            x=Lecturer.objects.all()
            for i in x:
                if(i.name==g):
                    y=i.phno
                    break
            print(hr)
            print(min) 
            what(y,hr,min+2)
            return render(request,"studentprofile(1).html")
            
    else:
         return render(request,"studentprofile(1).html")

def gmail(request):
    if(request.method=="POST"):
        stu=var
        subject=request.POST['subject']
        req=request.POST['request']
        img=request.POST['imagefile']
        n=request.POST['adminname']
        global g
        g=n  
        p=Permission.objects.create(stu=stu,subject=subject,req=req,img=img)
        p.save()
        l=Lecturer.objects.all()
        for i in l:
            if i.name == n:
                global m
                m=i.username
                break
        
        return render(request,"middle.html")
    else:
        return render(request,"studentprofile(1).html")




def email_alert(subject,body,to):
    msg=EmailMessage()
    msg.set_content(body)
    msg['subject']=subject
    msg['to']=to
    

    user = "permisovnrvjiet@gmail.com"
    msg['from']= user
    password="yhagvyuhhfotjcaz"

    server=smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(user,password)
    server.send_message(msg)

    server.quit()
def what(ph,hr,min):
    pywhatkit.sendwhatmsg("+91"+str(ph),"Please check your permiso inbox",hr,min)
    time.sleep(100)
    pyautogui.click(1778,964)


def approved(request):
    p=Permission.objects.all()
    l=Lecturer.objects.all()
    for j in l:
                if(j.name==var2):
                    name=j.name
                    phno=j.phno
                    email=j.username
                    dep=j.dept
                    img=j.img

                    break

    data=[]
    for i in p:
        if(i.grant=="grant"):
            data.append({'stu':i.stu,'req':i.req,'subject':i.subject})
            
    return render(request,"approved.html",{'data':data,'name':name,'phno':phno,'email':email,'dept':dep,'img':img})




