# Generated by Django 5.0.4 on 2024-04-30 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doc_search', '0004_alter_businesshours_options_alter_doctor_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='consultation_hours',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='location',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
