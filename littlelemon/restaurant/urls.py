from django.urls import path, include
from . import views

from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'tables', views.BookingViewSet)

urlpatterns = [
    # path('', views.home, name="home"),
    # path('about/', views.about, name="about"),
    # path('book/', views.book, name="book"),
    # path('reservations/', views.reservations, name="reservations"),
    path('menu/', views.MenuItemView.as_view(), name="menu"),
    path('menu/<int:pk>/', views.MenuItemSingleView.as_view(), name="menu_item"),  
    path('restaurant/booking/', include(router.urls)),
    path('users/', views.UserView.as_view()),
    # path('bookings', views.bookings, name='bookings'), 
]
