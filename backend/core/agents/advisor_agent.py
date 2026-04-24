

class AdvisorAgent:
    """
    Advisor Agent:
    - Provides high-level recommendations
    - Uses outputs from other agents
    """

    def __init__(self, conflicts, allocations, risks):
        self.conflicts = conflicts
        self.allocations = allocations
        self.risks = risks


    def generate_advice(self):
        advice = []

        # 🔴 If there are conflicts → suggest rescheduling
        if self.conflicts:
            advice.append(
                "Reschedule conflicting courses to different time slots"
            )

        # 🔴 If allocation issues exist
        for alloc in self.allocations:
            if "No suitable room" in alloc:
                advice.append(
                    "Increase classroom capacity or reduce class size"
                )

        # 🔴 If risks exist → interpret them
        for risk in self.risks:

            if "overloaded" in risk:
                advice.append(
                    "Reduce student course load or offer additional sections"
                )

            if "conflict" in risk:
                advice.append(
                    "Adjust timetable to eliminate student conflicts"
                )

        # Remove duplicates
        advice = list(set(advice))

        # If nothing found
        if not advice:
            advice.append("System is operating efficiently")

        return advice