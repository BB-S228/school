# Generated by Django 5.0 on 2023-12-06 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0006_alter_journal_grade_alter_journal_lesson_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journal',
            name='grade',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
