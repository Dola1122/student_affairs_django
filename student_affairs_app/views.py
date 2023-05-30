from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Admin, Student
from django.contrib.auth.hashers import make_password
from .forms import LoginForm
from django.contrib import messages

# Create your views here.


####################  Ahmed Adel Start  ####################

def add_student(request):
    template = loader.get_template('html/add_student.html')
    return HttpResponse(template.render())

def add_student(request):
    if request.method == 'POST':
        # Create a new student object with the submitted form data
        student = Student(
            name=request.POST['name'],
            email=request.POST['email'],
            mobile=request.POST['mobile'],
            IDnum=request.POST['IDnum'],
            birthDate=request.POST['birthDate'],
            gpa=request.POST['gpa'],
            level=request.POST['level'],
            dep=request.POST['dep'],
            gender=request.POST['gender'],
            status=request.POST['status']
        )
        # Save the student object to the database
        student.save()
        # Display a success message
        messages.success(request, 'Student added successfully!')
        # Redirect to the same page or any other page you desire
        # return redirect('add_student')

    # If the request method is GET, render the add_student.html template
    return render(request, 'html/add_student.html')

####################  Ahmed Adel End    ####################




####################  Mohamed Elmanori Start  ####################
# def edit_student(request):
#   template = loader.get_template('html/edit_student.html')
#   return HttpResponse(template.render())

def edit_student(request, id):
  student = Student.objects.get(id=id)
  template = loader.get_template('html/edit_student.html')
  context = {
    'student': student
    }
  return HttpResponse(template.render(context, request))

def updaterecord(request, id):

  name = request.POST['name']
  email = request.POST['email']
  gpa = request.POST['gpa']
  level = request.POST['level']
  gender = request.POST['gender']
  status = request.POST['status']
  student = Student.objects.get(id=id)
  student.name = name
  student.email = email
  student.gpa = gpa
  student.level = level
  student.gender = gender
  student.status = status
  student.save()
  #template = loader.get_template('html/student_list.html')
  #return HttpResponse(template.render())

  return HttpResponseRedirect(reverse('student_list'))


def delete(request, id):
  student = Student.objects.get(id=id)
  student.delete()
  return HttpResponseRedirect(reverse('student_list'))



def assign_department(request):
  template = loader.get_template('html/assign_department.html')
  return HttpResponse(template.render())

def assign_department(request, id):
  student = Student.objects.get(id=id)
  template = loader.get_template('html/assign_department.html')
  context = {
    'student': student
    }
  return HttpResponse(template.render(context, request))

def updateDep(request, id):

  # name = request.POST['name']
  # email = request.POST['email']
  # gpa = request.POST['gpa']
  dep = request.POST['dep']
  # level = request.POST['level']
  # gender = request.POST['gender']
  # status = request.POST['status']
  student = Student.objects.get(id=id)
  # student.name = name
  student.dep = dep
  # student.email = email
  # student.gpa = gpa
  # student.level = lev/el
  # student.gender = gender
  # student.status = status
  student.save()
  #template = loader.get_template('html/student_list.html')
  #return HttpResponse(template.render())

  return HttpResponseRedirect(reverse('student_list'))

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

def student_list(request):
  students = Student.objects.all()
  return render(request, 'html/student_list.html', {'students':students})

####################  Ahmed Younes End    ####################




####################  Sahar Start  ####################

def search(request):
  template = loader.get_template('html/search.html')
  return HttpResponse(template.render())

def search(request):
    students = Student.objects.all()
    return render(request, 'html/search.html', {'students':students})

####################  Sahar End    ####################

