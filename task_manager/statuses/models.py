from django.db import models


class Status(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
