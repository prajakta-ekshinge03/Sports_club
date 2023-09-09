from django.contrib import admin
from .models import User, Book_event , Admin, Event
# Register your models here.
admin.site.register(User)
admin.site.register(Book_event)
admin.site.register(Admin)
admin.site.register(Event)



