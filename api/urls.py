from django.urls import path

from .views import get_articles, get_article, create_article, edit_article, delete_article

urlpatterns = [
    path('', get_articles),
    path('<int:pk>', get_article),
    path('<int:pk>/create/', create_article),
    path('<int:pk>/edit/', edit_article),
    path('<int:pk>/delete', delete_article),
]