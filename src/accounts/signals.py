from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.models import User, Plan

@receiver(post_save, sender=User)
def create_user_plan(sender, instance, created, **kwargs):
    if created:
        Plan.objects.create(user=instance)
