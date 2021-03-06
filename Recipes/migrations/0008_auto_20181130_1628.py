# Generated by Django 2.1.3 on 2018-11-30 21:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Recipes', '0007_recette_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_ingredient', models.CharField(max_length=200)),
                ('quantity', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='choice',
            name='recette',
        ),
        migrations.AlterField(
            model_name='recette',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.AddField(
            model_name='ingredient',
            name='recette',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Recipes.Recette'),
        ),
    ]
