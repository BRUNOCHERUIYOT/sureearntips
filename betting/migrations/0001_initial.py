# Generated by Django 3.1.7 on 2021-09-24 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='daily_tip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('amount', models.IntegerField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('team1', models.CharField(max_length=200)),
                ('team2', models.CharField(max_length=200)),
                ('team1odds', models.CharField(max_length=5)),
                ('team2odds', models.CharField(max_length=5)),
                ('placed_bet', models.CharField(max_length=200)),
                ('odds_value', models.CharField(max_length=5)),
                ('game_day', models.DateTimeField()),
                ('history', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='special_fixed_tip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('amount', models.IntegerField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Tiptype',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('daily_tip', models.CharField(max_length=100)),
                ('weekend_tip', models.CharField(max_length=100)),
                ('special_fixed_tip', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
                ('phone', models.IntegerField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='weekend_tip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('amount', models.IntegerField(max_length=4)),
            ],
        ),
    ]
