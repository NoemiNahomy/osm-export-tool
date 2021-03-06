# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-11 01:08
from __future__ import unicode_literals

from django.db import migrations
from utils.aoi_utils import simplify_geom

def resimplify(apps, schema_editor):
    Job = apps.get_model('jobs', 'Job')
    for job in Job.objects.all():
        job.simplified_geom = simplify_geom(job.the_geom,force_buffer=job.buffer_aoi)
        job.save()

class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0058_auto_20170703_2355'),
    ]

    operations = [
            migrations.RunPython(resimplify,reverse_code=lambda x,y:None)
    ]
