# Generated by Django 4.1.2 on 2022-10-12 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Feria_App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='email',
            field=models.EmailField(max_length=30),
        ),
    ]
