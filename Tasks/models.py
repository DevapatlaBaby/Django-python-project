from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
   objects = None
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   title = models.CharField(max_length=200)
   description = models.TextField()
   category = models.CharField(max_length=1000)
   due_date = models.DateField(blank=True, null=True)
   priority = models.IntegerField()
   completed = models.BooleanField(default=False)
   created_at = models.DateTimeField(auto_now_add=True)

   def __str__(self):
     return self.title