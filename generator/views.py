from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.


def home_page(request):
    return render(request, "generator/home.html")


def aboutpage(request):

    return render(request, "generator/about.html")


def password(request):

    the_password = ""
    characters = list('abcdefghijklmnopqrstuvwxyz')
    length = int(request.GET.get('length'))
    if request.GET.get("isuppercase"):
        characters.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    if request.GET.get("isspecial"):
        characters.extend("~!@#$%^&*()_+-/?|")
    if request.GET.get("isnumber"):
        characters.extend("0123456789")
    for i in range(length):
        the_password += random.choice(characters)
    return render(request, "generator/generatedPassword.html", {'password': the_password})