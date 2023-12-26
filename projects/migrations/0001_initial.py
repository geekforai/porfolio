# Generated by Django 4.2.7 on 2023-11-30 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_title', models.CharField(max_length=50)),
                ('project_image', models.ImageField(max_length=50, upload_to='')),
                ('project_desc', models.TextField()),
                ('project_tech_used', models.TextField()),
                ('project_link', models.CharField(max_length=50)),
            ],
        ),
    ]