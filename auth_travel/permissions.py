from clients.models import User_Register, client_token_authentication
from rest_framework import permissions
from .authentication import SafeJWTAuthentication


class IsAuthenticated(permissions.BasePermission):
    """
    Allows access only to authenticated users.
    """

    def has_permission(self, request, view):
        try:
            if request.user.is_anonymous:
                return False
        except:
            return True
