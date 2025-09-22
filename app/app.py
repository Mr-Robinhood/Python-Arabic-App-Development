import reflex as rx
from app.pages.role_selection import role_selection_page
from app.pages.login import login_page
from app.pages.admin_dashboard import admin_dashboard_page
from app.pages.professor_dashboard import professor_dashboard_page
from app.pages.student_dashboard import student_dashboard_page

app = rx.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(rel="preconnect", href="https://fonts.gstatic.com", crossorigin=""),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700&display=swap",
            rel="stylesheet",
        ),
    ],
)


@rx.page(route="/", title="Select Role")
def role_selection() -> rx.Component:
    return rx.el.main(role_selection_page(), dir="rtl", class_name="font-['Tajawal']")


@rx.page(route="/login", title="Login")
def login() -> rx.Component:
    return rx.el.main(login_page(), dir="rtl", class_name="font-['Tajawal']")


@rx.page(route="/admin/dashboard", title="Admin Dashboard")
def admin_dashboard() -> rx.Component:
    return rx.el.main(admin_dashboard_page(), dir="rtl", class_name="font-['Tajawal']")


@rx.page(route="/professor/dashboard", title="Professor Dashboard")
def professor_dashboard() -> rx.Component:
    return rx.el.main(
        professor_dashboard_page(), dir="rtl", class_name="font-['Tajawal']"
    )


@rx.page(route="/student/dashboard", title="Student Dashboard")
def student_dashboard() -> rx.Component:
    return rx.el.main(
        student_dashboard_page(), dir="rtl", class_name="font-['Tajawal']"
    )


app.add_page(role_selection)
app.add_page(login)
app.add_page(admin_dashboard)
app.add_page(professor_dashboard)
app.add_page(student_dashboard)