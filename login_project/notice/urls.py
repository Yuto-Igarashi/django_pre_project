from django.urls import path
from . import views

app_name = 'notice'
urlpatterns = [
    path('list/',views.listTemplate.as_view(), name='list'),
    path('<int:pk>/',views.detailTemplate.as_view(), name='detail'),
]