from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsPortfolioOwnerOrReadOnly(BasePermission):
    message = "Only the portfolio owner can change projects."

    def has_permission(self, request, view):
        return (
            request.method in SAFE_METHODS
            or request.user.is_superuser
        )


class IsPortfolioOwnerOrEditorOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

        if request.method in ['PUT', 'PATCH']:
            return request.user and request.user.is_authenticated and (
                request.user.is_superuser or 
                request.user.is_staff or 
                request.user.groups.filter(name='Editor').exists()
            )

        if request.method in ['POST', 'DELETE']:
            return request.user and request.user.is_authenticated and request.user.is_superuser

        return False