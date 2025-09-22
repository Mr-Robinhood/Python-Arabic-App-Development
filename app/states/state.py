import reflex as rx
from typing import Literal

LoginType = Literal["student", "professor", "admin", ""]


class LoginState(rx.State):
    login_type: LoginType = ""
    username: str = ""
    password: str = ""
    remember_me: bool = False

    @rx.event
    def set_login_type(self, login_type: LoginType):
        self.login_type = login_type
        return rx.redirect("/login")

    @rx.event
    def handle_login(self, form_data: dict):
        self.username = form_data.get("username", "")
        self.password = form_data.get("password", "")
        yield rx.toast.info(
            f"Logging in as {self.login_type} with user: {self.username}"
        )
        if self.login_type == "admin":
            return rx.redirect("/admin/dashboard")
        if self.login_type == "professor":
            return rx.redirect("/professor/dashboard")
        if self.login_type == "student":
            return rx.redirect("/student/dashboard")

    @rx.event
    def go_back_to_selection(self):
        self.login_type = ""
        return rx.redirect("/")