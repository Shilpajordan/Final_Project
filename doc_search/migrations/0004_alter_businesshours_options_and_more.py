# Generated by Django 4.2.11 on 2024-04-30 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("doc_search", "0003_businesshours")]

    operations = [
        migrations.AlterModelOptions(
            name="businesshours",
            options={
                "ordering": ["id"],
                "verbose_name": "Business Hour",
                "verbose_name_plural": "Business Hours",
            },
        ),
        migrations.RemoveField(model_name="appointment", name="patient"),
        migrations.RemoveField(model_name="appointment", name="time"),
        migrations.AddField(
            model_name="appointment",
            name="patient_id",
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
