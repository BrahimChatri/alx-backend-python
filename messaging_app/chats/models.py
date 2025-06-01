#!/usr/bin/env python3
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Extend default User with any extra fields you want, e.g.:
    bio = models.TextField(blank=True, null=True)
    # Add more custom fields if needed

    def __str__(self):
        return self.username


class Conversation(models.Model):
    # Many-to-many relationship to track participants of the conversation
    participants = models.ManyToManyField(User, related_name='conversations')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        participant_names = ", ".join([user.username for user in self.participants.all()])
        return f"Conversation between: {participant_names}"


class Message(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages_sent')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    # Optionally add a read status or attachment fields

    def __str__(self):
        return f"Message from {self.sender.username} at {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}"
