# Generated by Django 2.0.7 on 2019-05-06 19:25

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0004_auto_20190413_1009'),
    ]

    operations = [
        migrations.AddField(
            model_name='idea',
            name='idea_proposal',
            field=tinymce.models.HTMLField(default='default', verbose_name='content'),
            preserve_default=False,
        ),
    ]