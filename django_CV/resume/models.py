from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    profile = models.TextField()

class Work(models.Model):
    company = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    workdetail = models.TextField()

class Skill(models.Model):
    skill = models.CharField(max_length=100)

class Edu(models.Model):
    school = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    edudetail = models.TextField()

class EProfile(models.Model):
    profile = models.TextField()

class EWork(models.Model):
    company = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    workdetail = models.TextField()

class ESkill(models.Model):
    skill = models.CharField(max_length=100)

class EEdu(models.Model):
    school = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    edudetail = models.TextField()

class AcaOutput(models.Model):
    title = models.CharField(max_length=1000)
    author = models.CharField(max_length=100)
    journal = models.CharField(max_length=100)

class PracOutput(models.Model):
    workoutput = models.CharField(max_length=100)

class CSoutput(models.Model):
    href = models.CharField(max_length=1000)
    project = models.CharField(max_length=100)

class ECSoutput(models.Model):
    href = models.CharField(max_length=1000)
    project = models.CharField(max_length=100)