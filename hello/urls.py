from django.urls import path

from . import views 

urlpatterns = [
    path("", views.index, name="index"),
    path("logout", views.logout_view, name = 'logout'),
    path('data-visualization/', views.data_visualization, name='data-visualization'),
]