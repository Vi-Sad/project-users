# Generated by Django 4.2.1 on 2024-04-22 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0020_user_date_registration'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]
