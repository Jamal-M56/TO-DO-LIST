from django.db import models
from django.conf import settings
# Create your models here.
class Task(models.Model):

    STATUS_CHOICES = [
        ('pending','Pending'),
        ('in_progress','In Progress'),
        ('completed','Completed'),
        ('delayed','Delayed'),
    ]

    title = models.CharField(max_length=100)
    discription = models.TextField(null=True,blank=True)
    status = models.CharField(choices= STATUS_CHOICES,max_length=100)
    deadline = models.DateTimeField(null=True,blank=True,)
    created_at = models.DateTimeField(auto_now=True)    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='tasks',

    )

    def __str__(self):
        return str(self.title)