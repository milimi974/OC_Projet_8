# Generated by Django 2.0.3 on 2018-04-08 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20180409_0154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='nutri_code',
            field=models.CharField(blank=True, max_length=1),
        ),
    ]
