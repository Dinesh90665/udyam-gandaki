from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import WorkerProfile
#Only when new user is created
@receiver(post_save, sender=User)#run the following functions after user saved
def create_worker_profile(sender, instance, created, **kwargs): # insatnce is User just was saved
    if created:#True only if this User was newly created.
        WorkerProfile.objects.create(user=instance) #automatically created profile


@receiver(post_save, sender=User)#Every time user is saved
def save_worker_profile(sender, instance, **kwargs):#Saves/updates the profile every time the user is saved
    instance.workerprofile.save()
#User registers → User object created → this signal runs → creates a worker profile:
