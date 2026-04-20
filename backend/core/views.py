from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def student(request):
    return render(request, 'student.html')

def faculty(request):
    return render(request, 'faculty.html')

def admin_dashboard(request):
    return render(request, 'admin.html')