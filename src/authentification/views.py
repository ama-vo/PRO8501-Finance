from django.contrib import messages
from django.shortcuts import redirect, render
from authentification.models import FinanceUser
from django.contrib.auth import authenticate, login
from allauth.account.forms import LoginForm
from allauth.account.models import EmailAddress
from allauth.account.views import ConfirmLoginCodeView
from allauth.account.internal.stagekit import clear_login
# Create your views here.
def index(request):

    return render(request, "index.html")

otp = ConfirmLoginCodeView.as_view(template_name="login/otp.html")


def cancel_login_code(request):
    clear_login(request)
    return redirect("login")

def login_user(request):

    if request.method == "POST" :

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)


        if user:

            login(request,user)

            return redirect('otp')

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


        if not email:

            messages.error(request, 'An email address is required to receive the verification code.')
            return redirect('signup')


        if password != confirmedpassword:

            messages.error(request, 'The password confirmation does not match.')
            return redirect('signup')

        else:



            new_user = FinanceUser.objects.create_user(
                username=username,
                first_name=firstname,
                last_name=lastname,
                email=email,
                password=password,
                address="",
                phone="",
            )
            EmailAddress.objects.create(
                user=new_user,
                email=email,
                primary=True,
            )

        # Same flow as the login page: emails a code, then redirects to the OTP page.
        form = LoginForm(
            data={"login": username, "password": password},
            request=request,
        )
        if form.is_valid():
            return form.login(request)

        return redirect('login')



    return render(request,"signin/signup.html")