from django.urls import path

from . import views

app_name ="diary"

urlpatterns = [
    path("",views.IndexView.as_view(),name='index'),
    path('<int:pk>/',views.detailView.as_view(), name='detail'),
    path('create/',views.createView.as_view(),name='create'),
]

