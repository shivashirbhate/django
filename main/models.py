from django.db import models

# Create your models here.

class Classes(models.Model):
    id = models.IntegerField(primary_key=True)
    className = models.CharField(max_length=50)
    def __str__(self):
        return self.className

class Student(models.Model):
    sRollNo = models.AutoField(primary_key=True)
    sName = models.CharField(max_length=255)
    sClass = models.ForeignKey(Classes, on_delete=models.CASCADE)
    snumber = models.CharField(max_length=16)
    pub_date = models.DateTimeField(auto_now_add=True)
    
    # @classmethod
    # def create(cls,argdata):
    #     return cls(sName=argdata['Name'], sClass=argdata['clss'], snumber=argdata['number'])

    
    def __str__(self):
        return self.sName

