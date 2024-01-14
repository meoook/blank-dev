from django.contrib import admin
from robot.core import models


@admin.register(models.Bot)
class LanguageAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Tactic)
class UserSkillAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Coin)
class UserLanguageAdmin(admin.ModelAdmin):
    pass
