from django.test import TestCase
from core.agents.scheduler import SchedulerAgent


# Dummy Schedule class to simulate the real model
class DummySchedule:
    def __init__(self, id, room, timeslot, course):
        self.id = id
        self.room = room
        self.timeslot = timeslot
        self.course = course


class SchedulerAgentTest(TestCase):

    def test_room_conflict(self):
        """Same room + same timeslot → conflict"""

        s1 = DummySchedule(1, "Room101", "10AM", "CSE101")
        s2 = DummySchedule(2, "Room101", "10AM", "CSE102")

        agent = SchedulerAgent([s1, s2])
        conflicts = agent.detect_conflicts()

        self.assertIn("Room101 is double booked at 10AM", conflicts)

    def test_course_conflict(self):
        """Same course + same timeslot → conflict"""

        s1 = DummySchedule(1, "Room101", "10AM", "CSE101")
        s2 = DummySchedule(2, "Room102", "10AM", "CSE101")

        agent = SchedulerAgent([s1, s2])
        conflicts = agent.detect_conflicts()

        self.assertIn(
            "Course CSE101 has multiple schedules at 10AM",
            conflicts
        )

    def test_no_conflict(self):
        """Different room & timeslot → no conflict"""

        s1 = DummySchedule(1, "Room101", "10AM", "CSE101")
        s2 = DummySchedule(2, "Room102", "12PM", "CSE102")

        agent = SchedulerAgent([s1, s2])
        conflicts = agent.detect_conflicts()

        self.assertEqual(len(conflicts), 0)
