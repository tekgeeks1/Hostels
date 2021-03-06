# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-03-08 10:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hostels', '0005_auto_20200307_2241'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoomType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roomtype', models.CharField(blank=True, choices=[('1 in 1', '1 in 1'), ('2 in 1', '2 in 1'), ('3 in 1', '3 in 1'), ('4 in 1', '4 in 1')], max_length=100, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='bookroom',
            name='hostel',
        ),
        migrations.RemoveField(
            model_name='bookroom',
            name='user',
        ),
        migrations.RemoveField(
            model_name='hostel',
            name='price1',
        ),
        migrations.RemoveField(
            model_name='hostel',
            name='price2',
        ),
        migrations.RemoveField(
            model_name='hostel',
            name='price3',
        ),
        migrations.RemoveField(
            model_name='hostel',
            name='price4',
        ),
        migrations.AlterField(
            model_name='hostel',
            name='roomtype1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='OneInOne', to='hostels.RoomType'),
        ),
        migrations.AlterField(
            model_name='hostel',
            name='roomtype2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='TwoInOne', to='hostels.RoomType'),
        ),
        migrations.AlterField(
            model_name='hostel',
            name='roomtype3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ThreeInOne', to='hostels.RoomType'),
        ),
        migrations.AlterField(
            model_name='hostel',
            name='roomtype4',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='FourInOne', to='hostels.RoomType'),
        ),
        migrations.DeleteModel(
            name='BookRoom',
        ),
    ]
