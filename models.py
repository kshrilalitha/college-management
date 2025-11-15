from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=40)
    usn=models.IntegerField(unique=True)
    gender=models.CharField(max_length=10)

class subject(models.Model):
     name=models.CharField(max_length=40)
     subject_id=models.IntegerField(unique=True)
     
class Enrollment(models.Model):
    enroll_id=models.IntegerField(primary_key=True)
    usn=models.ForeignKey(Student,on_delete=models.CASCADE)
    subject_id=models.ForeignKey(subject,on_delete=models.CASCADE)
        
        

# Create your models here.
