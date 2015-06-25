# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hubs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hubs',
            name='hub_type',
            field=models.CharField(default=b'h', max_length=5, choices=[(b'h', b'Hub'), (b'c', b'Country Manager')]),
        ),
    ]
