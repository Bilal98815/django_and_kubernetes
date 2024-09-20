# Generated by Django 5.1 on 2024-09-16 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practice_app', '0003_practicemodel_last_modified'),
    ]

    operations = [
        migrations.CreateModel(
            name='StaticFilesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                                           primary_key=True,
                                           serialize=False,
                                           verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('file', models.FileField(upload_to='files/')),
            ],
        ),
    ]
