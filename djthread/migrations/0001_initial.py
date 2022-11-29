# Generated by Django 4.0.4 on 2022-11-29 11:03

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
                ('student_name', models.CharField(max_length=100)),
                ('student_email', models.EmailField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
            ],
        ),
    ]
