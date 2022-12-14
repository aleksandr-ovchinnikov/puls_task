# Generated by Django 4.1.4 on 2022-12-14 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('1', 'In stock'), ('2', 'On order'), ('3', 'Await receipt'), ('4', 'Not available'), ('5', 'Not produces')], default='in stock', max_length=100),
        ),
    ]
