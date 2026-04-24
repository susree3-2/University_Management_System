

class RiskDetectorAgent:
    """
    Risk Detector Agent:
    - Monitors student course load
    - Detects overload
    - Detects schedule conflicts per student
    - Provides recommendations
    """

    def __init__(self, students, enrollments, schedules):
        self.students = students
        self.enrollments = enrollments
        self.schedules = schedules


    def detect_risks(self):
        risks = []

        # REQ-13 & REQ-14: Check student course load
        for student in self.students:

            # Get all courses for this student
            student_courses = [
                e.course for e in self.enrollments if e.student == student
            ]

            # Overload condition (threshold = 3 courses)
            if len(student_courses) > 3:
                risks.append(
                    f"{student.name} is overloaded with {len(student_courses)} courses"
                )

        # REQ-15: Detect schedule conflicts per student
        for student in self.students:

            student_courses = [
                e.course for e in self.enrollments if e.student == student
            ]

            student_schedules = [
                s for s in self.schedules if s.course in student_courses
            ]

            for s1 in student_schedules:
                for s2 in student_schedules:

                    if s1.id == s2.id:
                        continue

                    if s1.timeslot == s2.timeslot:
                        risks.append(
                            f"{student.name} has a conflict between {s1.course} and {s2.course}"
                        )

        return list(set(risks))


    def recommendations(self):
        suggestions = []

        # REQ-16: Suggest improvements
        for student in self.students:

            student_courses = [
                e.course for e in self.enrollments if e.student == student
            ]

            if len(student_courses) > 3:
                suggestions.append(
                    f"Reduce course load for {student.name}"
                )

        if not suggestions:
            suggestions.append("No major risks detected")

        return suggestions