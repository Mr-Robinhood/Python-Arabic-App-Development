import reflex as rx


class StudentDashboardState(rx.State):
    courses_count: str = "5"
    assignments_due: str = "2"
    gpa: str = "3.85"
    schedule_today_count: str = "2"