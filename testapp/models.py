from django.db import models

# Create your models here.

class Employee(models.Model):
    e_no = models.IntegerField()
    e_name = models.CharField(max_length=64)
    e_sal = models.FloatField()
    e_address = models.CharField(max_length=64)
    
    def __str__(self):
        return self.e_name

class Job(models.Model):
    post_name = models.CharField(max_length=89)
    posting_date = models.DateField()
    location = models.CharField(max_length=64)
    salary = models.IntegerField()
    qualification = models.CharField(max_length=64)
    
    def __str__(self):
        return self.post_name

class Book(models.Model):
    number = models.IntegerField()
    title = models.CharField(max_length=67)
    author = models.CharField(max_length=64)
    published_date = models.DateField()
    
    def __str__(self):
        return self.title

class Customer(models.Model):
    phoneNumber = models.IntegerField()
    name = models.CharField(max_length=67)
    age = models.IntegerField()
    mailId = models.EmailField()
    
    def __str__(self):
        return self.name