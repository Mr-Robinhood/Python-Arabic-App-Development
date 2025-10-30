import reflex as rx
from typing import Literal
from app.database import authenticate_user

LoginType = Literal["student", "professor", "admin", ""]


class LoginState(rx.State):
    login_type: LoginType = ""
    error_message: str = ""

    @rx.event
    def set_login_type(self, login_type: LoginType):
        self.login_type = login_type
        self.error_message = ""
        return rx.redirect("/login")

    @rx.event
    def handle_login(self, form_data: dict):
        self.error_message = ""
        identifier = form_data.get("username", "")
        password = form_data.get("password", "")
        if not identifier or not password:
            self.error_message = "يرجى إدخال اسم المستخدم وكلمة المرور"
            return
        user = authenticate_user(identifier, password, self.login_type)
        if user:
            yield rx.toast.success(f"مرحبًا بعودتك, {user['name']}")
            if self.login_type == "admin":
                return rx.redirect("/admin/dashboard")
            if self.login_type == "professor":
                return rx.redirect("/professor/dashboard")
            if self.login_type == "student":
                return rx.redirect("/student/dashboard")
        else:
            self.error_message = "بيانات الدخول غير صحيحة"
            return rx.toast.error("فشل تسجيل الدخول")

    @rx.event
    def go_back_to_selection(self):
        self.login_type = ""
        self.error_message = ""
        return rx.redirect("/")