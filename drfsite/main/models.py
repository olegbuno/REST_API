from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='persons')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
