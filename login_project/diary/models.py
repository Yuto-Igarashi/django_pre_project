from myapp.models import CustomUser
from django.db import models


class Diary(models.Model):
    user = models.ForeignKey(CustomUser,verbose_name='ユーザー', on_delete=models.PROTECT)
    title = models.CharField(max_length=50)
    content = models.TextField()
    create_date = models.DateField()

    class Meta:
        verbose_name_plural = "Difffary"

    def __str__(self):
        return self.title
