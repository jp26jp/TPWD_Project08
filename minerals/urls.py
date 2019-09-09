from django.urls import path

from . import views

app_name = "minerals"

urlpatterns = [
    path('', views.index, name='list'),
    path('letter/<str:letter>/', views.letter, name='letter'),
    path('group/<str:group>/', views.group, name='group'),
    path('<slug:slug>', views.detail, name='detail'),
    path('search/', views.search, name='search'),
    path('random/', views.random_mineral, name='random')
]
