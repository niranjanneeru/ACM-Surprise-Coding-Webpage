# Generated by Django 3.1.10 on 2021-05-15 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_auto_20210515_1036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='response',
            name='answer',
            field=models.CharField(max_length=500),
        ),
    ]
