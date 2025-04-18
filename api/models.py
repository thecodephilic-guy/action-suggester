from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import JSONField  

class QueryLog(models.Model):
    query = models.TextField()
    tone = models.CharField(max_length=100)
    intent = models.CharField(max_length=100)
    suggested_actions = models.JSONField()  # Use TextField if needed
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.query} ({self.tone}, {self.intent})"
    
#Note: Django automatically gives name to the tables using the app name and model name for example: api_querylog (this will be the name of the table in the database)