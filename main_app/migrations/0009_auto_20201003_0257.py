# Generated by Django 3.1.1 on 2020-10-03 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_auto_20201002_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='location',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]