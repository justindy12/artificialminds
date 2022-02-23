from django.urls import path
from . import views

app_name= 'sample'
urlpatterns = [
	path('', views.IndexView.as_view(), name="index"),
	path('register', views.RegistrationView.as_view(), name="register"),
	path('aregister', views.AdviserRegistrationView.as_view(), name="aregister"),
	path('login', views.login, name="login"),	
	path('alogin', views.AdviserLoginView.as_view(), name="alogin"),
	path('home', views.HomeView.as_view(), name="home"),
	path('about', views.AboutView.as_view(), name="about"),
	path('contact', views.ContactView.as_view(), name="contact"),
	path('setting', views.SettingView.as_view(), name="setting"),
	path('logout', views.LogoutView.as_view(), name="logout"),
	path('setappointment', views.SetAppointmentView.as_view(), name="setappointment"),
	path('viewappointment', views.ViewAppointmentView.as_view(), name="viewappointment"),

]

