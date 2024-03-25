from django.urls import path,include
from . import views

urlpatterns = [
    path('list/entries/<str:date>/',views.list_entries,name="main_view"),
]
