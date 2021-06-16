# project-2/model.py


from django.db import models

Department = (('Maths', 'maths'),
              ('Science', 'Science'),
              ('sports', 'sports')
              )


# Create your models here.

class Subject(models.Model):
    subject_Type = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.subject_Type


class Questions(models.Model):
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    #Subject = models.CharField(max_length=50,choices='Department')
    Question = models.TextField(max_length=500, default='')
    option_1 = models.CharField(max_length=100, default='')
    option_2 = models.CharField(max_length=100, default='')
    option_3 = models.CharField(max_length=100, default='')
    option_4 = models.CharField(max_length=100, default='')
    Answer = models.CharField(max_length=100, default='')
    #Answer = models.IntegerField()

    def __str__(self):
        return self.Question


