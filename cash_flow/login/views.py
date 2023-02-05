from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def login(request):
    return render(request, 'login/login.html')


def register(request):
    return HttpResponse("Test")


def logout(request):
    pass
