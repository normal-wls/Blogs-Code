from django.urls import path, include
from rest_framework.routers import DefaultRouter

from books import views


router = DefaultRouter()
router.register('books', views.BooksViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', views.login_view),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]