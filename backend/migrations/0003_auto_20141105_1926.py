# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20141105_1917'),
    ]

    operations = [
        migrations.AddField(
            model_name='roletofunction',
            name='description',
            field=models.CharField(default='description', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='roletofunction',
            name='name',
            field=models.CharField(default='name', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='roletofunction',
            name='status',
            field=models.CharField(default='approved', max_length=255),
            preserve_default=False,
        ),
    ]
