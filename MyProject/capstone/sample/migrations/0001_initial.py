# Generated by Django 3.2.5 on 2022-02-21 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('idnum', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('course', models.CharField(max_length=100)),
                ('year', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'student',
            },
        ),
    ]
