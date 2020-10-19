from django.db import models



# Moeda Periodicidade Datetime Open Low High Close


class Candle(models.Model):
    ticker_pair = models.CharField("Ticker pair", max_length=20)
    frequency = models.CharField("Frequency", max_length=10)
    timestamp = models.DateTimeField()
    open_price = models.DecimalField("Open", decimal_places=8, max_digits=16)
    low_price = models.DecimalField("Low", decimal_places=8, max_digits=16)
    high_price = models.DecimalField("High", decimal_places=8, max_digits=16)
    close_price = models.DecimalField("Close", decimal_places=8, max_digits=16)

    def __str__(self):
        return f"{self.ticker_pair} {self.frequency}"


