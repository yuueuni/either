from django.shortcuts import render


# Create your views here.
def signup(request):
    pass


def login(request):
    return render(request, 'accounts/login.html')


def logout(request):
    pass