# Generated by Django 5.0.7 on 2024-09-14 20:54

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("grade", "0002_day_grade_student_grade"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name="day_grade",
            name="student_grade",
        ),
        migrations.AddField(
            model_name="day_grade",
            name="student",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="day_grades",
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
    ]
