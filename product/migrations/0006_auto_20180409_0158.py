# Generated by Django 2.0.3 on 2018-04-08 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20180409_0157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='nutri_code',
            field=models.CharField(blank=True, default='', max_length=1),
        ),
    ]
