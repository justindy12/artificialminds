from django.urls import path
from . import views

app_name= 'sample'
urlpatterns = [
	path('index', views.IndexView.as_view(), name="index_view"),
	path('register', views.RegistrationView.as_view(), name="register"),
	path('login', views.LoginView.as_view(), name="login"),
]