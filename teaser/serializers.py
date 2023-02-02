from rest_framework import serializers

from .models import Teaser


class TeaserCreateSerializer(serializers.ModelSerializer):
    """Запрещает обычным пользователям менять поля 'Статус' и 'Автор' при создании тизера"""

    class Meta:
        model = Teaser
        exclude = ["status", "author"]


class TeaserUpdateSerializer(serializers.ModelSerializer):
    """Запрещает обычным пользователям менять поля 'Статус' и 'Автор' при обновлении тизера"""

    # Вынесено в отдельный класс для последующего расширения
    class Meta:
        model = Teaser
        exclude = ["status", "author"]


class TeaserViewSerializer(serializers.ModelSerializer):
    """Сериализует все поля модели."""

    class Meta:
        model = Teaser
        fields = "__all__"


class TeaserUpdateAdminSerializer(serializers.ModelSerializer):
    """Позволяет изменить все поля за исключением 'Статус' при смене с 'На рассмотрении'"""

    def validate_status(self, value: str):
        if self.instance.status != Teaser.Status.PENDING:
            raise serializers.ValidationError(
                f"Невозможно изменить статус с {self.instance.status}"
            )
        return value

    class Meta:
        model = Teaser
        fields = "__all__"
