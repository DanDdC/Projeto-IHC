from django.shortcuts import render

def auth_view(request):
    return render(request, 'auth.html')

def home_view(request):
    return render(request, 'home.html')