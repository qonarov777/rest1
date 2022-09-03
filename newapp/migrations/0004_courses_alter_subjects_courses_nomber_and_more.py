# Generated by Django 4.1 on 2022-09-01 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0003_subjects'),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.IntegerField(max_length=50)),
                ('students', models.TextField(max_length=30)),
                ('title', models.TextField(max_length=100)),
                ('image', models.ImageField(upload_to='media/Courses/')),
                ('mark', models.IntegerField(max_length=50)),
                ('price', models.IntegerField(max_length=50)),
            ],
            options={
                'verbose_name': 'Mavzu',
                'verbose_name_plural': 'Mavzular',
            },
        ),
        migrations.AlterField(
            model_name='subjects',
            name='courses_nomber',
            field=models.IntegerField(max_length=50),
        ),
        migrations.AlterField(
            model_name='subjects',
            name='image',
            field=models.ImageField(upload_to='media/subjects/'),
        ),
    ]
