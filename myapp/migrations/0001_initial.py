# Generated by Django 2.2.5 on 2019-09-27 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'employee',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=50)),
                ('age', models.CharField(max_length=3)),
            ],
            options={
                'db_table': 'student',
            },
        ),
    ]
