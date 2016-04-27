# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20150914_2009'),
    ]

    operations = [
        migrations.CreateModel(
            name='Husband',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('age', models.IntegerField(max_length=3)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Wife',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('age', models.IntegerField(max_length=3)),
                ('name', models.CharField(max_length=50)),
                ('husband', models.OneToOneField(to='app.Husband')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
