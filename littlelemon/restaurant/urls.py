from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MenuItemsView, SingleMenuItemView
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('menu/', MenuItemsView.as_view(), name='menu-items'),
    path('menu/items/', MenuItemsView.as_view(), name='menu-items-alias'),
    path('menu/<int:pk>/', SingleMenuItemView.as_view(), name='menu-item-detail'),
    path('api-token-auth/', obtain_auth_token),
]
