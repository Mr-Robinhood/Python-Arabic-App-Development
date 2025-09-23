import reflex as rx
from app.pages.login import login_page
from app.pages.role_selection import role_selection_page
from app.pages.student_dashboard import student_dashboard_page
from app.pages.professor_dashboard import professor_dashboard_page
from app.pages.admin_dashboard import admin_dashboard_page

app = rx.App(theme=rx.theme(appearance="light"))
app.add_page(role_selection_page, route="/")
app.add_page(login_page, route="/login")
app.add_page(student_dashboard_page, route="/student")
app.add_page(professor_dashboard_page, route="/professor")
app.add_page(admin_dashboard_page, route="/admin")