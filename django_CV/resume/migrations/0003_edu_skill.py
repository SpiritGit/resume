# Generated by Django 3.0.6 on 2020-05-26 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0002_work'),
    ]

    operations = [
        migrations.CreateModel(
            name='Edu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.CharField(max_length=100)),
                ('time', models.CharField(max_length=100)),
                ('edudetail', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(max_length=100)),
            ],
        ),
    ]
