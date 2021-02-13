from django.db import models


class Article(models.Model):
    """Create Article table with columns in database"""

    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title
