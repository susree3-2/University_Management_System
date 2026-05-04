#  University Management System with Autonomous AI Agents

##  Demo Access
- Admin Login (Google OAuth): /
- Admin Dashboard: /admin-dashboard/
- Django Admin Panel: /admin/

##  Overview

This project is a **University Management System** enhanced with **Autonomous AI Agents** that assist in scheduling, resource allocation, and risk detection.

The system simulates how intelligent agents can support administrative decision-making in an academic environment.

---

##  Key Features

### Google Federated Login (OAuth 2.0)

- Secure admin login using Google account
- Integrated using Django Allauth
- Eliminates need for manual password management

---

###  AI Agents

The system includes four intelligent agents:

* **Scheduler Agent**

  * Detects scheduling conflicts
  * Identifies duplicate course timings and room clashes

* **Resource Allocation Agent**

  * Assigns optimal classrooms based on capacity
  * Prevents double booking of rooms

* **Risk Detection Agent**

  * Detects student course overload
  * Identifies schedule conflicts for students

* **Advisor Agent**

  * Provides recommendations based on system analysis
  * Suggests solutions like rescheduling or reducing workload

---

###  Admin Dashboard

* View system-wide schedules
* Detect conflicts automatically
* Allocate classrooms using AI
* Add courses, rooms, and timeslots
* View AI-generated recommendations

---

###  Student & Faculty Dashboards

* Basic interface to represent system roles
* Connected to the same centralized database
* Included for system completeness and demonstration

---

##  Database Models

* **Course** – Stores course information
* **Room** – Stores classroom details and capacity
* **TimeSlot** – Represents scheduling time
* **Schedule** – Links course, room, and timeslot
* **Student** – Stores student data
* **Enrollment** – Links students with courses

---

##  Technologies Used

* Backend: Django (Python)
* Database: SQLite (default Django DB)
* Frontend: HTML, CSS
* Authentication: Google OAuth 2.0 (Django Allauth)
* AI Logic: Rule-based intelligent agents

---

##  System Workflow

1. Admin logs in using Google account
2. Admin creates courses, rooms, and schedules
3. AI agents automatically:
   - Detect conflicts
   - Allocate classrooms
   - Identify risks
4. Advisor Agent generates recommendations
5. Admin takes action based on system insights

---

##  Purpose

This project demonstrates how **AI-driven agents** can:

* Improve scheduling efficiency
* Optimize resource usage
* Assist in decision-making

---

## Unit Testing

Unit testing has been implemented for the **Scheduler Agent** to verify the correctness of conflict detection logic.

### Test Cases Covered:
- Room conflict detection (same room, same timeslot)  
- Course conflict detection (same course, same timeslot)  
- No-conflict scenario validation  

### How to Run Tests:
```bash
python manage.py test
```

All tests pass successfully, confirming that the scheduling logic works as expected.

---

##  Note


* Student and faculty dashboards are minimal and used for system representation

---

##  Future Improvements

* Fully automated scheduling system
*  Advanced role-based access control (Admin/Faculty/Student)
* Real-time notifications

---

##  Author

CSE327 Project – Group 6

