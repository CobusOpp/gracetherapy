# Generated by Django 3.2.8 on 2021-11-19 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_contactlist_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactlist',
            old_name='title',
            new_name='Bussiness_name',
        ),
        migrations.RemoveField(
            model_name='contactlist',
            name='biz_name',
        ),
    ]