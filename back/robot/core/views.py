import logging

from rest_framework import viewsets, permissions
from django.contrib.auth.models import User
from robot.core import serializers, models
from robot.core.api.utils import DefaultSetPagination

logger = logging.getLogger(__name__)


class LanguageViewSet(viewsets.ModelViewSet):
    """ Display all languages on login """
    serializer_class = serializers.LanguageSerializer
    http_method_names = ['get']
    queryset = models.Language.objects.filter(active=True)


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserSerializer
    http_method_names = ['get']
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all().order_by('-date_joined')


class SkillTableViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.SkillTableSerializer
    http_method_names = ['get']
    permission_classes = [permissions.IsAuthenticated]
    queryset = models.SkillGroup.objects.all()


class SkillRequestViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.SkillRequestSerializer
    http_method_names = ['get', 'post', 'put', 'delete']
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = DefaultSetPagination
    queryset = models.SkillRequest.objects.filter(active=True).order_by('-created')

    def list(self, request, *args, **kwargs):
        """ Display SkillRequest user have skill """
        _user_skills = self.request.user.skills.filter(validated=True).values_list('skill', flat=True)
        _user_languages = self.request.user.languages.values_list('language', flat=True)
        _qs = self.get_queryset().filter(skill__in=_user_skills)
        _qs = _qs.filter(language__in=_user_languages).order_by('skill', 'language')
        _page = self.paginate_queryset(_qs)
        _serializer = self.get_serializer(_page, many=True)
        return self.get_paginated_response(data=_serializer.data)

    def perform_create(self, serializer):
        _user = self.request.user
        skill: str = self.request.data.get("skill")  # For log only
        language: str = self.request.data.get("language")  # For log only
        logger.info(f'User {_user.first_name}:{_user.id} creating skill request {language=} {skill=}')
        serializer.save(scholar=_user)


class SkillResponseViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.SkillResponseSerializer
    http_method_names = ['get', 'post', 'put', 'delete']
    permission_classes = [permissions.IsAuthenticated]
    queryset = models.SkillResponse.objects.all()


class LessonViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.LessonSerializer
    http_method_names = ['get', 'post', 'put']
    permission_classes = [permissions.IsAuthenticated]
    queryset = models.Lesson.objects.all()
