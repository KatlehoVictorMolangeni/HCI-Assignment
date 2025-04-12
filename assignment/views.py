from django.shortcuts import render, redirect
from .models import student_details
from .forms import LoginForm

def Login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            
            try:
                student = student_details.objects.get(username=username, password=password)
                request.session['student_id'] = student.id
                return redirect('dashboard')
            except student_details.DoesNotExist:
                try:
                    student_details.objects.get(username=username)
                    return render(request, 'login.html', {'form': form, 'error': 'Invalid password'})
                except student_details.DoesNotExist:
                    return render(request, 'login.html', {'form': form, 'error': 'Username does not exist'})
    
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form': form})


def home(request):
    return render(request, 'index.html');

def Dashboard(request):
    student_id = request.session.get('student_id')

    if not student_id:
        return redirect('login')  # if not logged in, redirect to login

    try:
        student = student_details.objects.get(id=student_id)
    except student_details.DoesNotExist:
        return redirect('login')

    return render(request, 'Dashboard.html', {'student': student})

def Manage_Assignment(request):
    return render(request, 'assignments.html')

def view_quotes(request):
    return render(request, 'quotes.html')

def study_plane(request):
    return render(request, 'study.html')

def register(request):
    return render(request, 'register.html')