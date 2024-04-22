
from django.contrib import admin
from django.urls import path,include
from .views import *
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('login', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('snippets/', SnippetListCreateView.as_view(), name='snippet-list-create'),
    path('snippets/<int:pk>',SnippetsDetail.as_view(),name='snippet-detail'),
    path('tags/',TagListCreateView.as_view(), name='tags-list-create'),
    path('tags/<int:pk>',TagDetail.as_view(),name='tags-detail'),
]