from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    create_date = models.DateField()

    def __str__(self):
        return self.title

