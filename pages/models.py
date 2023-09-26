from django.db import models


class Team(models.Model):

    first_name = models.CharField(max_length=225)
    last_name = models.CharField(max_length=225)
    designation = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name




