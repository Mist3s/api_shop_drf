from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    """Чтение или доступно только Администратору."""

    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
            and request.user.is_superuser
        )
