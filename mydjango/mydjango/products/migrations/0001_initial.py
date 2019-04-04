# Generated by Django 2.0.7 on 2019-01-17 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('description', models.TextField()),
                ('price', models.TextField()),
                ('summary', models.TextField(default='this is cool!!')),
            ],
        ),
    ]
