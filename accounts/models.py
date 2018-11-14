from decimal import Decimal

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='user',on_delete=models.CASCADE,)
    gender = models.CharField(max_length=140)
    height = models.DecimalField(default=Decimal('000.0'),max_digits=5, decimal_places=1)
    weight = models.DecimalField(default=Decimal('000.0'),max_digits=5, decimal_places=1)
    city = models.CharField(max_length=140, blank=True, default='')

    def __str__(self):
        return 'Profile of user: {}'.format(self.user.username)


def create_profile(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        user_profile = UserProfile(user=user)
        user_profile.save()


post_save.connect(create_profile, sender=User)
