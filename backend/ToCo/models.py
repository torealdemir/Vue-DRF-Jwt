from django.db import models
from django.contrib.auth.models import User


class MainContent(models.Model):
    title = models.CharField(max_length=155)
    content = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title


    @property
    def created_by_username(self):
        return self.created_by.username