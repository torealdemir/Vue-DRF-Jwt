from django.db import models

class MainContent(models.Model):
    title = models.CharField(max_length=155)
    content = models.TextField()

    def __str__(self):
        return self.title
