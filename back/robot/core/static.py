from django.db import models


class LessonTime(models.IntegerChoices):
    """ Time in minutes for lesson """
    SHORT = 30
    NORMAL = 45
    HOUR = 60
    ACADEMIC = 90
    BIG = 120


class Grade(models.IntegerChoices):
    OMG = 1  # Money back
    BAD = 2
    NORMAL = 3
    GOOD = 4
    BEST = 5
