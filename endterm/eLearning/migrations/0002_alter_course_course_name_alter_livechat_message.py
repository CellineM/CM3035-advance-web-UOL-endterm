# Generated by Django 4.2.11 on 2024-09-06 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eLearning', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='livechat',
            name='message',
            field=models.TextField(blank=True, null=True),
        ),
    ]
