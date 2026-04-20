from django.shortcuts import render
from .models import Course

def index(request):
    return render(request, 'index.html')

def student(request):
    courses = Course.objects.all()   # get all courses
    return render(request, 'student.html', {'courses': courses})

def faculty(request):
    return render(request, 'faculty.html')

def admin_dashboard(request):
    return render(request, 'admin.html')