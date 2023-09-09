from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("", views.index),
    path('home', views.home, name='home'), 
    path("user_reg",views.user_reg, name='user_reg'),
    path('user_reg_data',views.user_reg_data,name='user_reg_data'),
    path('user_login',views.user_login,name='user_login'),
    path('user_loging',views.user_loging,name='user_loging'),
    path('userpage',views.userpage,name='userpage'),
    path('book_event',views.book_event, name='book_event'),
    path('booked_event_data', views.booked_event_data, name='booked_event_data'), 
    path('admin_login', views.admin_login, name='admin_login'),
    path('adminhome', views.adminhome, name='adminhome'),
    path('admin_loging', views.admin_loging, name='admin_loging'),
    path('booked_events_admin', views.booked_events_admin, name='booked_events_admin'),
    path('admin_event', views.admin_event, name='admin_event'),
    path('add_event', views.add_event, name='add_event'), 
    path('add_event_data', views.add_event_data, name='add_event_data'), 
    path('user_show_events', views.user_show_events, name='user_show_events'), 
    path('user_logout', views.user_logout, name='user_logout'),
    path('admin_logout', views.admin_logout, name='admin_logout'), 
    path('event_delete', views.event_delete, name='event_delete'), 
    path('email_send', views.email_send, name='email_send'),
    path('send_email_1', views.send_email_1, name='send_email_1'),
    path('send_email', views.send_email, name='send_email'),
    path('verify_otp', views.verify_otp, name='verify_otp'),
    path('otp_check', views.otp_check, name='otp_check'),
    path('change_pass', views.change_pass, name='change_pass'),
    path('Updated_pass', views.Updated_pass, name='Updated_pass'),
    
    
    

    
    

]
