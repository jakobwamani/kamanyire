# Generated by Django 3.2.5 on 2021-08-03 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profit_pen_app', '0003_auto_20210803_2029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rawmaterial',
            name='amount',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='rawmaterial',
            name='cost_of_supply',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='rawmaterial',
            name='pricing',
            field=models.IntegerField(default=0),
        ),
    ]