# Generated by Django 5.0 on 2023-12-12 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0008_lesson'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='date',
            field=models.DateField(default='NULL'),
        ),
    ]