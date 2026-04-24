from django.shortcuts import render
from .models import Course, Room, Schedule, TimeSlot,Student, Enrollment
from .agents.scheduler import SchedulerAgent                     # import the agent
from .agents.resource_agent import ResourceAllocationAgent
from .agents.risk_agent import RiskDetectorAgent


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
    courses = Course.objects.all()
    rooms = Room.objects.all()
    timeslots = TimeSlot.objects.all()
    students = Student.objects.all()
    enrollments = Enrollment.objects.all()

    # Initialize the Scheduler Agent
    scheduler = SchedulerAgent(schedules)

    # Detect conflicts
    conflicts = scheduler.detect_conflicts()

    #  generate schedule
    generated_schedule = scheduler.generate_schedule(courses, rooms, timeslots)

    # Resource Allocation Agent
    resource_agent = ResourceAllocationAgent(courses, rooms, schedules)
    allocations = resource_agent.assign_rooms()

    risk_agent = RiskDetectorAgent(students, enrollments, schedules)
    risks = risk_agent.detect_risks()
    recommendations = risk_agent.recommendations()

    # Send conflicts to template
    return render(request, 'admin.html', {
        'conflicts': conflicts,
        'allocations': allocations,
        'generated_schedule': generated_schedule,
        'risks': risks,
        'recommendations': recommendations
    })