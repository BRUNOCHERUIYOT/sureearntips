# Generated by Django 3.1.7 on 2021-09-24 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('betting', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daily_tip',
            name='amount',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='users',
            name='phone',
            field=models.IntegerField(),
        ),
    ]
