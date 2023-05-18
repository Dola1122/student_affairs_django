from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Admin
from django.contrib.auth.hashers import make_password
from .forms import LoginForm
from django.contrib import messages

# Create your views here.


####################  Ahmed Adel Start  ####################


####################  Ahmed Adel End    ####################




####################  Mohamed Elmanori Start  ####################


####################  Mohamed Elmanori End    ####################




####################  John Start  ####################

def index(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())

def home(request):
  template = loader.get_template('html/home.html')
  return HttpResponse(template.render())

def signup(request):
    if request.method == 'POST':
        entered_username = request.POST['username']
        entered_phone = request.POST['phone']
        entered_email = request.POST['email']
        entered_password = request.POST['password']
        entered_gender = request.POST['gender']

        existing_user = Admin.objects.filter(username=entered_username)
        if existing_user.exists():
            context = {'error_message': 'Username already taken!'}
            return render(request, 'html/signup.html', context)

        new_user = Admin(username=entered_username, phone=entered_phone, email=entered_email,password=entered_password, gender=entered_gender)
        new_user.save()

        return redirect('login.html')

    return render(request, 'html/signup.html')


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = Admin.objects.filter(username=username,password=password)
            if user.exists():
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('home.html')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = LoginForm()
    return render(request=request, template_name='html/login.html', context={'form': form})
####################  John End    ####################




####################  Ahmed Younes Start  ####################


####################  Ahmed Younes End    ####################




####################  Sahar Start  ####################


####################  Sahar End    ####################

