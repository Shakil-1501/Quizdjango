# Core Django imports.
from django.db import models
from django.contrib.auth.models import User
from .course_model import Course
from PIL import Image
from image_optimizer.fields import OptimizedImageField
from ckeditor.fields import RichTextField


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=100)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    marks = models.IntegerField(default=10)
    number_of_attempts = models.IntegerField(default=2)
    Attempts_left = models.IntegerField(default=1)
    Time_taken = models.IntegerField(default=30)
    

    def __str__(self):
        return f"{self.user.username}'s Profile"

 