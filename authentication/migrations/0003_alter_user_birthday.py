# Generated by Django 4.2.1 on 2023-06-08 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_user_birthday_user_phone_number_user_updated_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birthday',
            field=models.DateField(default='2023-06-07'),
        ),
    ]
