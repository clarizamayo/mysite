# Generated by Django 3.2 on 2021-05-02 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dog',
            name='age',
            field=models.IntegerField(),
        ),
    ]
