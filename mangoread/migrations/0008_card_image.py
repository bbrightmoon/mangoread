# Generated by Django 4.2 on 2023-04-17 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mangoread', '0007_card_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='image',
            field=models.URLField(blank=True, null=True),
        ),
    ]
