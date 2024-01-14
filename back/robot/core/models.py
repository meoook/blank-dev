from django.db import models
from django.contrib.auth.models import User
from robot.core.static import LessonTime


class Coin(models.Model):
    name = models.CharField(max_length=50, unique=True)
    short_name = models.CharField(max_length=4, unique=True)
    ticker = models.CharField(max_length=10, unique=True)
    active = models.BooleanField(default=False)
    in_futures = models.BooleanField(default=False)
    delimiter = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.short_name


class Tactic(models.Model):
    name = models.CharField(max_length=50, unique=True)
    free = models.BooleanField(default=False)
    # Tactic settings
    avg_time = models.PositiveSmallIntegerField(choices=LessonTime.choices, null=True)

    def __str__(self):
        return self.name


class Bot(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    coin = models.ForeignKey(Coin, on_delete=models.PROTECT)
    tactic = models.ForeignKey(Tactic, on_delete=models.PROTECT)
    name = models.CharField(max_length=50)
    api_key = models.CharField(max_length=64)
    balance = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.tactic}:{self.name} {self.balance} {self.coin}'

    class Meta:
        unique_together = ('owner', 'name',)
