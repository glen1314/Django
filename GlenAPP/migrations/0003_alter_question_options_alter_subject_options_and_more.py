# Generated by Django 5.0.4 on 2024-04-12 15:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GlenAPP', '0002_subject_teacher_question_choice'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'managed': False, 'verbose_name': '问题', 'verbose_name_plural': '问题'},
        ),
        migrations.AlterModelOptions(
            name='subject',
            options={'managed': False, 'verbose_name': '科目', 'verbose_name_plural': '科目'},
        ),
        migrations.AlterModelOptions(
            name='teacher',
            options={'managed': False, 'verbose_name': '老师', 'verbose_name_plural': '老师'},
        ),
    ]