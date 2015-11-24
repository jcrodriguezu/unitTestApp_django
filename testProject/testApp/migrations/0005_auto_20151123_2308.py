# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0004_auto_20151118_2347'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='books_borrowed',
            field=models.ManyToManyField(to='testApp.Book', null=True),
        ),
        migrations.RemoveField(
            model_name='user',
            name='privileges',
        ),
        migrations.AddField(
            model_name='user',
            name='privileges',
            field=models.ForeignKey(default=1, to='testApp.Privileges'),
            preserve_default=False,
        ),
    ]
