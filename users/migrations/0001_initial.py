# Generated by Django 3.1.2 on 2020-12-09 12:24

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('union', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_photo', cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='profile_photo')),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('location', models.CharField(blank=True, max_length=60)),
                ('contact', models.CharField(blank=True, max_length=60)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('studentunion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='union.studentunion')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
