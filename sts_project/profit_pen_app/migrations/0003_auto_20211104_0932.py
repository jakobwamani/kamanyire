# Generated by Django 3.2.7 on 2021-11-04 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profit_pen_app', '0002_auto_20211017_1946'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='fish',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='general_purpose_premix',
            field=models.IntegerField(default=0),
        ),
    ]
