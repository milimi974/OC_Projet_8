# Generated by Django 2.0.3 on 2018-04-08 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_auto_20180409_0158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='nutri_code',
            field=models.CharField(max_length=1, null=True),
        ),
    ]
