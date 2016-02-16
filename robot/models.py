from django.db import models
from django.contrib.auth.models import User


class Robot(models.Model):
    command = models.CharField(max_length=10)
    user = models.ForeignKey(User)

    def __str__(self):
        return self.command
