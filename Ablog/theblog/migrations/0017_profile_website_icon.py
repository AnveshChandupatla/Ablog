# Generated by Django 4.2.4 on 2023-10-03 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0016_profile_instagram_icon_profile_twitter_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='website_icon',
            field=models.ImageField(blank=True, null=True, upload_to='images/social/'),
        ),
    ]
