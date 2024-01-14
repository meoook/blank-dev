# Generated by Django 4.0.5 on 2022-07-02 22:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False,
                                           verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('api_key', models.CharField(max_length=64)),
                ('balance', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Coin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False,
                                           verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('short_name', models.CharField(max_length=4, unique=True)),
                ('ticker', models.CharField(max_length=10, unique=True)),
                ('active', models.BooleanField(default=False)),
                ('in_futures', models.BooleanField(default=False)),
                ('delimiter', models.PositiveIntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Tactic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False,
                                           verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('free', models.BooleanField(default=False)),
                ('avg_time', models.PositiveSmallIntegerField(
                    choices=[(30, 'Short'), (45, 'Normal'), (60, 'Hour'), (90, 'Academic'), (120, 'Big')],
                    null=True)),
            ],
        ),
    ]
