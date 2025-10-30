import reflex as rx
from typing import Literal
from app.database import (
    create_user,
    get_user_by_email,
    get_user_by_university_id,
    get_user_by_username,
)

RegistrationType = Literal["student", "professor"]


class RegistrationState(rx.State):
    registration_type: RegistrationType = "student"

    @rx.event
    def set_registration_type(self, reg_type: RegistrationType):
        self.registration_type = reg_type
        if reg_type == "student" or reg_type == "professor":
            return rx.redirect("/register")

    @rx.event
    def handle_student_registration(self, form_data: dict):
        name = form_data.get("name")
        university_id = form_data.get("university_id")
        email = form_data.get("email")
        password = form_data.get("password")
        if not all([name, university_id, email, password]):
            return rx.toast.error("يرجى ملء جميع الحقول")
        if get_user_by_university_id(university_id) or get_user_by_email(email):
            return rx.toast.error("هذا الحساب مسجل بالفعل")
        create_user(
            name=name,
            password=password,
            role="student",
            email=email,
            university_id=university_id,
        )
        yield rx.toast.success(f"تم إنشاء حساب الطالب: {name}")
        return rx.redirect("/login")

    @rx.event
    def handle_professor_registration(self, form_data: dict):
        name = form_data.get("name")
        username = form_data.get("username")
        email = form_data.get("email")
        password = form_data.get("password")
        if not all([name, username, email, password]):
            return rx.toast.error("يرجى ملء جميع الحقول")
        if get_user_by_username(username) or get_user_by_email(email):
            return rx.toast.error("هذا الحساب مسجل بالفعل")
        create_user(
            name=name,
            password=password,
            role="professor",
            email=email,
            username=username,
        )
        yield rx.toast.success(f"تم إنشاء حساب الأستاذ: {name}")
        return rx.redirect("/login")