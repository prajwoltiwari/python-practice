# Generated by Django 2.0.7 on 2019-01-17 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20190117_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='summary',
            field=models.TextField(blank=True),
        ),
    ]
