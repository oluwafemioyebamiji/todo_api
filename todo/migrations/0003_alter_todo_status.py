# Generated by Django 5.1.1 on 2024-09-29 13:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("todo", "0002_todo_percentage_completion"),
    ]

    operations = [
        migrations.AlterField(
            model_name="todo",
            name="status",
            field=models.CharField(default="new", max_length=200),
        ),
    ]
