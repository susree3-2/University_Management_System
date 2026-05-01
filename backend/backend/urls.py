"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from core.views import index, student, faculty, admin_dashboard, add_course, allocate_classroom,add_room, add_timeslot, create_schedule

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', index),
    path('student/', student),
    path('faculty/', faculty),
    path('admin-dashboard/', admin_dashboard),
    path('add-course/', add_course, name='add_course'), 
    path('allocate-classroom/', allocate_classroom, name='allocate_classroom'),
    path('add-room/', add_room, name='add_room'),
    path('add-timeslot/', add_timeslot, name='add_timeslot'),
    path('create-schedule/', create_schedule, name='create_schedule'),
    
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.BASE_DIR / "templates")
