# Generated by Django 4.2.7 on 2023-12-01 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experience', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='image',
            field=models.ImageField(default=1, max_length=50, upload_to=''),
            preserve_default=False,
        ),
    ]
