from django.contrib import admin
from any_skill.core import models


@admin.register(models.Language)
class LanguageAdmin(admin.ModelAdmin):
    pass


@admin.register(models.UserSkill)
class UserSkillAdmin(admin.ModelAdmin):
    pass


@admin.register(models.UserLanguage)
class UserLanguageAdmin(admin.ModelAdmin):
    pass


@admin.register(models.SkillRequest)
class SkillRequestAdmin(admin.ModelAdmin):
    pass


@admin.register(models.SkillResponse)
class SkillResponseAdmin(admin.ModelAdmin):
    pass

