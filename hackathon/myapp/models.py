from django.db import models


from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    ROLE_CHOICES = (
        ('worker', 'Worker'),
        ('employer', 'Employer'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username} ({self.role})"


from django.db import models
from django.contrib.auth.models import User

class Training(models.Model):
    title = models.CharField(max_length=200)
    provider = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title
    
class WorkerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    skills = models.CharField(max_length=200)
    certificate = models.FileField(upload_to='certificates/', blank=True, null=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username


class Job(models.Model):
    employer = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=100)
    pay_rate = models.CharField(max_length=50)
    posted_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


