# Generated by Django 3.0.5 on 2020-04-18 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='covid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=200)),
                ('number', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='covid1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=200)),
                ('number', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='fullmore',
            fields=[
                ('headlines', models.CharField(max_length=500, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=2500)),
                ('hyperlink', models.URLField(max_length=2000)),
                ('source', models.CharField(max_length=2000)),
            ],
        ),
    ]
