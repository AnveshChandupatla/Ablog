# Generated by Django 4.2.4 on 2023-09-27 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0006_alter_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(default='codings', max_length=255),
        ),
    ]
