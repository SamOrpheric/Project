"""
URL configuration for HelloDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from rest_framework import routers
from . import views

from .views import CommentViewSet

router = routers.DefaultRouter()
router.register(r'comments', CommentViewSet)

app_name = 'blog'
urlpatterns = [
    path('', include(routers.urls)),
    path('', views.post_list, name='post_list'),
    path('posts/<int:id>/', views.post_detail, name='post_detail'),
    path('posts/<int:id>/edit/', views.post_edit, name='post_edit'),
    path('posts/<int:id>/publish/', views.post_publish, name='post_publish'),
    path('comment/<int:id>/add/', views.add_comment, name='add_comment'),
    path('post/add/', views.post_edit, name='post_add'),
]
