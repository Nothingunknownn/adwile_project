from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import TextField, CharField, ForeignKey, UUIDField
from django.utils.translation import gettext_lazy as _

from uuid import uuid4


User = get_user_model()


class Teaser(models.Model):

    class Category(models.IntegerChoices):
        FIRST = 1, _('Первая категория')
        SECOND = 2, _('Вторая категория')
        THIRD = 3, _('Третья категория')

    class Status(models.IntegerChoices):
        PENDING = 1, _("На рассмотрении")
        PAID = 2, _("Оплачен")
        REJECTED = 3, _("Отклонен")

    id = UUIDField(primary_key=True, default=uuid4, editable=False)
    title = CharField(max_length=64)
    description = TextField(max_length=256)
    author = ForeignKey(User, on_delete=models.CASCADE)
    category = models.IntegerField(
        choices=Category.choices,
        default=Category.FIRST,
    )
    status = models.IntegerField(
        choices=Status.choices,
        default=Status.PENDING,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Тизер'
        verbose_name_plural = 'Тизеры'
