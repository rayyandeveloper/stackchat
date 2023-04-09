# Generated by Django 4.1.7 on 2023-04-08 08:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='u1', to=settings.AUTH_USER_MODEL)),
                ('u2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='u2', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
