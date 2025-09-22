import reflex as rx
from app.states.state import LoginState
from app.components.login_form import login_form


def login_page() -> rx.Component:
    return rx.el.div(
        rx.el.button(
            rx.icon(tag="arrow-right", class_name="h-5 w-5"),
            on_click=LoginState.go_back_to_selection,
            class_name="absolute top-8 left-8 text-gray-500 hover:bg-gray-100 p-2 rounded-full transition",
        ),
        rx.match(
            LoginState.login_type,
            (
                "admin",
                login_form(
                    icon_name="shield",
                    icon_bg_color="bg-green-100",
                    welcome_title="مرحباً بك مشرفنا الكريم",
                    welcome_subtitle="سجل دخولك لإدارة النظام بالكامل",
                    username_label="اسم المستخدم",
                    username_placeholder="admin123",
                    username_icon="user",
                    button_text="تسجيل الدخول",
                    button_color="bg-green-500",
                    form_handler=LoginState.handle_login,
                ),
            ),
            (
                "professor",
                login_form(
                    icon_name="book-user",
                    icon_bg_color="bg-purple-100",
                    welcome_title="مرحباً بك أستاذنا الكريم",
                    welcome_subtitle="سجل دخولك لإدارة المواد والمحاضرات",
                    username_label="البريد الجامعي",
                    username_placeholder="name@university.edu",
                    username_icon="mail",
                    button_text="تسجيل الدخول",
                    button_color="bg-purple-500",
                    form_handler=LoginState.handle_login,
                ),
            ),
            (
                "student",
                login_form(
                    icon_name="users",
                    icon_bg_color="bg-blue-100",
                    welcome_title="مرحباً بك",
                    welcome_subtitle="سجل دخولك للوصول إلى ملفاتك الجامعية",
                    username_label="الرقم الجامعي",
                    username_placeholder="1234567",
                    username_icon="user",
                    button_text="تسجيل الدخول",
                    button_color="bg-blue-500",
                    form_handler=LoginState.handle_login,
                ),
            ),
            rx.el.div(
                rx.el.p("Please select a login type first."),
                rx.el.a("Go back", href="/"),
            ),
        ),
        class_name="w-full min-h-screen flex items-center justify-center bg-gray-50 p-4",
    )