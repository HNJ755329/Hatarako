# Generated by Django 2.0.4 on 2019-06-14 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hataraku', '0003_auto_20190614_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='color',
            field=models.CharField(max_length=7),
        ),
    ]
