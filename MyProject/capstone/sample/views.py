from django.shortcuts import render, redirect
from django.http import Http404
from django.http import HttpResponse
from django.views.generic import View
from .forms import *
from django.contrib import messages
from .models import *
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login
# Imports for Video Calling
from agora_token_builder import RtcTokenBuilder
from django.http import JsonResponse
import random
import time
import json

from .models import RoomMember
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

class IndexView(View):
		def get(self, request):
			return render(request, 'index.html')

		# def post(self, request):
		# 	if 'login' in request.POST:
		# 		return redirect('sample:register')


class RegistrationView(View):
		def get(self, request):
			return render(request, 'register.html')

		def post(self, request):
			form = StudentForm(request.POST)

			if form.is_valid():
				firstname = request.POST['firstname']
				lastname = request.POST['lastname']
				idnum = request.POST['idnum']
				email = request.POST['email']
				course = request.POST['course'] 
				year = request.POST['year']
				gender = request.POST['gender']
				contact = request.POST['contact']
				password = request.POST['password']
				cpassword = request.POST['cpassword']

				if password != cpassword:
					messages.error(request, 'Password do not match!')
					return redirect('sample:register')

				elif password == cpassword:
					form = Student(firstname=firstname, lastname=lastname, idnum = idnum, email = email,  course = course, year = year, gender = gender, contact = contact, password = password)
					form.save()
					print('student created')
					#messages.success(request, 'Your account has been successfully registered!')
					return redirect('sample:login')


class AdviserRegistrationView(View):
		def get(self, request):
			return render(request, 'registerAdviser.html')

		def post(self,request):
			form = AdviserForm(request.POST)

			if form.is_valid():
				firstname = request.POST['firstname']
				lastname = request.POST['lastname']
				idnum = request.POST['idnum']
				email = request.POST['email']
				contact = request.POST['contact']
				password = request.POST['password']
				cpassword = request.POST['cpassword']

				if password != cpassword:
					messages.error(request, 'Password do not match')
					return redirect('sample:aregister')

				elif password == cpassword:
					form = Adviser(firstname=firstname, lastname=lastname, idnum = idnum, email = email, contact = contact, password = password)	
					form.save()
					print('adviser created')
					return redirect('sample:alogin')

def login(request):
	if request.method == 'POST':
		email = request.POST.get('email')
		password = request.POST.get('password')
		students = Student.objects.all()

		if Student.objects.filter(email=email).count() != 0 :
			account = Student.objects.get(email=email)
			print('account')
			if account.password == password:
				print('login successful')
				Student.objects.filter(email=email).update(isLoggedIn = True)
				return redirect('/home?'+email)

			elif account.password != password: 
				messages.error(request, 'Incorrect Password')
				return render(request,'login.html')

		else:
			messages.error(request, 'Username does not exist!')
			return render(request,'login.html')
	else:
		return render(request,'login.html')

def alogin(request):
	if request.method == 'POST':
		email = request.POST.get('email')
		password = request.POST.get('password')
		adviser = Adviser.objects.all()

		if Adviser.objects.filter(email=email).count() != 0:
			account = Adviser.objects.get(email=email)
			print('adviser account')
			if account.password == password:
				print('adviser login successful')
				Adviser.objects.filter(email=email).update(isLoggedIn = True)
				return redirect('/ahome?'+email)

			elif account.password != password:
				messages.error(request,'Incorrect Password')
				return render(request,'alogin.html')

		else:
			messages.error(request,'Username does not exist!')
			return render(request,'alogin.html')
	else:
		return render(request,'alogin.html')

class HomeView(View):
	def get(self, request):
		students = Student.objects.all()
		
		for student in students:
			if(student.isLoggedIn == True):
				return render(request, 'home.html', {'students':student})
	
		return redirect('sample:login')

