# Generated by Django 4.1.4 on 2023-01-09 17:34

from django.db import migrations, models
import main_page.models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0049_alter_about_photo_alter_about_video_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='photo',
            field=models.ImageField(upload_to=main_page.models.NewFileName.get_file_name),
        ),
        migrations.AlterField(
            model_name='about',
            name='video',
            field=models.FileField(upload_to=main_page.models.NewFileName.get_file_name),
        ),
        migrations.AlterField(
            model_name='chefs',
            name='photo',
            field=models.ImageField(upload_to=main_page.models.NewFileName.get_file_name),
        ),
        migrations.AlterField(
            model_name='dish',
            name='photo',
            field=models.ImageField(upload_to=main_page.models.NewFileName.get_file_name),
        ),
        migrations.AlterField(
            model_name='events',
            name='photo',
            field=models.ImageField(upload_to=main_page.models.NewFileName.get_file_name),
        ),
        migrations.AlterField(
            model_name='restaurantphoto',
            name='photo',
            field=models.ImageField(upload_to=main_page.models.NewFileName.get_file_name),
        ),
        migrations.AlterField(
            model_name='review',
            name='photo',
            field=models.ImageField(blank=True, upload_to=main_page.models.NewFileName.get_file_name),
        ),
        migrations.AlterField(
            model_name='startpage',
            name='photo',
            field=models.FileField(upload_to=main_page.models.NewFileName.get_file_name),
        ),
    ]
