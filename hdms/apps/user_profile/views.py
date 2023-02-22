from django.shortcuts import render
from django.http import HttpResponse


def dashboard(request):
    html = "<html><body><p>Dashboard Page</p></body></html>" % now
    return HttpResponse(html)
