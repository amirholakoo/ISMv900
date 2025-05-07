import jdatetime
from num2fawords import words

class PersianDateText:
    months = ['فروردین', 'اردیبهشت', 'خرداد', 'تیر', 'مرداد', 'شهریور',
              'مهر', 'آبان', 'آذر', 'دی', 'بهمن', 'اسفند']

    def __init__(self, date_list):
        if not isinstance(date_list, list) or len(date_list) != 3:
            raise ValueError("Input must be a list like [year, month, day]")

        self.year, self.month, self.day = map(int, date_list)
        self.jdate = jdatetime.date(self.year, self.month, self.day)

    def to_text(self):
        year_text = words(self.year)
        month_name = self.months[self.month - 1]
        day_text = words(self.day)

        return f"{day_text} {month_name} {year_text}"
