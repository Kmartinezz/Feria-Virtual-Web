# Generated by Django 2.1.15 on 2022-12-13 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Feria_App', '0017_auto_20221209_1921'),
    ]

    operations = [
        migrations.AddField(
            model_name='transporte',
            name='capacidad',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
    ]
