from multiprocessing.spawn import import_main_path
from django.db.models.signals import post_save, post_delete
from .models import Profile
from django.contrib.auth.models import User


def createProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user
        )





post_save.connect(createProfile, sender=User)