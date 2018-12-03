from decimal import Decimal

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='user', on_delete=models.CASCADE, )
    FEMME = 'Femme'
    HOMME = 'Homme'
    INDEFINI = 'Indefini'
    GENDER = (
        (FEMME, 'F'),
        (HOMME, 'H'),
        (INDEFINI, 'I')
    )
    gender = models.CharField(max_length=1,
        choices=GENDER,
        default=INDEFINI)
    HYPERPROTEINE = 'hyperprotéiné'
    PROTEINE = 'protéiné'
    HYPOCALORIQUE = 'hypocalorique'
    DISSOCIE = 'Dissocié'
    VEGAN = 'végétarien'
    ANTICELLULITE = 'anticellulite'
    SANSSEL = 'sans sel'
    HYPOGLUCIDIQUE = 'hypoglucidique'
    DETOX = 'detox'
    AUCUN = 'aucun régime'
    DIETS= (
        (HYPERPROTEINE, 'HYPP'),
        (PROTEINE, 'PROT'),
        (HYPOCALORIQUE, 'HYPC'),
        (DISSOCIE, 'DISS'),
        (VEGAN, 'VEGE'),
        (ANTICELLULITE, 'ANTI'),
        (SANSSEL, 'SSEL'),
        (HYPOGLUCIDIQUE, 'HYPG'),
        (DETOX,'DETX'),
        (AUCUN,'NONE')
    )
    diet = models.CharField(max_length=4,
                              choices=DIETS,
                              default=AUCUN)
    height = models.DecimalField(default=Decimal('000.0'), max_digits=5, decimal_places=1)
    weight = models.DecimalField(default=Decimal('000.0'), max_digits=5, decimal_places=1)
    city = models.CharField(max_length=140, blank=True, default='')
    birthday = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.user.username


def create_profile(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        user_profile = UserProfile(user=user)
        user_profile.save()


post_save.connect(create_profile, sender=User)
