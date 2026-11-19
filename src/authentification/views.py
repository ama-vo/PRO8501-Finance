from django.contrib import messages
from django.shortcuts import redirect, render
from authentification.models import FinanceUser
from django.contrib.auth import authenticate, login
# Create your views here.
def index(request):

    return render(request, "index.html")

def login_user(request):

    if request.method == "POST" :

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)


        if user:

            login(request,user)

            return redirect('index')

        else:
            messages.error(request, 'wrong password or user does not exist.')
            return redirect('login')

        

    return render(request,"login/login.html")

def signup(request):

    if request.method == "POST":

        username = request.POST.get("username")
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirmedpassword = request.POST.get("confirmedpassword")

        if FinanceUser.objects.filter(username=username).exists():

            messages.error(request, 'User already exist.')
            return redirect('signup')


        if password != confirmedpassword:

            messages.error(request, 'The password confirmation does not match.')
            return redirect('signup')

        else:



            new_user = new_user = FinanceUser.objects.create_user(
            username=username,
            first_name=firstname,
            last_name=lastname,
            email=email,
            password=password
        )

        return render(request,"index.html")



    return render(request,"signin/signup.html")