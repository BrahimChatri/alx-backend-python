#!/usr/bin/env python3
import logging
from datetime import datetime
from django.http import HttpResponseForbidden
from django.http import JsonResponse
from time import time

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('requests.log')
formatter = logging.Formatter('%(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)

message_tracker = {}

class RolepermissionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = request.user
        if request.path.startswith('/admin/') or request.path.startswith('/moderator-only/'):
            if not user.is_authenticated or user.role not in ['admin', 'moderator']:
                return HttpResponseForbidden("403 Forbidden: You don't have permission to access this resource.")
        return self.get_response(request)


class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = request.user if request.user.is_authenticated else "Anonymous"
        logger.info(f"{datetime.now()} - User: {user} - Path: {request.path}")
        return self.get_response(request)

class RestrictAccessByTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        current_hour = datetime.now().hour
        if current_hour < 18 or current_hour >= 21:
            return HttpResponseForbidden("Chat access allowed only between 6PM and 9PM")
        return self.get_response(request)


class OffensiveLanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.method == 'POST' and 'messages' in request.path:
            ip = request.META.get('REMOTE_ADDR')
            now = time()
            if ip not in message_tracker:
                message_tracker[ip] = []
            message_tracker[ip] = [t for t in message_tracker[ip] if now - t < 60]

            if len(message_tracker[ip]) >= 5:
                return JsonResponse({'error': 'Rate limit exceeded. Max 5 messages per minute.'}, status=429)

            message_tracker[ip].append(now)
        return self.get_response(request)

class RolePermissionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = request.user
        if request.path.startswith('/admin-only/') or request.path.startswith('/moderator-only/'):
            if not user.is_authenticated or not hasattr(user, 'role') or user.role not in ['admin', 'moderator']:
                return HttpResponseForbidden("You do not have the required permissions.")
        return self.get_response(request)
