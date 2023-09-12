import datetime
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from .models import User, Book_event, Admin, Event
from django.contrib.auth import authenticate, login, logout
import random


def index (request):
    return render(request, 'index.html')
def home(request):
    return render(request, 'home.html')

def user_reg (request):
    return render(request, 'user_reg.html')


def user_reg_data (request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        gender=request.POST.get('gender')
        contact=request.POST.get('contact')
        password=request.POST.get('password')
        record=User(name=name, email=email, gender=gender, contact=contact, password=password)
        record.save()
        para={"done":"Profile Created!"}
    return render(request, 'userpage.html', para)

def user_loging(request):
    if request.method=='POST':
        name=request.POST.get('name')
        password=request.POST.get('password')

        try:
            user=User.objects.get(name=name)
            if user.password==password:
                request.session['u_name']=name
                return userpage(request)
            else:
                para={'msg':'password is wrong'}
                return render(request, 'user_login.html',para)
        except Exception as e:
            para={'msg':'user does not exist'}
            return render(request, 'user_login.html', para)
def user_login (request):
    if 'u_name' in request.session:
        para={'name':request.session.get('u_name')}
        return render(request, 'userpage.html', para)
    else:
        para={'msg':"Something went wrong"}
        return render(request, "user_login.html")
    
def userpage(request):
    if "u_name" in request.session:
        name=request.session.get('u_name')
        para={"name":name}
        return render(request, 'userpage.html', para )
    else:
        para={'msg':'Login First'}
        return render(request, 'user_login.html',para )
    

def book_event(request):
    return render(request, 'book_event.html')

def book_event(request):
    if "u_name" in request.session:
        para={'date':datetime.date.today}
        return render (request, 'book_event.html', para)
    else:
        para={'status':'You need to log in!'}
        return render(request, 'user_login.html', para)
    
def booked_event_data(request):
    if request.method=="POST":
        date=request.POST.get('date')
        time=request.POST.get('time')
        try:
            book=Book_event.objects.get(date=date)
            para={'status':'Please selact another date!'}
            return render(request, 'book_event.html', para)
        except Exception as e:
            # fetching users details through session
            user=User.objects.get(name=request.session.get('u_name'))
            # fetching uid,contact and name from user
            book=Book_event(uid=user.uid, name=user.name, time=time, date=date, mobile=user.contact)
            book.save()
            para={'status':'Your event has been booked! Thank You!'}
            return render(request, 'userpage.html', para)
    else:
        para={'error_msg':'Something went wrong:( please try again'}
        return render(request, 'userpage.html', para )
    
def user_show_events(request):
    if 'u_name' in request.session:
        events=Event.objects.all()
        para={'data':events}
        return render(request, 'user_show_events.html', para )

def admin_login(request):
    if 'a_name' in request.session:
        para={'name':request.session.get('a_name')}
        return render(request, 'adminhome.html', para)
    return render(request, 'admin_login.html')

def admin_loging(request):
    if request.method=="POST":
        aname=request.POST.get('aname')
        password=request.POST.get('password')

        try:
            admin=Admin.objects.get(name=aname)
            if admin.password==password:
                request.session['a_name']=aname
                return render(request,'adminhome.html')
            else:
                para={'msg':'Incorrect Password!'}
                return render(request, 'admin_login.html', para)
        except Exception as e:
            para={"status":"admin does not exist"}
            return render(request, 'admin_login.html', para)


def adminhome(request):
    if 'a_name'in request.session:
        aname=request.session.get('a_name')
        para={'name':aname}
        return render(request, 'adminhome.html',para)
    else:
        para={'status':'Login first'}
        return render(request, 'admin_login.html',para)
    
def adminhome(request):
    if 'a_name'in request.session:
        return render(request, 'adminhome.html')
    else:
        para={'status':'Login first'}
        return render(request, 'admin_login.html',para)
    
def booked_events_admin(request):
    if 'a_name'in request.session:
        booking=Book_event.objects.all()
        para={'data':booking}
        return render(request, 'booked_events_admin.html', para )
    else:
        para={'msg':'You need to log in!'}
        return render (request, 'admin_login.html',para)


def admin_event (request):
    if 'a_name' in request.session:
        events=Event.objects.all()
        para={'data':events}
        return render (request, 'admin_event.html', para)
    else:
        para={'msg':'You need to log in!'}
        return render (request, 'admin_login.html',para)
    
def event_delete(request):
    if 'a_name' in request.session:
        event_id=request.GET.get('event_id')
        Event.objects.filter(event_id=event_id).delete()
        para={'status':'Event deleted Successfully'}
        return render(request, 'admin_event.html',para)


def add_event(request):
    if 'a_name' in request.session:
        para={'edate':datetime.date.today}
        return render (request, 'add_event.html',para)
    else:
        para={'msg':'You need to log in!'}
        return render (request, 'admin_login.html',para)
    
def add_event_data(request):
    if request.method=="POST":
        ename=request.POST.get('event_name') 
        edate=request.POST.get('event_date')
        etime=request.POST.get('event_time')
        eduration=request.POST.get('duration')
        event=Event(event_name=ename, event_date=edate, event_time=etime, duration=eduration)
        event.save()
        para={'status':'Event added successfully!'}
        return render(request, 'admin_event.html', para)
    else:
        para={'error':'something went wrong please try again!'}
        return render (request, 'add_event.html', para)
    
def user_logout(request):
    if 'u_name' in request.session:
        del request.session['u_name']
        para={'logout_msg':'Logged out succesfully'}
        return render(request, "user_login.html",para)
    else:
        para={'msg':'Login first'}
        return render(request, "user_login.html",para)

def admin_logout(request):
    if 'a_name' in request.session:
        del request.session['a_name']
        para={'logout_msg':'Logged out succesfully'}
        return render(request, "admin_login.html",para)
    else:
        para={'msg':'Login first'}
        return render(request, "admin_login.html", para)
    
def send_email(request):
    return render(request, "send_email.html")
    
def email_send(request):
    return render(request, "send_email.html")

def verify_otp(request):
    return render(request, "verify_otp.html")

def send_email_1(request):
    email=request.POST.get("email")
    subject="Forget Password"
    otp=random.randint(1000, 9999)
    msg="Your OTP is: "
    msg+=str(otp)
    email_from=settings.EMAIL_HOST_USER
    to=(email,)
    send_mail(subject, msg, email_from, to)
    para={'otp':otp, 'email':email}
    return render(request, "verify_otp.html", otp)

def otp_check(request):
    myotp=request.POST.get("myotp")
    otp=request.POST.get("otp")
    emailid=request.POST.get('emailid')
    if (myotp==otp):
        para={'emailid':emailid}
        return render(request, "change_pass.html", para)
    else:
        para={'otp':myotp, "emailid":emailid, 'msg':'Please enter valid OTP'}
        return render(request, "verify_otp.html")
    
def change_pass(request):
    return render(request, "change_pass.html")

def Updated_pass(request):
    new_password=request.POST.get('pass')
    user_email=request.POST.get('email')
    user=User.objects.get(email=user_email)
    user.password=new_password
    user.save()
    para={'update':'Password updated successfully! '}
    return render(request, "user_login.html",para)
    



    
