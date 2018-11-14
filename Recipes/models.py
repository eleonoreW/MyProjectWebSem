from django.db import models
from django.forms import ModelForm
# the following lines added:
import datetime

from django.forms import forms
from django.utils import timezone


class Recette(models.Model):
    recette_description = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.recette_description

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    recette = models.ForeignKey(Recette, on_delete=models.DO_NOTHING, )
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

