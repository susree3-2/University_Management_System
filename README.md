#  University Management System with Autonomous AI Agents

##  Demo Access
- Admin Dashboard: /admin-dashboard/
- Django Admin Panel: /admin/

##  Overview

This project is a **University Management System** enhanced with **Autonomous AI Agents** that assist in scheduling, resource allocation, and risk detection.

The system simulates how intelligent agents can support administrative decision-making in an academic environment.

---

##  Key Features

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
* AI Logic: Rule-based intelligent agents

---

##  System Workflow

1. Admin creates courses, rooms, and schedules
2. AI agents analyze the system:

   * Detect conflicts
   * Allocate resources
   * Identify risks
3. Advisor agent suggests improvements
4. Admin takes action based on recommendations

---

##  Purpose

This project demonstrates how **AI-driven agents** can:

* Improve scheduling efficiency
* Optimize resource usage
* Assist in decision-making

---

##  Note

* Authentication is simplified for demonstration purposes
* Student and faculty dashboards are minimal and used for system representation

---

##  Future Improvements

* Google Federated Login (OAuth 2.0)
* Fully automated scheduling system
* Role-based authentication system
* Real-time notifications

---

##  Author

CSE327 Project – Group 6

