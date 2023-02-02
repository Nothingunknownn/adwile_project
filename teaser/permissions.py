from rest_framework import permissions
from rest_framework.request import Request

from .models import Teaser


class IsOwnerOrAdmin(permissions.BasePermission):
    """Проверка на доступ к объекту - Создатель или Админ."""

    def has_object_permission(self, request: Request, view, obj: Teaser):
        # is_staff - отвечает за то что пользователь админ
        # альтернативное условие что пользователь создатель
        return request.user.is_staff or obj.author == request.user