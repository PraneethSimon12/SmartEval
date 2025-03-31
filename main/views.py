from django.shortcuts import render
from django.http import HttpResponseRedirect

def login_register_view(request):
    if request.method == 'POST':
        if 'username' in request.POST:
            # Registration form submitted
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            print("Registering:", username, email, password)
            # You can handle user creation here or use Django forms
        elif 'login_username' in request.POST:
            # Login form submitted
            login_username = request.POST.get('login_username')
            login_password = request.POST.get('login_password')
            print("Logging in:", login_username, login_password)
            # You can handle authentication here

        return HttpResponseRedirect('/')  # Redirect to same page after form submit

    return render(request, 'main/login_register.html')
