# Generated by Django 3.1.7 on 2021-03-28 09:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.IntegerField(default=1, primary_key=True, serialize=False)),
                ('className', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('sRollNo', models.IntegerField(default=1, primary_key=True, serialize=False)),
                ('sName', models.CharField(max_length=255)),
                ('snumber', models.CharField(max_length=16)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('sClass', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.classes')),
            ],
        ),
    ]
