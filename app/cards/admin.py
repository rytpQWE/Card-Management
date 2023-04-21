from django.contrib import admin
from django.contrib.admin import ModelAdmin

from cards.models import Card
from users.models import User


# pass for all users EcfuqZE4r!nyXtDT
@admin.register(User)
@admin.register(Card)
class CardAdmin(ModelAdmin):
    pass


class HistoryAdmin(ModelAdmin):
    readonly_fields = ('series',)


