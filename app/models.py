from django.db import models

# Create your models here.
class Student(models.Model):
    sid=models.IntegerField(primary_key=True)
    sname=models.CharField(max_length=125)
    email=models.EmailField(default='charanbkumar25@gmail.com')
    phone=models.CharField(max_length=100)
    def __str__(self):
        return self.sname

class Topic(models.Model):
    
    topic_name=models.CharField(max_length=100,primary_key=True)
    def __str__(self):
        return self.topic_name
class WebPage(models.Model):
    topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    url=models.URLField()
    email=models.EmailField(default='charanbkumar25@gmail.com')
    def __str__(self):
        return self.name
class AccessRecord(models.Model):
    name=models.ForeignKey(WebPage,on_delete=models.CASCADE)
    author=models.CharField(max_length=100)
    date=models.DateField() 
    def __str__(self):
        return self.author