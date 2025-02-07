# Generated by Django 5.1.3 on 2024-12-15 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PlaceName', models.CharField(max_length=255)),
                ('Weather', models.CharField(max_length=255)),
                ('State', models.CharField(max_length=255)),
                ('District', models.CharField(max_length=255)),
                ('GoogleMap', models.URLField(max_length=255)),
                ('Description', models.CharField(max_length=255)),
                ('Images', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
