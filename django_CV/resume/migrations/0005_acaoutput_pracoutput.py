# Generated by Django 3.0.6 on 2020-05-26 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0004_eedu_eprofile_eskill_ework'),
    ]

    operations = [
        migrations.CreateModel(
            name='AcaOutput',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('author', models.CharField(max_length=100)),
                ('journal', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PracOutput',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workoutput', models.CharField(max_length=100)),
            ],
        ),
    ]
