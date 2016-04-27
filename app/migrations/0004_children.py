# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_husband_wife'),
    ]

    operations = [
        migrations.CreateModel(
            name='Children',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField(max_length=3)),
                ('mother', models.ForeignKey(to='app.Wife')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
