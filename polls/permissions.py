from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of a poll to edit or delete it.
    """
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed for any request (GET, HEAD, OPTIONS)
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Write permissions are only allowed to the owner
        return obj.owner == request.user

class IsVoter(permissions.BasePermission):
    """
    Custom permission to only allow users to cast one vote per poll.
    """
    def has_permission(self, request, view):
        # Allow all authenticated users to attempt to vote
        return request.user.is_authenticated