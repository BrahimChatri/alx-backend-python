from rest_framework.routers import DefaultRouter
from .views import ConversationViewSet, MessageViewSet
from django.urls import path, include

router = DefaultRouter()
router.register('conversations', ConversationViewSet)
router.register('messages', MessageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
