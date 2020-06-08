import json

from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from books.models import Books
from books.serializer import BooksSerializer


class BooksViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer


def login_view(request):
    # data = json.loads(request.body.decode('utf-8'))
    # username = data.get('user')
    # password = data.get('password')
    user = auth.authenticate(request, username='Tom', password='tompassword')
    if user is not None and user.is_active:
        auth.login(request, user)
    return HttpResponse("Login Success")