class AdviserHomeView(View):
	def get(self, request):
		try:
			adviser_online = Adviser.objects.get(isLoggedIn = True)
		except:
			return redirect('sample:alogin')

		student = Student.objects.all()
		appointment = Appointment.objects.filter(meeting_counselor=adviser_online.adviserID,is_Approved=0)
	
		approved_chat = Appointment.objects.filter(meeting_counselor=adviser_online.adviserID,is_Approved=1,meeting_type = 'chat')
		approved_live = Appointment.objects.filter(meeting_counselor=adviser_online.adviserID,is_Approved=1,meeting_type = 'live')
		context ={
			'advisers':adviser_online,
			'students':student,
			'appointments':appointment,
			'approved_chat':approved_chat,
			'approved_live':approved_live,
			
		}
		
		if(adviser_online.isLoggedIn == True):
			return render(request, 'homeAdviser.html', context)

	def post(self, request):
		if request.method == 'POST':
			if 'btnApprove' in request.POST:	
				print('approve button clicked')
				sid = request.POST.get("sid")
				aid = request.POST.get("aid")
				apid = request.POST.get("apid")
				print(sid)
				print(aid)
				print(apid)
				update_appointment_status = Appointment.objects.filter(student_id = sid, meeting_counselor_id = aid, appointmentID =apid).update(is_Approved = 1, meeting_status='approved')

				print('appointment approved')
				return redirect('sample:ahome')

			elif 'btnUpdate' in request.POST:
				print('Update Button Clicked')
				sid = request.POST.get("sid")
				aid = request.POST.get("aid")
				apid = request.POST.get("apid")
				meeting_date = request.POST.get("newdate")
				meeting_time = request.POST.get("newtime")
				print(meeting_date)
				print(meeting_time)

				update_appointment = Appointment.objects.filter(student_id = sid, meeting_counselor_id = aid, appointmentID = apid).update(meeting_date = meeting_date, meeting_time = meeting_time,is_Approved = 1, meeting_status='re-scheduled' )

				print('appointment updated')
				return redirect('sample:ahome')	
			
class AboutView(View):
		def get(self, request):
			students = Student.objects.all()

			for student in students:
				if(student.isLoggedIn == True):
					return render(request, 'about.html', {'students':student})

			return redirect('sample:login')		

class ContactView(View):
		def get(self, request):
			students = Student.objects.all()

			for student in students:
				if(student.isLoggedIn == True):
					return render(request, 'contact.html', {'students':student})

			return redirect('sample:login')		
			
class SettingView(View):
		def get(self, request):
			students = Student.objects.all()

			for student in students:
				if(student.isLoggedIn == True):
					return render(request, 'setting.html', {'students':student})

			return redirect('sample:login')		

		def post(self, request):
			if request.method == 'POST':
				if 'btnUpdate' in request.POST:
					print('update button clicked')
					sid = request.POST.get("sid")
					firstname = request.POST.get("firstname")
					lastname = request.POST.get("lastname")
					email = request.POST.get("email")
					contact = request.POST.get("contact")
					course = request.POST.get("course")
					year = request.POST.get("year")
					
					update_student = Student.objects.filter(studentID = sid).update(firstname = firstname, lastname = lastname, email = email, contact = contact, course = course, year = year)

					print(update_student)
					return redirect('sample:home')
					
class LogoutView(View):
	def get(self, request):
		students = Student.objects.all()
		advisers = Adviser.objects.all()

		for student in students:
			if(student.isLoggedIn == True):
				Student.objects.update(isLoggedIn = False)
				print('user successfully log out')
				return redirect('sample:index')

		for adviser in advisers:
			if(adviser.isLoggedIn == True):
				Adviser.objects.update(isLoggedIn = False)
				print('user successfully log out')
				return redirect('sample:index')
		

class SetAppointmentView(View):
		def get(self, request):
			advisers = Adviser.objects.all()
			students = Student.objects.all()

			for student in students:
				if(student.isLoggedIn == True):
					return render(request, 'setappointment.html', {'students':student, 'adviser':advisers})

		def post(self, request):
			form = AppointmentForm(request.POST)

			if form.is_valid():
				student_id = request.POST['student_id']
				meeting_type = request.POST['meeting_type']
				meeting_counselor_id = request.POST['meeting_counselor']
				meeting_date = request.POST['meeting_date']
				meeting_time = request.POST['meeting_time']

				form = Appointment(meeting_type=meeting_type, meeting_counselor_id=meeting_counselor_id, meeting_date=meeting_date, meeting_time=meeting_time, student_id=student_id)
				form.save()
				print('appointment saved')
				return redirect('sample:home')
			
			else:
				return redirect('sample:setappointment')

class ViewAppointmentView(View):
		def get(self, request):
			adviser = Adviser.objects.all()
			student_online = Student.objects.get(isLoggedIn = True)
			appointment = Appointment.objects.filter(student = student_online.studentID)
			chat_appointment = Appointment.objects.filter(student = student_online.studentID, meeting_type='chat')
			live_appointment = Appointment.objects.filter(student = student_online.studentID, meeting_type='live')

			context ={
				'advisers':adviser,
				'students':student_online,
				'appointments':appointment,
				'live_appointment':live_appointment,
				'chat_appointment':chat_appointment,
			}

			if(student_online.isLoggedIn == True):
				return render(request, 'viewappointment.html', context)

			return redirect('sample:login')

