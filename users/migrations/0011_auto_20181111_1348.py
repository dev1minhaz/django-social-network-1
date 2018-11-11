# Generated by Django 2.1.2 on 2018-11-11 13:48

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_siteuser_friends'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteuser',
            name='friends',
            field=models.ManyToManyField(blank=True, related_name='user_friends', to=settings.AUTH_USER_MODEL),
        ),
    ]
