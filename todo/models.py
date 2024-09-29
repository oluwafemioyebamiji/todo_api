from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    completed_at = models.DateField(null=True)
    status = models.CharField(max_length = 200, default = "new")
    is_archived = models.BooleanField(default = False)
    percentage_completion = models.IntegerField(default = 0)

    def __str__(self):
        return f"{self.title} - {self.status}"