# Generated by Django 3.1.7 on 2021-03-27 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0005_auto_20210327_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoapp',
            name='title',
            field=models.CharField(max_length=250),
        ),
    ]
