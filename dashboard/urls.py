from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.dashboard,name="main_view"),
    path('calendar/',views.calendar,name="calendar"),
    path('entry/<str:dateEntry>/',views.entry,name="entry"),
    path('api/',include('dashboard.api_urls'),name="api"),
]
