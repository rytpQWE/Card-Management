import pytz
from django.db import models
from datetime import datetime

from users.models import User


class Card(models.Model):
    name = models.CharField(max_length=100)
    series = models.IntegerField(unique=True)
    created = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField('Дата окончания', editable=True, blank=True, null=True)
    activation = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

    @property
    def expiration_date(self):
        tz_me = pytz.timezone('Asia/Bangkok')
        now_time = tz_me.localize(datetime.now())
        # (self.end_date - self.created) - действие карты(в секундах)
        # (now_time - self.created) - кол-во секунд с момента создания
        if (self.end_date - self.created).total_seconds() < (now_time - self.created).total_seconds():
            return False
        return True


class History(models.Model):
    use_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    series = models.IntegerField(null=True)

    def __str__(self):
        return f'History: {self.user}'
