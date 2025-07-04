from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from .models import ExpenseIncome
from .serializers import ExpenseIncomeSerializer
from .permissions import IsOwnerOrSuperuser
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import api_view


# Create your views here.
class ExpenseIncomeViewSet(viewsets.ModelViewSet):
    serializer_class = ExpenseIncomeSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrSuperuser]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return ExpenseIncome.objects.all()
        return ExpenseIncome.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
@api_view(['POST'])
def register_user(request):
    if request.method == 'POST':
        username =request.data.get('username')
        password = request.data.get('password')

        if User.objects.filter(username=username).exists():
            return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)
    

        user=User.objects.create_user(username=username, password=password)
        user.save()
        return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
    return Response({'error': 'Invalid request method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)