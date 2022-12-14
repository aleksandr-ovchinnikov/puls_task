# Generated by Django 4.1.4 on 2022-12-14 13:16

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_product_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=None, default=None, force_format='WEBP', keep_meta=True, quality=75, scale=None, size=[1920, 1080], upload_to='imgs/'),
        ),
    ]