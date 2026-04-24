

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