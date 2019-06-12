from django.db import models
import uuid

# Create your models here.

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    contents = models.TextField(null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    industory = models.CharField(max_length=30)
    career = models.CharField(max_length=30)
    age = models.CharField(max_length=20)