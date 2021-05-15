# Generated by Django 3.1.10 on 2021-05-15 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rules',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('priority', models.PositiveSmallIntegerField(unique=True)),
                ('rule', models.CharField(max_length=1000)),
            ],
            options={
                'verbose_name': 'Rule',
                'verbose_name_plural': 'Rules',
            },
        ),
    ]