# Generated by Django 2.0.7 on 2018-07-17 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_authors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='notes',
            field=models.TextField(default='null'),
            preserve_default=False,
        ),
    ]