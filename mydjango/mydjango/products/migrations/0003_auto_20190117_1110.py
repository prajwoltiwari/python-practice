# Generated by Django 2.0.7 on 2019-01-17 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20190117_0548'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='verified',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]