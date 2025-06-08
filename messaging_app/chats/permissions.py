from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsParticipantOfConversation(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user in obj.participants.all()

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated
