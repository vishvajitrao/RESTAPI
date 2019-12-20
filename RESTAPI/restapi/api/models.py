from django.db import models

# Create your models here.


class University(models.Model):
    university = models.CharField(max_length=100)

    class Meta:
        verbose_name = "University"
        verbose_name_plural = "Universities"

    def __str__(self):
        return self.university
 

Gender =  (
    ('Male','Male'),
    ('Female','Female'),
)

class Student(models.Model):
    id = models.CharField(max_length=10,primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    number = models.IntegerField()
   
    

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"

    def __str__(self):
        return self.first_name

