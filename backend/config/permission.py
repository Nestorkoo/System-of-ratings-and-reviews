from rest_framework.permissions import BasePermission


class IsAdminOrModerator(BasePermission):

    def has_permission(self, request, view):
        return request.user and (request.user.roles == 'admin' or request.user.roles == 'moderator')