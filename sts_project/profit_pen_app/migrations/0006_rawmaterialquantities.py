# Generated by Django 3.2.7 on 2021-09-15 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profit_pen_app', '0005_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='RawMaterialQuantities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('maize_bran', models.IntegerField(default=0)),
                ('cotton', models.IntegerField(default=0)),
                ('sun_flower', models.IntegerField(default=0)),
                ('fish', models.IntegerField(default=0)),
                ('salt', models.IntegerField(default=0)),
                ('general_purpose_premix', models.IntegerField(default=0)),
                ('layers_premix', models.IntegerField(default=0)),
                ('shells', models.IntegerField(default=0)),
                ('meat_boaster', models.IntegerField(default=0)),
                ('egg_boaster', models.IntegerField(default=0)),
            ],
        ),
    ]
