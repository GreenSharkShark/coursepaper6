# Generated by Django 4.2.3 on 2023-07-28 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailsender', '0005_remove_mailing_mailing_time_mailing_mailing_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailing',
            name='mailing_datetime',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Время и дата рассылки'),
        ),
    ]
