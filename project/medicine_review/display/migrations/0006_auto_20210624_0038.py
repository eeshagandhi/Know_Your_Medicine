# Generated by Django 3.2.3 on 2021-06-23 19:08

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('display', '0005_remove_category_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(related_name='blogposts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(default='physical health', max_length=255),
        ),
    ]
