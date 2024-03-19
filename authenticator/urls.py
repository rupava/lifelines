from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('signup/',views.signup,name="signup"),
    path('login/', auth_views.LoginView.as_view(template_name='html/authenticator/login.html'), name='login'),
]
