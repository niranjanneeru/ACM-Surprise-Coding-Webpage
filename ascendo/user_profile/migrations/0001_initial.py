# Generated by Django 3.1.10 on 2021-05-15 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('nick_name', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=15)),
                ('college', models.CharField(max_length=100)),
                ('language', models.BooleanField(default=False)),
                ('code', models.BooleanField(default=False)),
                ('has_completed', models.BooleanField(default=False)),
                ('last_submission', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Profile',
                'ordering': ('-has_completed', 'last_submission', '-code', '-has_completed'),
            },
        ),
    ]
