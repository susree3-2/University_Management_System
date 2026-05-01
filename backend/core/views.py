from django.shortcuts import render
from .models import Course, Room, Schedule, TimeSlot,Student, Enrollment
from .agents.scheduler import SchedulerAgent                        # import the agent
from .agents.resource_agent import ResourceAllocationAgent
from .agents.risk_agent import RiskDetectorAgent
from .agents.advisor_agent import AdvisorAgent
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.http import HttpResponse
from allauth.socialaccount.models import SocialAccount


def index(request):
    return render(request, 'index.html')

def student(request):
    courses = Course.objects.all()   # get all courses
    return render(request, 'student.html', {'courses': courses})

def faculty(request):
    return render(request, 'faculty.html')

def admin_dashboard(request):
    if not request.user.is_authenticated:
        return redirect('/')
    social_account = SocialAccount.objects.filter(user=request.user).first()
    if not social_account:
        return HttpResponse("Access Denied")
    user_email = social_account.extra_data.get('email')

    ALLOWED_ADMINS = [
        "sumaiyasusree@gmail.com"
    ]
    if user_email not in ALLOWED_ADMINS:
        return HttpResponse("Access Denied")
    
    action = request.GET.get('action')
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

    # Resource Allocation Agent
    allocations = request.session.pop('allocations', [])

    risk_agent = RiskDetectorAgent(students, enrollments, schedules)
    risks = risk_agent.detect_risks()
    recommendations = risk_agent.recommendations()

    advisor = AdvisorAgent(conflicts, allocations, risks)
    advice = advisor.generate_advice()

    # Send conflicts to template
    return render(request, 'admin.html', {
        'action': action,
        'conflicts': conflicts,
        'allocations': allocations,
        'risks': risks,
        'recommendations': recommendations,
        'advice': advice,
        'rooms': rooms,
        'courses': courses, 
        'timeslots': timeslots, 
        'students': students,
        'courses_count': courses.count()
    })

def add_course(request):
    if request.method == "POST":
        name = request.POST.get('name')
        students = request.POST.get('students')

        if name and students:
            Course.objects.create(
                name=name,
                students=int(students)
            )

    return redirect('/admin-dashboard/')

def allocate_classroom(request):
    schedules = Schedule.objects.all()
    rooms = Room.objects.all()
    courses = Course.objects.all()

    agent = ResourceAllocationAgent(courses, rooms, schedules)
    allocations = agent.assign_rooms()

    # STORE results in session
    request.session['allocations'] = allocations

    return redirect('/admin-dashboard/')

def add_room(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        capacity = request.POST.get('capacity')

        Room.objects.create(
            name=name,
            capacity=capacity
        )

    return redirect('/admin-dashboard/')

def add_timeslot(request):
    if request.method == 'POST':
        day = request.POST.get('day')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')

        TimeSlot.objects.create(
            day=day,
            start_time=start_time,
            end_time=end_time
        )

    return redirect('/admin-dashboard/')

def create_schedule(request):
    if request.method == "POST":
        course_id = request.POST.get('course_id')
        timeslot_id = request.POST.get('timeslot_id')

        course = Course.objects.get(id=course_id)
        timeslot = TimeSlot.objects.get(id=timeslot_id)

        # Create schedule WITHOUT room (AI will assign later)
        Schedule.objects.create(
            course=course,
            timeslot=timeslot,
            room=Room.objects.first()  # temporary room (will be fixed by AI)
        )

    return redirect('/admin-dashboard/')

