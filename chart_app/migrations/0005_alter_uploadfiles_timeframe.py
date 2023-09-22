# Generated by Django 4.2.5 on 2023-09-22 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chart_app', '0004_alter_uploadfiles_timeframe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadfiles',
            name='timeframe',
            field=models.CharField(choices=[('', 'Select timeframe'), ('1min', '1min'), ('5min', '5min'), ('15min', '15min'), ('30min', '30min'), ('1H', '1H'), ('4H', '4H'), ('D', '1D')], default='', max_length=5),
        ),
    ]
