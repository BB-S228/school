# Generated by Django 4.2.6 on 2023-12-12 14:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0008_lessondate'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='LessonDate',
            new_name='Lesson',
        ),
    ]
