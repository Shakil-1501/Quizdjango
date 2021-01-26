# Core Django imports.
from django.contrib.auth.models import User
from django.db import models
from PIL import Image
from image_optimizer.fields import OptimizedImageField
from ckeditor.fields import RichTextField

class Course(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='courses')
    title = models.CharField(max_length=250, null=False, blank=False, unique=True)
    
    

    def __str__(self):
        return self.title
choiceq=(('All question at a time','All at once'),
         ('One question at a time','One at once')   
            )
class Quiz(models.Model):
    Quizname = models.CharField(max_length=250, null=False, blank=False, unique=True)
    Quiztype = models.CharField(max_length=100,default="Graded Quiz")
    chooseview = models.CharField(max_length=100,choices=choiceq,blank=True)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    Availablefrom = models.DateTimeField(blank=True)
    Until = models.DateTimeField(blank=True)
    points = models.IntegerField(blank=True)
    Questions = models.IntegerField(blank=True) 



choice=(('Multiple choice','MCQ'),('Multiple correct','MCC'),('True or False','T/F'))
class Question(models.Model):
    course= models.ForeignKey(Course,on_delete=models.CASCADE)
    quiznumber = models.ForeignKey(Quiz,on_delete=models.CASCADE,blank=True)
    questiontype = models.CharField(max_length=100,choices=choice,default='Multiple choice')
    question = models.TextField(max_length=1000,blank=False)
    description = RichTextField(blank=True,null=True)
    answer =  models.IntegerField()
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length = 100 , blank = True )
    option4 = models.CharField(max_length = 100 , blank = True )
    points = models.IntegerField(default=5,blank=True) 
    
    img = OptimizedImageField(
        upload_to='pics',
        optimized_image_output_size=(500, 300),
        optimized_image_resize_method='cover',blank=True  
    )
    files = models.FileField(upload_to='Quiz/uploads', blank=True,max_length=254)

    def __str__(self):
        return self.question

    

class Responses(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    Questionid=models.ForeignKey(Question,on_delete=models.CASCADE)
    answer=models.IntegerField(blank=True)
    comments=models.TextField(max_length=1000,blank=True)


  
