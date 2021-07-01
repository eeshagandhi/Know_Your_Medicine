from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.urls import reverse
# Create your models here.

class medicine_data(models.Model):
    SNo=models.IntegerField(blank='True')
    Disease=models.CharField(max_length=100,blank='True')
    Prescribed_medicine=models.CharField(max_length=100,blank='True')
    Dosage= models.CharField(max_length=300, blank='True')
    Side_Effects=models.CharField(max_length=500,blank='True')
    Patient_Review=models.CharField(max_length=10, blank='True')
    Price=models.IntegerField(blank='True')
    Feedback=models.TextField(max_length=500, blank='True')

class comment(models.Model):
    med=models.ForeignKey(medicine_data, related_name='comments', on_delete=models.CASCADE)  
    name=models.CharField(max_length=255)
    body=models.TextField()
    def __str__(self):
        return '%s-%s' % (self.med.Prescribed_medicine, self.name)
    def get_absolute_url(self):
        return reverse('check')

class Category(models.Model):
    name=models.CharField(max_length=255)
    def  __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('blog')
      
class post(models.Model):
    title=models.CharField(max_length=255)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    body=models.TextField()
    category=models.CharField(max_length=255, default='physical health')
    likes=models.ManyToManyField(User, related_name='blogposts')

    def total_likes(self):
        return self.likes.count()
    def  __str__(self):
        return self.title + ' | ' + str(self.author)
    def get_absolute_url(self):
        return reverse('blog')

    