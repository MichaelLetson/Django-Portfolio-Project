# Generated by Django 3.2.14 on 2022-08-07 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PT_APP', '0004_alter_post_featured_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='featured_image',
            field=models.ImageField(blank=True, default='placeholder', upload_to='images/'),
        ),
    ]