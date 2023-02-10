import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")

import django

django.setup()

import random
from datetime import datetime
from datetime import timedelta
from cards.models import Card
from faker import Faker

fake = Faker()


def us(request):
    return request.user.id


def get_random_date(start, end):
    delta = end - start
    return start + timedelta(random.randint(0, delta.days))


start_dt = datetime.strptime('01.01.2023', '%m.%d.%Y')
end_dt = datetime.strptime('01.01.2024', '%m.%d.%Y')


def generator(value):
    for i in range(value):
        name = fake.name()
        series = random.randint(1, 2147483647)
        created = datetime.now()
        end_date = get_random_date(start_dt, end_dt)
        obj = Card.objects.get_or_create(name=name, series=series, created=created, end_date=end_date)


def main():
    n = int(input('How many cards you want to send: '))
    generator(n)


if __name__ == "__main__":
    main()
