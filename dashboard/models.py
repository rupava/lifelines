from django.db import models
from django.contrib.auth.models import User

class Entry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    entry_title = models.CharField(max_length=100)
    entry_content = models.TextField()

    class Meta:
        unique_together = [['user', 'date']]

    def __str__(self):
        return self.entry_title