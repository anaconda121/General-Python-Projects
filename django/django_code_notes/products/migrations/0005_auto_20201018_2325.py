# Generated by Django 3.1.2 on 2020-10-19 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20201018_2324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='summary',
            field=models.TextField(default='plz work come on dog'),
        ),
    ]