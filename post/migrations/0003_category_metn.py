# Generated by Django 2.2.5 on 2020-01-08 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='metn',
            field=models.TextField(default=10),
            preserve_default=False,
        ),
    ]