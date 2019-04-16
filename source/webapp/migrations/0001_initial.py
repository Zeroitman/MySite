# Generated by Django 2.2 on 2019-04-15 16:38

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
            name='Program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, max_length=2000, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('edited_date', models.DateTimeField(auto_now=True)),
                ('deleted_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_skill', models.CharField(default='Введите код навыка!', max_length=5, verbose_name='Код навыка')),
                ('name', models.CharField(max_length=255, verbose_name='Название навыка')),
                ('description', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Описание навыка')),
                ('date_create', models.DateTimeField(auto_now_add=True, verbose_name='Время создания навыка')),
                ('date_update', models.DateTimeField(blank=True, null=True, verbose_name='Время редактирование навыка')),
                ('date_delete', models.DateTimeField(blank=True, null=True, verbose_name='Время удаления навыка')),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=50, verbose_name='Телефон')),
                ('delete_date', models.DateTimeField()),
                ('edit_date', models.DateTimeField(auto_now=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='client', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
    ]
