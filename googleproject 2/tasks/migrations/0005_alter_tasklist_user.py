# Generated by Django 4.0.5 on 2022-07-10 21:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0004_rename_title_task_name_remove_task_user_tasklist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasklist',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tasklist', to=settings.AUTH_USER_MODEL),
        ),
    ]
