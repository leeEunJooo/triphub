# Generated by Django 2.1.8 on 2019-07-20 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RoomInput',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='date published')),
                ('roomname', models.CharField(max_length=10)),
                ('mainmember', models.CharField(max_length=10)),
            ],
        ),
    ]
