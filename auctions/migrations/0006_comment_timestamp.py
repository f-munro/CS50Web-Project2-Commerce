# Generated by Django 4.1.2 on 2022-11-22 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auctions", "0005_comment_content"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="timestamp",
            field=models.DateTimeField(auto_now=True),
        ),
    ]