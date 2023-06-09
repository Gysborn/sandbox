from rest_framework import permissions


class IsOwnerOrAdmin(permissions.BasePermission):
    """
    Допуск владельца или админа
    """

    def has_object_permission(self, request, view, obj):
        if obj.id == request.user.id:
            return True
        return bool(request.user and request.user.is_staff)


class IsAuthOrAdmin(permissions.BasePermission):
    """
    Допуск авторизованного или админа
    """

    def has_permission(self, request, view):
        if bool(request.user and request.user.is_authenticated):
            return True
        else:
            return bool(request.user and request.user.is_staff)
