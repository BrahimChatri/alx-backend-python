#!/usr/bin/env python3
from rest_framework import serializers
from .models import User, Conversation, Message

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'bio']  # Include custom fields if any


class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)  # Nested sender info

    class Meta:
        model = Message
        fields = ['id', 'sender', 'content', 'timestamp']


class ConversationSerializer(serializers.ModelSerializer):
    participants = UserSerializer(many=True, read_only=True)  # Nested users in conversation
    messages = MessageSerializer(many=True, read_only=True)  # Nested messages in conversation

    class Meta:
        model = Conversation
        fields = ['id', 'participants', 'created_at', 'messages']
