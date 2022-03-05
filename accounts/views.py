import re
from django.shortcuts import render
# from django.http.response import HttpResponse

# Create your views here.

def login(request):
    return render(request,'accounts/navbar.html')
    
def register():
    pass