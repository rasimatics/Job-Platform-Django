# Generated by Django 2.2.5 on 2020-02-05 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0010_post_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='price',
            field=models.IntegerField(),
        ),
    ]
