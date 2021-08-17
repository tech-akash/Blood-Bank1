from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.enums import Choices
from django.contrib.auth.models import User
# Create your models here.

class Donate(models.Model):
    name=models.CharField( 'Name of Donar',max_length=100,null=False)
    address=models.CharField('Address',max_length=200,null=False)
    phoneno=models.CharField('Phone Number',max_length=10,null=False)
    age=models.IntegerField('Age',null=False)
    GENDER=(('M','Male'),
    ('F','Female'),
    ('T','Trans'))
    gender=models.CharField('Gender',max_length=1,choices=GENDER,null=False)
    BLOODGROUP=(
    ('A+','A+'),
    ('A-','A-'),
    ('O+','O+'),
    ('O-','O-'),
    ('B+','B+'),
    ('B-','B-'),
    ('AB-','AB-'),
    ('AB+','AB+')
    )
    bloodgroup=models.CharField('Blood Group',max_length=3,choices=BLOODGROUP,null=False)
    dayofdonate=models.DateField('Day of Donating',null=True,blank=True)
    STATUS=(
    ('Pending','Pending'),
    ('Accepted','Accepted'),
    ('Donated','Donated'),
    ('Rejected','Rejected')
    )
    status=models.CharField('Status',choices=STATUS,default='Pending',max_length=20,null=True,blank=True)
    def __str__(self):
        return self.name

class Accept(models.Model):
    name=models.CharField( max_length=100,null=False)
    address=models.CharField('Address',max_length=200,null=False)
    phoneno=models.CharField('Phone Number',max_length=10,null=False)
    age=models.IntegerField('Age',null=False)
    GENDER=(('M','Male'),
    ('F','Female'),
    ('T','Trans'))
    gender=models.CharField('Gender',max_length=1,choices=GENDER,null=False)
    BLOODGROUP=(
    ('A+','A+'),
    ('A-','A-'),
    ('O+','O+'),
    ('O-','O-'),
    ('B+','B+'),
    ('B-','B-'),
    ('AB-','AB-'),
    ('AB+','AB+')
    )
    bloodgroup=models.CharField('Blood Group',max_length=3,choices=BLOODGROUP,null=False)
    dayofaccept=models.DateField('Day of Accepting',null=True,blank=True)
    STATUS=(
    ('Pending','Pending'),
    ('Accepted','Accepted'),
    ('GotIt','GotIt'),
    ('Rejected','Rejected')
    )
    status=models.CharField('Status',choices=STATUS,default='Pending', max_length=20,null=True,blank=True)
    def __str__(self):
        return self.name

class Customer(models.Model):
    user=models.OneToOneField(User,null=True,blank=True,on_delete=CASCADE)
    username=models.CharField('Username',max_length=200,primary_key=True)
    name=models.CharField( max_length=100,null=True,blank=True)
    email=models.EmailField('Email',null=True,blank=True,default='abc@gmail.com')
    address=models.CharField('Address',max_length=200,null=True,blank=True)
    phoneno=models.CharField('Phone Number',max_length=10,null=True,blank=True)
    age=models.IntegerField('Age',null=True,blank=True)
    prescription=models.ImageField(null=True,blank=True)
    GENDER=(('M','Male'),
    ('F','Female'),
    ('T','Trans'))
    gender=models.CharField('Gender',max_length=1,choices=GENDER,null=True,blank=True)
    BLOODGROUP=(
    ('A+','A+'),
    ('A-','A-'),
    ('O+','O+'),
    ('O-','O-'),
    ('B+','B+'),
    ('B-','B-'),
    ('AB-','AB-'),
    ('AB+','AB+')
    )
    bloodgroup=models.CharField('Blood Group',max_length=3,choices=BLOODGROUP,null=True,blank=True)
    dayofaccept=models.DateField('Day of Accepting',null=True,blank=True)
    NEED=(('None','None'),
        ('Acceptor','Acceptor'),
    ('Donator','Donator'),)
    need=models.CharField('Need',choices=NEED,default='None',null=True,blank=True,max_length=20)
    STATUS=(
    ('Pending','Pending'),
    ('Accepted','Accepted'),
    ('GotIt','GotIt'),
    ('Rejected','Rejected')
    )
    status=models.CharField('Status',choices=STATUS,default='Pending', max_length=20,null=True,blank=True)
    
