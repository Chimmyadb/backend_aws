# Generated by Django 5.1.4 on 2025-01-17 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_rename_classroom_classlevel_delete_grade'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='role',
            field=models.CharField(default='teacher', max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('admin', 'admin'), ('teacher', 'teacher')], max_length=20),
        ),
    ]
