# Generated by Django 3.1 on 2020-08-22 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blogger_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogger',
            name='photo',
            field=models.ImageField(blank=True, default='unnamed.png', null=True, upload_to=''),
        ),
    ]