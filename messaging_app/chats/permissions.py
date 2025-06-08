#!/usr/bin/env python3 

from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS

class IsParticipantOfConversation(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        user = request.user
        if request.method in SAFE_METHODS + ("PUT", "PATCH", "DELETE"):
            return user in obj.conversation.participants.all()
        return False
