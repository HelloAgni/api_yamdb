# Generated by Django 2.2.16 on 2022-03-22 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0011_auto_20220322_1542'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='title',
            name='rating',
        ),
    ]