from django.urls import path
from . import views

app_name= 'sample'
urlpatterns = [
	path('index', views.IndexView.as_view(), name="index_view"),
	path('registration', views.RegistrationView.as_view(), name="register_view"),

]