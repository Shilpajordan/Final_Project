# Generated by Django 5.0.4 on 2024-04-28 17:08

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("doc_search", "0004_alter_patient_complaint_alter_patient_insurance"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="appointment",
            name="time",
        ),
    ]
