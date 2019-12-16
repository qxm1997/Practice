from django.db import models

# Create your models here.

class Plan(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField()
    image = models.ImageField(upload_to='img')
    lesson_count = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class User(models.Model):
    nickname = models.CharField(max_length=32)
    email = models.EmailField()
    password = models.CharField(max_length=32)
    plan = models.ForeignKey(to=Plan,on_delete=models.CASCADE)

    def __str__(self):
        return self.nickname

class Lesson(models.Model):
    lable = models.CharField(max_length=32)
    picture = models.ImageField(upload_to='img')
    show_number = models.IntegerField()
    plan = models.ManyToManyField(to=Plan)

    def __str__(self):
        return self.lable
