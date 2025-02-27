# Generated by Django 5.0.1 on 2024-05-08 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manytomany_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='students_related',
            field=models.ManyToManyField(blank=True, null=True, related_name='courses_related', to='manytomany_app.student'),
        ),
        migrations.AlterField(
            model_name='student',
            name='courses',
            field=models.ManyToManyField(blank=True, null=True, related_name='students', to='manytomany_app.course'),
        ),
    ]
