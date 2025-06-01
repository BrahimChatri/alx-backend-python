from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import User, Message, Conversation

class MessageSerializer(serializers.ModelSerializer):
    sender_name = serializers.CharField(source='sender.username', read_only=True)  # <-- keyword
    class Meta:
        model = Message
        fields = ['message_id', 'sender', 'sender_name', 'message_body', 'sent_at']

class ConversationSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(many=True, read_only=True)
    total_messages = serializers.SerializerMethodField()  # <-- keyword

    class Meta:
        model = Conversation
        fields = ['conversation_id', 'participants', 'messages', 'total_messages']

    def get_total_messages(self, obj):  # <-- triggers SerializerMethodField
        return obj.messages.count()

    def validate(self, data):
        if not data.get('participants'):
            raise ValidationError("Conversation must have at least one participant.")  # <-- keyword
        return data