class AdviserLoginView(View):
		def get(self, request):
			return render(request, 'loginAdviser.html')


class AdviserAboutView(View):
		def get(self, request):
			advisers = Adviser.objects.all()

			for adviser in advisers:
				if(adviser.isLoggedIn == True):
					return render(request, 'aabout.html', {'advisers':adviser})

			return redirect('sample:alogin')

class AdviserContactView(View):
		def get(self, request):
			advisers = Adviser.objects.all()

			for adviser in advisers:
				if(adviser.isLoggedIn == True):
					return render(request, 'acontact.html', {'advisers':adviser})

			return redirect('sample:alogin')
			
class AdviserSettingView(View):
		def get(self, request):
			advisers = Adviser.objects.all()

			for adviser in advisers:
				if(adviser.isLoggedIn == True):
					return render(request, 'asetting.html', {'advisers':adviser})

			return redirect('sample:alogin')
			
		def post(self, request):
			if request.method == 'POST':
				if 'btnUpdate' in request.POST:
					print('update button clicked')
					sid = request.POST.get("sid")
					firstname = request.POST.get("firstname")
					lastname = request.POST.get("lastname")
					email = request.POST.get("email")
					contact = request.POST.get("contact")
					
					update_adviser = Adviser.objects.filter(adviserID = sid).update(firstname = firstname, lastname = lastname, email = email, contact = contact)

					print(update_adviser)
					return redirect('sample:ahome')

def lobby(request):
	advisers = Adviser.objects.all()
	for adviser in advisers:
		if(adviser.isLoggedIn == True):
			return render(request, 'lobby.html', {'advisers':adviser})


def videoroom(request):
	return render(request, 'room.html')

def getToken(request):
	appId = 'd988d90c6efd41f0b05a8a209f59c6a2'
	appCertificate = '6a3551c1e8dd4f8989aa0cfef4a47229'
	channelName = request.GET.get('channel')
	uid = random.randint(1, 230)
	expirationTimeInSeconds = 3600
	currentTimeStamp = int(time.time())
	privilegeExpiredTs = currentTimeStamp + expirationTimeInSeconds
	role = 1

	token = RtcTokenBuilder.buildTokenWithUid(appId, appCertificate, channelName, uid, role, privilegeExpiredTs)

	return JsonResponse({'token': token, 'uid': uid}, safe=False)

@csrf_exempt
def createMember(request):
    data = json.loads(request.body)
    member, created = RoomMember.objects.get_or_create(
        name=data['name'],
        uid=data['UID'],
        room_name=data['room_name']
    )

    return JsonResponse({'name':data['name']}, safe=False)

def getMember(request):
    uid = request.GET.get('UID')
    room_name = request.GET.get('room_name')

    member = RoomMember.objects.get(
        uid=uid,
        room_name=room_name,
    )
    name = member.name
    return JsonResponse({'name':member.name}, safe=False)

@csrf_exempt
def deleteMember(request):
    data = json.loads(request.body)
    member = RoomMember.objects.get(
        name=data['name'],
        uid=data['UID'],
        room_name=data['room_name']
    )
    member.delete()
    return JsonResponse('Member deleted', safe=False)


def chathome(request):
	return render(request, 'chathome.html')

def room(request,room):
	username = request.GET.get('username')
	room_details = Room.objects.get(name=room)
	return render(request, 'chatroom.html', {
		'username': username,
		'room': room,
		'room_details': room_details
		})

def checkview(request):
	room = request.POST['room_name']
	username = request.POST['username']

	if Room.objects.filter(name=room).exists():
		return redirect('/'+room+'/?username='+username)

	else:
		new_room = Room.objects.create(name=room)
		new_room.save()
		return redirect('/'+room+'/?username='+username)


def send(request):
	message = request.POST['message']
	username = request.POST['username']
	room_id = request.POST['room_id']

	new_message = Message.objects.create(value=message, user=username, room=room_id)
	new_message.save()
	return HttpResponse('Message sent')

def getMessages(request, room):
    room_details = Room.objects.get(name=room)

    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})

def ratings(request):
	return render(request, 'ratings.html')
