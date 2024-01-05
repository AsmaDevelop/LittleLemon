from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from .models import Menu,Booking
from .serializers import MenuSerializer, BookingSerializer

# Create your views here.

def index(request):
    return render(request, 'index.html')
def home(request):
    return render(request, 'home.html')

class MenuItemView(generics.ListCreateAPIView):
    #permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
  
class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    #permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
class BookingViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
   queryset = Booking.objects.all()
   serializer_class = BookingSerializer
   