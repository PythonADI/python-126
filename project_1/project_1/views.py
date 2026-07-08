from django.http import HttpResponse
from django.shortcuts import render


def home_page(request, name):
    return render(
        request, 
        "home.html", 
        {
            "name": name
        }
    )
