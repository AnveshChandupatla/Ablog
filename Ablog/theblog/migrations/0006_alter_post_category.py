# Generated by Django 4.2.4 on 2023-09-27 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0005_category_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(default='--Select Category--', max_length=255),
        ),
    ]
