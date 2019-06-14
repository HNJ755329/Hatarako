# Generated by Django 2.0.4 on 2019-06-14 00:22

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('web', models.CharField(max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('contents', models.TextField(null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('industory', models.CharField(max_length=30)),
                ('career', models.CharField(max_length=30)),
                ('age', models.CharField(max_length=20)),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='hataraku.Color')),
            ],
        ),
    ]