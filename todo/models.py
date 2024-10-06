from django.db import models
from  django.utils import timezone
# Create your models here.
from  django.utils.text import slugify

# def createslug(title):
#     return title.replace(" ", "-")

def createslug(title):
    return slugify(title)

class Todo(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    completed_at = models.DateTimeField(null=True)
    STATUS_CHOICES = [
        ("new","new"),
        ("done","done"),
        ("in-progress","in-progress"),
    ]
    status = models.CharField(max_length = 200, choices = STATUS_CHOICES, default = "new")
    slug = models.CharField(max_length = 200, null=True, unique=True)
    is_archived = models.BooleanField(default = False)
    archived_at = models.DateTimeField(null=True)
    percentage_completion = models.IntegerField(default = 0)

    def save(self, *args, **kwargs):
        # Add some logic here
        if not self.completed_at and self.status == 'done':
            self.completed_at = timezone.now()
        if self.archived_at is None and self.is_archived:
            self.archived_at = timezone.now()
        self.slug = self.createsluginternal()
        # self.slug = self.title.replace(" ", "-")
        super(Todo, self).save(*args, **kwargs)

    def createsluginternal(self):
        return slugify(self.title)

    def __str__(self):
        return f"{self.title} - {self.status}"