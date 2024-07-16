# chat/views.py
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.conf import settings
from .models import User, Chat
from .serializers import UserSerializer, ChatSerializer
from .services import HuggingFaceService
# chat/views.py
from django.shortcuts import render

def home(request):
    return render(request, 'chat/home.html')


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ChatViewSet(viewsets.ModelViewSet):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer

    @action(detail=False, methods=['post'])
    def interact(self, request):
        user_id = request.data.get('user_id')
        model_name = request.data.get('model_name')
        prompt = request.data.get('prompt')

        if not all([user_id, model_name, prompt]):
            return Response({'error': 'Missing parameters'}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.get(id=user_id)
        model = settings.HUGGING_FACE_MODELS.get(model_name)
        if not model:
            return Response({'error': 'Invalid model name'}, status=status.HTTP_400_BAD_REQUEST)

        service = HuggingFaceService(model)
        response = service.generate_response(prompt)

        chat = Chat.objects.create(user=user, model_name=model_name, prompt=prompt, response=response)
        serializer = ChatSerializer(chat)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


# chat/views.py
class ChatHistoryViewSet(viewsets.ViewSet):
    def list(self, request, user_id=None):
        chats = Chat.objects.filter(user_id=user_id)
        serializer = ChatSerializer(chats, many=True)
        return Response(serializer.data)
