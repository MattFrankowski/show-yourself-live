# Generated by Django 3.1 on 2020-08-27 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_blogger_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogger',
            name='photo',
            field=models.ImageField(blank=True, default='unnamed.png', null=True, upload_to='media'),
        ),
    ]
