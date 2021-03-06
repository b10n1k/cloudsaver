# Generated by Django 2.0.7 on 2018-08-08 16:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Idea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idea_title', models.CharField(max_length=30)),
                ('idea_text', models.CharField(max_length=200)),
                ('idea_repo', models.CharField(blank=True, max_length=80, null=True)),
                ('idea_owner', models.CharField(blank=True, max_length=30, null=True)),
                ('idea_status', models.CharField(blank=True, max_length=30, null=True)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Ideas_Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_text', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='idea',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ideas.Ideas_Group'),
        ),
    ]
