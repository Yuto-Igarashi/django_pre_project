from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

#AbstractUserを継承CoustomUserクラスを作成
class CustomUser(AbstractUser):
    age = models.IntegerField(null=True)