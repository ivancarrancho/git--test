# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_children'),
    ]

    operations = [
        migrations.AlterField(
            model_name='children',
            name='mother',
            field=models.ForeignKey(related_name='children', to='app.Wife'),
            preserve_default=True,
        ),
    ]
