from django.db import models
from django.contrib.auth.models import User
from robot.core.static import LessonTime, Grade


class Language(models.Model):
    name = models.CharField(max_length=50, unique=True)
    short_name = models.CharField(max_length=10)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.short_name


class UserLanguage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='languages')
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    level = models.PositiveSmallIntegerField(choices=Grade.choices)

    def __str__(self):
        return f'{self.user} {self.language}:{self.level}'

    class Meta:
        unique_together = ('user', 'language',)


class SkillGroup(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class SkillSubGroup(models.Model):  # TODO: rename to - Tags ?
    group = models.ForeignKey(SkillGroup, on_delete=models.PROTECT, related_name='subs')
    name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.group}:{self.name}'

    class Meta:
        unique_together = ('group', 'name',)


class Skill(models.Model):
    sub_group = models.ForeignKey(SkillSubGroup, on_delete=models.PROTECT, related_name='skills')
    name = models.CharField(max_length=200)
    avg_price = models.PositiveIntegerField(default=0)
    avg_time = models.PositiveSmallIntegerField(choices=LessonTime.choices, null=True)

    def __str__(self):
        return f'{self.sub_group}:{self.name}'

    class Meta:
        unique_together = ('sub_group', 'name',)


class UserSkill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='skills')
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    level = models.PositiveSmallIntegerField(choices=Grade.choices)
    validated = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user} {self.level}:{self.skill}'

    class Meta:
        unique_together = ('user', 'skill',)


class SkillRequest(models.Model):
    scholar = models.ForeignKey(User, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.scholar} {self.language}:{self.skill}'


class SkillResponse(models.Model):
    request = models.ForeignKey(SkillRequest, on_delete=models.CASCADE)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    time = models.PositiveSmallIntegerField(choices=LessonTime.choices)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.teacher} {self.time}:{self.price} on {self.request}'

    class Meta:
        unique_together = ('request', 'teacher',)


class Lesson(models.Model):
    response = models.OneToOneField(SkillResponse, on_delete=models.CASCADE)
    dt_planed = models.DateTimeField(blank=True, null=True)
    dt_start = models.DateTimeField(blank=True, null=True)
    dt_end = models.DateTimeField(blank=True, null=True)
    level = models.PositiveSmallIntegerField(null=True, choices=Grade.choices)
    comment = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.response} - result {self.level}'
