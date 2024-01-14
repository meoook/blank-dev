import random
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

from robot.core.models import Language, UserLanguage, Skill, UserSkill, SkillRequest, SkillResponse
from robot.core.static import Grade


class Command(BaseCommand):
    help = 'Manager to create test objects to test UI'

    def handle(self, *args, **options):
        name = 'alex'
        scholar = User.objects.create_user(username=name, email=f'{name}@gmail.com', password='123')
        self.stdout.write(f'Created user {name=}')
        teacher = User.objects.get(username='meok')

        active_langs = Language.objects.filter(active=True)
        for language in active_langs:
            UserLanguage.objects.create(user=scholar, language=language, level=random.choice(Grade.values))
            UserLanguage.objects.create(user=teacher, language=language, level=random.choice(Grade.values))
            self.stdout.write(f'All users knows {language}')

        for skill in Skill.objects.all():
            UserSkill.objects.create(user=teacher, skill=skill, level=random.choice(Grade.values), validated=random.choice([True,False]))
            self.stdout.write(f'Teacher now knows {skill}')
            req = SkillRequest.objects.create(scholar=scholar, skill=skill, language=random.choice(active_langs))
            SkillResponse.objects.create(teacher=teacher, request=req, price=100, time=45)

    @staticmethod
    def __random_name(length=0):
        name = ''
        length = length if isinstance(length, int) and length > 0 else 15
        letters_arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                       'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        for _ in range(length):
            letter_n = random.randrange(len(letters_arr))
            name += letters_arr[letter_n]
        return name.capitalize()
