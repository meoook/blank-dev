from django.urls import path, include
from rest_framework import routers
from robot.core import views

router = routers.DefaultRouter()
router.register(r'languages', views.LanguageViewSet)
router.register(r'skills', views.SkillTableViewSet)
router.register(r'requests', views.SkillRequestViewSet)

router.register(r'users', views.UserViewSet)

# API urls
urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework'))
]
