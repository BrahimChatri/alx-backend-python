#!/usr/bin/env python3
from rest_framework import serializers
from .models import User, Conversation, Message

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'bio']  # Include custom fields if any


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['message_id', 'sender', 'message_body', 'sent_at']

class ConversationSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(many=True, read_only=True)
    participants = serializers.StringRelatedField(many=True)

    class Meta:
        model = Conversation
        fields = ['conversation_id', 'participants', 'messages']
