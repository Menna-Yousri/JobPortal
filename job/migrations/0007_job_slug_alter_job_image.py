# Generated by Django 4.2.15 on 2024-09-09 01:18

from django.db import migrations, models
import job.models


class Migration(migrations.Migration):
    dependencies = [
        ("job", "0006_job_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="job",
            name="slug",
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="job",
            name="image",
            field=models.ImageField(upload_to=job.models.image_upload),
        ),
    ]
