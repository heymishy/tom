# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='roletofunction',
            name='description',
        ),
        migrations.RemoveField(
            model_name='roletofunction',
            name='name',
        ),
        migrations.RemoveField(
            model_name='roletofunction',
            name='status',
        ),
    ]
