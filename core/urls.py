from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('next/<str:zip>/', views.next, name='next'),
    # path('mail/<str:zip>/', views.mail, name='mail'),
    # path('success/', views.success, name='success'),
]