# Generated by Django 5.0.6 on 2024-05-22 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.TextField()),
                ('opening', models.CharField(max_length=255)),
                ('speciality', models.CharField(max_length=255)),
                ('number_of_doctors', models.PositiveIntegerField()),
            ],
        ),
    ]
