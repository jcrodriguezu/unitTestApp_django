# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0007_auto_20151123_2335'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='books_borrowed',
            new_name='books_lent',
        ),
    ]
