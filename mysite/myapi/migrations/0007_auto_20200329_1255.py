# Generated by Django 3.0.4 on 2020-03-29 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0006_auto_20200329_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='key',
            field=models.CharField(max_length=8, unique=True),
        ),
    ]
