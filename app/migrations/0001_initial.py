# Generated by Django 2.2.12 on 2020-10-19 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticker_pair', models.CharField(max_length=20, verbose_name='Ticker pair')),
                ('frequency', models.CharField(max_length=10, verbose_name='Frequency')),
                ('timestamp', models.DateTimeField()),
                ('open_price', models.DecimalField(decimal_places=8, max_digits=16, verbose_name='Open')),
                ('low_price', models.DecimalField(decimal_places=8, max_digits=16, verbose_name='Low')),
                ('high_price', models.DecimalField(decimal_places=8, max_digits=16, verbose_name='High')),
                ('close_price', models.DecimalField(decimal_places=8, max_digits=16, verbose_name='Close')),
            ],
        ),
    ]