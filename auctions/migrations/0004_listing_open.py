# Generated by Django 4.1.2 on 2022-11-10 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_bid_user_alter_listing_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='open',
            field=models.BooleanField(default=True),
        ),
    ]