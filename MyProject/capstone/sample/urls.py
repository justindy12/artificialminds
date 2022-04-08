from django.urls import path
from . import views

app_name= 'sample'
urlpatterns = [
	path('', views.IndexView.as_view(), name="index"),
	path('register', views.RegistrationView.as_view(), name="register"),
	path('aregister', views.AdviserRegistrationView.as_view(), name="aregister"),
	path('login', views.login, name="login"),	
	path('alogin', views.alogin, name="alogin"),
	path('home', views.HomeView.as_view(), name="home"),
	path('ahome', views.AdviserHomeView.as_view(), name="ahome"),
	path('about', views.AboutView.as_view(), name="about"),
	path('aabout', views.AdviserAboutView.as_view(), name="aabout"),
	path('contact', views.ContactView.as_view(), name="contact"),
	path('acontact', views.AdviserContactView.as_view(), name="acontact"),
	path('setting', views.SettingView.as_view(), name="setting"),
	path('asetting', views.AdviserSettingView.as_view(), name="asetting"),
	path('logout', views.LogoutView.as_view(), name="logout"),
	path('setappointment', views.SetAppointmentView.as_view(), name="setappointment"),
	path('viewappointment', views.ViewAppointmentView.as_view(), name="viewappointment"),
	path('lobby/', views.lobby),
	path('videoroom/', views.videoroom),
	path('get_token/', views.getToken),
	path('create_member/', views.createMember),
	path('get_member/', views.getMember),
	path('delete_member/', views.deleteMember),
	path('chathome', views.chathome, name='chathome'),
    path('<str:room>/', views.room, name='room'),
    path('checkview', views.checkview, name='checkview'),
    path('send', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
    path('ratings', views.ratings, name="ratings"),

]

