from django.db import models

# Create your models here.

class Uploadfiles(models.Model):
    choises = [('', 'Select timeframe',),
               ('1min', '1min',),
               ('5min', '5min',),
               ('15min', '15min',),
               ('30min', '30min',),
               ('1H', '1H',),
               ('4H', '4H',),
               ('D', '1D',),
               ]

    file = models.FileField(upload_to='files/%d/%m/%Y')
    timeframe = models.CharField(choices=choises, max_length=5, default='')
    ex_mov_average = models.IntegerField(blank=True, null=True)
