# Generated by Django 4.2 on 2023-04-24 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_directmessage_options_directmessage_is_reply_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='directmessage',
            name='is_reply',
        ),
        migrations.RemoveField(
            model_name='directmessage',
            name='reply',
        ),
        migrations.AlterField(
            model_name='profile',
            name='img',
            field=models.ImageField(upload_to='profile_img/%Y/%m/%d'),
        ),
    ]
