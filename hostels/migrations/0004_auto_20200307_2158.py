# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-03-07 21:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostels', '0003_auto_20200307_2152'),
    ]

    operations = [
        migrations.RenameField(
            model_name='roomtype',
            old_name='price',
            new_name='price1',
        ),
        migrations.RenameField(
            model_name='roomtype',
            old_name='roomtype',
            new_name='roomtype1',
        ),
        migrations.AddField(
            model_name='roomtype',
            name='price2',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='roomtype',
            name='price3',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='roomtype',
            name='price4',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='roomtype',
            name='roomtype2',
            field=models.CharField(blank=True, choices=[('1 in 1', '1 in 1'), ('2 in 1', '2 in 1'), ('3 in 1', '3 in 1'), ('4 in 1', '4 in 1')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='roomtype',
            name='roomtype3',
            field=models.CharField(blank=True, choices=[('1 in 1', '1 in 1'), ('2 in 1', '2 in 1'), ('3 in 1', '3 in 1'), ('4 in 1', '4 in 1')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='roomtype',
            name='roomtype4',
            field=models.CharField(blank=True, choices=[('1 in 1', '1 in 1'), ('2 in 1', '2 in 1'), ('3 in 1', '3 in 1'), ('4 in 1', '4 in 1')], max_length=100, null=True),
        ),
    ]
