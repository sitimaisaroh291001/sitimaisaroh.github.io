from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name = 'members'),
    path('base/', views.base, name = 'base'),
    path('django/', views.django, name = 'django'),
    path('menu/', views.menu, name = 'menu'),
    path('menu1/', views.menu1, name = 'menu1'),
]