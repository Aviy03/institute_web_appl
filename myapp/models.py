from django.db import models
import uuid

# Create your models here.

class Course(models.Model):
	courseno=models.IntegerField(primary_key= True)
	coursename=models.CharField(max_length=30)
	duration=models.IntegerField()
	fees=models.IntegerField()
	class Meta:
		db_table='Course'

class Batch(models.Model):
	batchno=models.IntegerField(primary_key= True)
	batchname=models.CharField(max_length=30)
	batchtime=models.IntegerField()
	maxstudents=models.IntegerField()
	currentstu=models.IntegerField()
	class Meta:
		db_table='Batch'

class Admin(models.Model):
	adminid=models.IntegerField(primary_key= True)
	adminname=models.CharField(max_length=30)
	adminpass=models.CharField(max_length=30)
	class Meta:
		db_table='Admin'

class Query(models.Model):
	queryid=models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False)
	qname=models.CharField(max_length=30)
	qemail=models.CharField(max_length=30)
	qphone=models.IntegerField()
	query=models.CharField(max_length=300)
	class Meta:
		db_table='Query'