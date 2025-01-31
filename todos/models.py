# models.py
from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError

# Model Manager
class TodoManager(models.Manager):
    def active(self):
        return self.filter(is_completed=False)
    
    def completed(self):
        return self.filter(is_completed=True)
    
    def priority(self, level):
        return self.filter(priority=level)

# Abstract Base Class
class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)  # Changed back
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
# Main Todo Model with enhanced fields
class Todo(TimeStampedModel):
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High')
    ]

    content = models.TextField()
    is_completed = models.BooleanField(default=False)
    priority = models.CharField(
        max_length=10, 
        choices=PRIORITY_CHOICES, 
        default='medium'
    )
    due_date = models.DateTimeField(null=True, blank=True)
    notes = models.TextField(blank=True)

    # Model Manager
    objects = TodoManager()

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.content[:50]}..."

    # Model Method
    def mark_as_completed(self):
        self.is_completed = True
        self.save()

    # Property
    @property
    def is_overdue(self):
        if self.due_date and not self.is_completed:
            return timezone.now() > self.due_date
        return False

    # Custom Validation
    def clean(self):
        if self.due_date and self.due_date < timezone.now():
            raise ValidationError("Due date cannot be in the past")

# Category Model (for relationship example)
class Category(models.Model):
    name = models.CharField(max_length=100)
    todos = models.ManyToManyField(Todo, related_name='categories')

    def __str__(self):
        return self.name