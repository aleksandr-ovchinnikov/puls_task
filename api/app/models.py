from django.db import models
from django_resized import ResizedImageField


ORDER_CHOICES = [
    ('1', 'In stock'),
    ('2', 'On order'),
    ('3', 'Await receipt'),
    ('4', 'Not available'),
    ('5', 'Not produces')
]
# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    article = models.IntegerField()
    price = models.FloatField()
    status = models.CharField(
        choices=ORDER_CHOICES, max_length=100, default='in stock')
    image = ResizedImageField(force_format="WEBP", quality=75, upload_to='imgs/', default='/home/theblindone/codeProjects/PythonProjects/puls_task/api/app/imgs/1.jpg')

    class Meta:
        ordering = ['status']
