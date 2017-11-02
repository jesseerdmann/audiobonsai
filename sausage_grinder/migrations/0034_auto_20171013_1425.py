# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-13 14:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sausage_grinder', '0033_merge_20170822_2222'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='followers_change',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='artist',
            name='followers_change_from_release',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='artist',
            name='followers_change_pct',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='artist',
            name='followers_change_pct_from_release',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='artist',
            name='orig_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='artist',
            name='orig_followers',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='artist',
            name='orig_pop',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='artist',
            name='pop_change',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='artist',
            name='pop_change_from_release',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='artist',
            name='pop_change_pct',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='artist',
            name='pop_change_pct_from_release',
            field=models.IntegerField(default=0),
        ),
    ]