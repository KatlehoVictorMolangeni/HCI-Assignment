from django.db import models

# Create your models here.
class student_details(models.Model):
    name = models.TextField(max_length=150)
    surname = models.TextField(max_length=150)
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # We'll hash it later
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username