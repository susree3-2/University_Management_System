
class ResourceAllocationAgent:
    """
    Resource Allocation Agent:
    - Assigns best room based on capacity
    - Avoids room conflicts
    """

    def __init__(self, courses, rooms, schedules):
        self.courses = courses
        self.rooms = rooms
        self.schedules = schedules

    def is_room_available(self, room, timeslot):
        """
        Check if room is already booked at a given timeslot
        """
        for schedule in self.schedules:
            if schedule.room == room and schedule.timeslot == timeslot:
                return False  # Room already booked
        return True

    def assign_rooms(self):
        """
     Assign rooms to existing schedules

    Logic:
    - For each schedule, find best room
    - Match capacity
    - Avoid double booking
    """
        allocations = []

        for schedule in self.schedules:
            course = schedule.course
            timeslot = schedule.timeslot

            best_room = None

            for room in self.rooms:

                # Check capacity condition
                if room.capacity >= course.students:

                    # REQ-11: avoid double booking
                    is_available = True
                    for s in self.schedules:
                        if s.room == room and s.timeslot == timeslot and s.id != schedule.id:
                            is_available = False
                            break
                    if is_available:
                        # choose smallest suitable room (optimization)
                        if not best_room or room.capacity < best_room.capacity:
                            best_room = room
            if best_room:
                allocations.append(
                f"{course.name} → {best_room.name} at {timeslot}"
            )
            else:
                allocations.append(
                f"No suitable room for {course.name} at {timeslot}"
            )
        return allocations