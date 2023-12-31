#define URL route for index() view
from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('menu/', views.MenuItemView.as_view(), name= 'menu'),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
]
