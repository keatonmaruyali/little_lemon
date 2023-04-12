from django.urls import path, include
from . import views

from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'book', views.BookingViewSet, 'book')

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('menu/', views.MenuItemView.as_view(), name="menu"),
    path(
        'menu/<int:pk>/',
        views.MenuItemSingleView.as_view(),
        name="menu_item",
    ),
    path('reservations/', include(router.urls)),
]
