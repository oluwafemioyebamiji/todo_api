# Generated by Django 5.1.1 on 2024-10-06 14:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("todo", "0005_todo_slug_alter_todo_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="todo",
            name="slug",
            field=models.CharField(max_length=200, null=True, unique=True),
        ),
    ]
