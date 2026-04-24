from django.shortcuts import render
from .models import Course, Schedule
from .agents.scheduler import SchedulerAgent   # import the agent

def index(request):
    return render(request, 'index.html')

def student(request):
    courses = Course.objects.all()   # get all courses
    return render(request, 'student.html', {'courses': courses})

def faculty(request):
    return render(request, 'faculty.html')

def admin_dashboard(request):
    # Get all schedules from database
    schedules = Schedule.objects.all()

    # Initialize the Scheduler Agent
    agent = SchedulerAgent(schedules)

    # Detect conflicts
    conflicts = agent.detect_conflicts()

    # Send conflicts to template
    return render(request, 'admin.html', {
        'conflicts': conflicts
    })