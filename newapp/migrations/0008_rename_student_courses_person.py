# Generated by Django 4.1 on 2022-09-01 07:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0007_rename_students_courses_student'),
    ]

    operations = [
        migrations.RenameField(
            model_name='courses',
            old_name='student',
            new_name='person',
        ),
    ]