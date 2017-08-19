# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-19 19:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarPark',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('num', models.IntegerField(default=0)),
                ('price', models.IntegerField(default=0)),
                ('address', models.CharField(max_length=50)),
                ('imageurl', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='CarToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carnum', models.CharField(max_length=50)),
                ('token', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ParkingTransaction',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('parkingLotID', models.CharField(max_length=50)),
                ('carnum', models.CharField(max_length=50)),
                ('timeStartParking', models.DateTimeField()),
                ('timeEndParking', models.DateTimeField(blank=True, null=True)),
                ('parkingLength', models.IntegerField(default=0)),
                ('paid', models.IntegerField(default=0)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='cartoken',
            unique_together=set([('carnum', 'token')]),
        ),
    ]
