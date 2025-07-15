from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
import uuid

# Create your models here.
class Movie(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    title = models.CharField(max_length=200)
    date = models.DateTimeField(default=datetime.now)
    recommended_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title