# Generated by Django 5.0.4 on 2024-04-27 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sport', '0005_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='coach',
            field=models.CharField(max_length=100),
        ),
    ]