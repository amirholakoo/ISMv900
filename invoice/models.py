from django.db import models
from invoice.utils import PersianDateText

class Invoice(models.Model):
    queue = models.AutoField(primary_key=True)

    year = models.IntegerField()
    month = models.IntegerField()
    day = models.IntegerField()

    @property
    def persian_date_text(self):
        return PersianDateText([self.year, self.month, self.day]).to_text()

# {{ event.persian_date_text }}
# Invoice.get_persian_date_text()