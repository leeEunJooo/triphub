# Generated by Django 2.1.8 on 2019-07-20 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TripHubApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='myRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_id', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=10)),
            ],
        ),
    ]
