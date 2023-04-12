from datetime import datetime
import json

from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, viewsets
from rest_framework.response import Response

# from .forms import BookingForm
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer, UserSerializer


@csrf_exempt
def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    ordering_fields = ['price', 'inventory']
    filterset_fields = ['price', 'inventory']
    search_fields = ['title']


class MenuItemSingleView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def list(self, request):
        queryset = Booking.objects.all()
        serializer = BookingSerializer(queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, request):
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(status=201)

    def retrieve(self, request, pk=None):
        booking = Booking.objects.all()
        booking = get_object_or_404(booking, pk=pk)
        serializer = BookingSerializer(booking)
        return Response(serializer.data)

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        booking = Booking.objects.all()
        booking = get_object_or_404(booking, pk=pk)
        booking.delete()
        return HttpResponse(status=200)


class UserView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [IsAdminUser]

    # def get_queryset(self):
    #     users = User.objects.all()
    #     return users
