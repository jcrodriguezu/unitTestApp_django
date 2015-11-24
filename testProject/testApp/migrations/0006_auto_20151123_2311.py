# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0005_auto_20151123_2308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='books_borrowed',
            field=models.ManyToManyField(to='testApp.Book'),
        ),
    ]
