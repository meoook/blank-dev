from rest_framework import serializers
from django.contrib.auth.models import User

from any_skill.core import models


class LanguageSerializer(serializers.ModelSerializer):
    """ Language choice """

    class Meta:
        model = models.Language
        fields = ('id', 'name', 'short_name',)


class SkillSerializer(serializers.ModelSerializer):
    """ Skill choice """

    class Meta:
        model = models.Skill
        fields = ('id', 'name',)  # 'avg_price', 'avg_time',)


class SkillSubGroupSerializer(serializers.ModelSerializer):
    """ Sub skill group choice """
    skills = SkillSerializer(many=True, read_only=True)

    class Meta:
        model = models.SkillSubGroup
        fields = ('id', 'name', 'skills',)


class SkillTableSerializer(serializers.ModelSerializer):
    """ Primary skill group """
    groups = SkillSubGroupSerializer(many=True, read_only=True, source='subs')

    class Meta:
        model = models.SkillGroup
        fields = ('id', 'name', 'groups',)


class UserLanguageSerializer(serializers.ModelSerializer):
    """ User language skill """
    # language = LanguageSerializer(many=False, read_only=True)

    class Meta:
        model = models.UserLanguage
        fields = ('language', 'level',)


class UserSkillSerializer(serializers.ModelSerializer):
    """ User skill """
    # skill = SkillSerializer(many=False, read_only=True)

    class Meta:
        model = models.UserSkill
        fields = ['skill', 'level', 'validated']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    languages = UserLanguageSerializer(many=True, read_only=True)
    skills = UserSkillSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'languages', 'skills',)


class SkillRequestSerializer(serializers.ModelSerializer):
    # scholar = UserSerializer(many=False, read_only=True)
    # skill = SkillSerializer(many=False, read_only=True)
    # language = LanguageSerializer(many=False, read_only=True)

    class Meta:
        model = models.SkillRequest
        fields = ('scholar', 'skill', 'language', 'description', 'created',)


class SkillResponseSerializer(serializers.ModelSerializer):
    request = SkillRequestSerializer(many=False, read_only=True)
    teacher = UserSerializer(many=False, read_only=True)

    class Meta:
        model = models.SkillResponse
        fields = ('request', 'teacher', 'price', 'time', 'created',)


class LessonSerializer(serializers.ModelSerializer):
    response = SkillResponseSerializer(many=False, read_only=True)

    class Meta:
        model = models.Lesson
        fields = ('response', 'dt_planed', 'dt_start', 'dt_end', 'level', 'comment', 'created',)
