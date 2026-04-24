# core/agents/resource_agent.py

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
        Assign best available room to each course
        """
        allocations = []

        for course in self.courses:

            best_room = None

            for room in self.rooms:

                # Check capacity condition
                if room.capacity >= course.students:

                    # Check availability (avoid conflict)
                    # NOTE: here we assume same timeslot for simplicity
                    # later we can improve this
                    timeslot = self.schedules.first().timeslot if self.schedules.exists() else None

                    if timeslot and self.is_room_available(room, timeslot):

                        # Choose smallest suitable room (optimization)
                        if not best_room or room.capacity < best_room.capacity:
                            best_room = room

            if best_room:
                allocations.append(
                    f"{course.name} → {best_room.name} (Capacity: {best_room.capacity})"
                )
            else:
                allocations.append(
                    f"No available room for {course.name}"
                )

        return allocations