import re
from django.shortcuts import render,redirect
from django.contrib.auth import login
from .forms import SignupForm
from django.contrib.auth.models import User

# from django.http.response import HttpResponse

# Create your views here.

def login(request):
    return render(request,'accounts/navbar.html')

def login_user(request):
    return render(request, 'accounts/login.html')



def register(request):
	if request.method == 'POST':
		form = SignupForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			email = form.cleaned_data.get('email')
			password = form.cleaned_data.get('password')
			User.objects.create_user(username=username, email=email, password=password)
			return redirect('index')
	else:
		form = SignupForm()
	
	context = {
		'form':form,
	}

	return render(request, 'accounts/register.html', context)

