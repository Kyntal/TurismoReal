# Generated by Django 3.0.10 on 2020-10-18 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0003_auto_20201016_2336'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='contrasena',
            field=models.CharField(max_length=30, null=True),
        ),
    ]