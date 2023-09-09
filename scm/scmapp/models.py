from django.db import models

class User(models.Model):
    uid=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    gender=models.CharField(max_length=10)
    contact=models.CharField(max_length=12)
    password=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book_event(models.Model):
    bid=models.AutoField(primary_key=True)
    uid=models.IntegerField()
    name=models.CharField(max_length=100)
    date=models.DateField()
    time=models.TimeField()
    mobile=models.IntegerField(max_length=10)
    def __str__(self):
        return self.name


class Admin(models.Model):
    aid=models.AutoField(primary_key=True)
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    password=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Event(models.Model):
    event_id=models.AutoField(primary_key=True)
    event_name=models.CharField(max_length=500)
    event_date=models.DateField()
    event_time=models.TimeField()
    duration=models.CharField(max_length=100)
    def __str__(self):
        return self.event_name