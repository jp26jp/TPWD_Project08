from django.urls import path, re_path

from . import views

app_name = "minerals"

urlpatterns = [
    path('', views.index, name='list'),
    path('letter/<str:letter>/', views.letter, name='letter'),
    path('<slug:slug>', views.detail, name='detail'),
    path('search/', views.search, name='search')
]
