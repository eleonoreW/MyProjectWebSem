from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm
# the following lines added:
import datetime

from django.forms import forms
from django.utils import timezone


class Recette(models.Model):
    recette_description = models.CharField(max_length=200)
    recette_instructions = models.TextField(max_length=1000,blank=True, null=True);
    pub_date = models.DateTimeField(auto_now_add=True, blank=True)
    nombre_part = models.IntegerField(default=0);
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING ,blank=True, null=True)
    nbCalories = models.BigIntegerField(default=0,blank=True, null=True)
    image = models.URLField(default='https://cb2.scene7.com/is/image/CB2/BlackClayDinnerPlate11inSHF16/?$web_product_hero$&161208101132&wid=625&hei=625',blank=True, null=True)

    def __str__(self):
        return self.recette_description

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Ingredient(models.Model):
    recette = models.ForeignKey(Recette, on_delete=models.DO_NOTHING, )
    id_ingredient = models.CharField(max_length=200)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.id_ingredient


class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    carbohydrates_100g = models.FloatField(blank=True, null=True)  # This field type is a guess.
    energy_100g = models.FloatField(blank=True, null=True)  # This field type is a guess.
    fat_100g = models.FloatField(blank=True, null=True)  # This field type is a guess.
    fiber_100g = models.FloatField(blank=True, null=True)  # This field type is a guess.
    #id_product = models.IntegerField(blank=True, null=True)
    ingredients_text = models.CharField(max_length=2083, blank=True, null=True)
    product_name = models.CharField(max_length=61, blank=True, null=True)
    proteins_100g = models.FloatField(blank=True, null=True)  # This field type is a guess.
    quantity = models.CharField(max_length=29, blank=True, null=True)
    sodium_100g = models.FloatField(blank=True, null=True)  # This field type is a guess.
    sugars_100g = models.FloatField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'product'
