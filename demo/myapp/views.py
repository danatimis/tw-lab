from django.shortcuts import render, HttpResponse

def loadingscreen(request):
    return render(request, "HTML/loading.html")

def login(request):
    return render(request, "HTML/login.html")

def home(request):
    return render(request, "HTML/home.html")

def register(request):
    return render(request, "HTML/register.html")

def chatbot(request):
    return render(request, "HTML/chatbot.html")

def universities(request):
    return render(request, "HTML/universities.html")