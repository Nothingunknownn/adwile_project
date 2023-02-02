from django.contrib import admin

from .models import Teaser


@admin.register(Teaser)
class TeaserAdmin(admin.ModelAdmin):

    # Поля отображающиеся в админке
    list_display = (
        "id",
        "title",
        "author",
        "description",
        "status",
        "created_at",
        "updated_at",
    )
    # Поля предполагающие филтрацию
    list_filter = (
        "status",
    )

    # Не изменяемые поля, только для чтения
    readonly_fields = [
        "id",
        "created_at",
        "updated_at",
    ]

    # Поля по которым происходит поиск
    search_fields = (
        "id",
        "title",
        "author__username",
        "description",
    )

    # Отображение тизеров на странице
    list_per_page = 20

    # Разделяет окно Создания и Редактирования на два сета:
    # Основная информация и Время
    fieldsets = (
        (
            "Main info",
            {
                "fields": ("id", ("title", "author"), "status", "description"),
                "description": "Все поля в этом блоке обязательны для заполнения",
            },
        ),
        (
            "Timestamps",
            {
                "fields": (
                    "created_at",
                    "updated_at",
                )
            },
        ),
    )

    def get_readonly_fields(self, request, obj: Teaser = None):
        """Делает поле `Статус` только для чтения после изменения с `На рассмотрении`"""
        if not obj or (obj and obj.status != Teaser.Status.PENDING):
            return self.readonly_fields + ["status"]

        return self.readonly_fields
