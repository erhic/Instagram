import re
from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import login
from .forms import SignupForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# from django.http.response import HttpResponse
# account registration using email
from django.core.mail import EmailMessage
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site

# Create your views here.



def register(request):
	if request.method == 'POST':
		form = SignupForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			email = form.cleaned_data.get('email')
			password = form.cleaned_data.get('password')
			User.objects.create_user(username=username, email=email, password=password)
			messages.info(request, f'Account created successfully')
            
	else:
     
		form = SignupForm()
         
   
	context = {
		'form':form,
	}

	return render(request, 'accounts/register.html', context)



def login_user(request):
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email = email, password = password)

        if user is not None:
            login(request, user)
            messages.info(request, f'Logged in successfully')
            return redirect('register')
        
    
    return render(request, 'accounts/login.html')

def activate(request, uib64, token):
    
    return HttpResponse("Account Activated successful!")

