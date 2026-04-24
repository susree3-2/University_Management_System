

class SchedulerAgent:
    """
    Scheduler Agent:
    Responsible for detecting scheduling conflicts
    """

    def __init__(self, schedules):
        # schedules = list or queryset of Schedule objects
        self.schedules = schedules

    def detect_conflicts(self):
        """
        Detect:
        1. Same room booked at same time
        2. Same course scheduled twice at same time
        """

        conflicts = []

        # Loop through all schedules
        for s1 in self.schedules:
            for s2 in self.schedules:

                # Skip comparing same schedule
                if s1.id == s2.id:
                    continue

                # If timeslot is same
                if s1.timeslot == s2.timeslot:

                    # Conflict 1: Room double booked
                    if s1.room == s2.room:
                        conflicts.append(
                            f"{s1.room} is double booked at {s1.timeslot}"
                        )

                    # Conflict 2: Course duplicated
                    if s1.course == s2.course:
                        conflicts.append(
                            f"Course {s1.course} has multiple schedules at {s1.timeslot}"
                        )

        # Remove duplicate messages
        return list(set(conflicts))
    
    def generate_schedule(self, courses, rooms, timeslots):
        """
    Generate schedule for courses

    Logic:
    - Assign each course a room and timeslot
    - Avoid conflicts
    - Respect room capacity
    """
        generated = []
        for course in courses:
            assigned = False
            for timeslot in timeslots:
                for room in rooms:
                    # Check capacity
                    if room.capacity >= course.students:
                        conflict = False
                        # Check if room already booked
                        for s in self.schedules:
                            if s.room == room and s.timeslot == timeslot:
                                conflict = True
                                break
                            if not conflict:
                                generated.append(
                                    f"{course.name} scheduled in {room.name} at {timeslot}"
                                )
                                assigned = True
                                break
                if assigned:
                    break
            if not assigned:
                generated.append(
                    f"Could not schedule {course.name}"
                )
        return generated