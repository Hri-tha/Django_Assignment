# chat/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ChatViewSet, ChatHistoryViewSet, home

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'chats', ChatViewSet)

urlpatterns = [
    path('', home, name='home'),
    path('api/', include(router.urls)),
    path('history/<int:user_id>/', ChatHistoryViewSet.as_view({'get': 'list'})),
]


# router = DefaultRouter()
# router.register(r'users', UserViewSet)
# router.register(r'chats', ChatViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
# ]
