# Generated by Django 4.1.2 on 2022-10-26 20:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Feria_App', '0003_productor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fotografia', models.CharField(max_length=200)),
                ('precio', models.IntegerField()),
                ('cantidad', models.IntegerField(max_length=10)),
                ('estado', models.CharField(choices=[('disponible', 'Disponible'), ('ocupada', 'Ocupada')], max_length=10)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
