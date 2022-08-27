# Release notes

| Version |    Date    | Changes                     |
|:-------:|:----------:|:----------------------------|
|  0.0.1  | 02.07.2022 | Start                       |


```python
from django.conf.global_settings import LANGUAGES


def get_languages(apps, schema_editor):
    languages = apps.get_model('core', 'Language')
    for language in LANGUAGES:
        language_to_add = languages(name=language[1], short_name=language[0])
        if language[0] in ('en', 'ru', 'de', 'es'):
            language_to_add.active = True
        language_to_add.save()

```