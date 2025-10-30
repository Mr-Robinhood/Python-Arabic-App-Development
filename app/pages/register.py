import reflex as rx
from app.states.registration_state import RegistrationState


def registration_form() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.button(
                "طالب",
                on_click=lambda: RegistrationState.set_registration_type("student"),
                class_name=rx.cond(
                    RegistrationState.registration_type == "student",
                    "px-6 py-2 rounded-lg bg-purple-600 text-white font-semibold",
                    "px-6 py-2 rounded-lg bg-gray-200 text-gray-600 font-semibold",
                ),
            ),
            rx.el.button(
                "أستاذ",
                on_click=lambda: RegistrationState.set_registration_type("professor"),
                class_name=rx.cond(
                    RegistrationState.registration_type == "professor",
                    "px-6 py-2 rounded-lg bg-purple-600 text-white font-semibold",
                    "px-6 py-2 rounded-lg bg-gray-200 text-gray-600 font-semibold",
                ),
            ),
            class_name="flex gap-4 p-1 bg-gray-100 rounded-lg mb-8",
        ),
        rx.match(
            RegistrationState.registration_type,
            ("student", student_registration_form()),
            ("professor", professor_registration_form()),
        ),
        class_name="w-full max-w-lg flex flex-col items-center",
    )


def form_field(
    label: str, name: str, placeholder: str, type: str, icon: str
) -> rx.Component:
    return rx.el.div(
        rx.el.label(
            label, html_for=name, class_name="text-gray-600 font-medium mb-2 block"
        ),
        rx.el.div(
            rx.el.input(
                id=name,
                name=name,
                placeholder=placeholder,
                type=type,
                class_name="w-full py-3 pr-4 pl-12 rounded-lg border border-gray-200 focus:outline-none focus:ring-2 focus:ring-purple-300 transition",
            ),
            rx.icon(
                tag=icon,
                class_name="absolute left-4 top-1/2 -translate-y-1/2 text-gray-400",
            ),
            class_name="relative",
        ),
        class_name="mb-6",
    )


def student_registration_form() -> rx.Component:
    return rx.el.form(
        form_field("الاسم الكامل", "name", "مثال: خالد محمد الأحمد", "text", "user"),
        form_field("الرقم الجامعي", "university_id", "مثال: 441001234", "text", "hash"),
        form_field(
            "البريد الإلكتروني", "email", "example@university.edu", "email", "mail"
        ),
        form_field("كلمة المرور", "password", "••••••••", "password", "lock"),
        rx.el.button(
            "إنشاء حساب",
            type="submit",
            class_name="w-full bg-purple-500 text-white py-3 rounded-lg font-semibold text-lg hover:bg-purple-600 transition shadow-md",
        ),
        on_submit=RegistrationState.handle_student_registration,
        reset_on_submit=True,
        class_name="w-full",
    )


def professor_registration_form() -> rx.Component:
    return rx.el.form(
        form_field("الاسم الكامل", "name", "مثال: د. خالد الأحمد", "text", "user"),
        form_field("اسم المستخدم", "username", "مثال: k.alahmad", "text", "at-sign"),
        form_field(
            "البريد الإلكتروني", "email", "k.alahmad@university.edu", "email", "mail"
        ),
        form_field("كلمة المرور", "password", "••••••••", "password", "lock"),
        rx.el.button(
            "إنشاء حساب",
            type="submit",
            class_name="w-full bg-purple-500 text-white py-3 rounded-lg font-semibold text-lg hover:bg-purple-600 transition shadow-md",
        ),
        on_submit=RegistrationState.handle_professor_registration,
        reset_on_submit=True,
        class_name="w-full",
    )


def register_page() -> rx.Component:
    return rx.el.div(
        rx.el.button(
            rx.icon(tag="arrow-right", class_name="h-5 w-5"),
            on_click=rx.redirect("/"),
            class_name="absolute top-8 right-8 text-gray-500 hover:bg-gray-100 p-2 rounded-full transition",
        ),
        rx.el.div(
            rx.el.div(
                rx.icon(tag="user-plus", class_name="h-10 w-10 text-white"),
                class_name="p-5 rounded-full bg-purple-100 text-purple-600 mb-8 shadow-md",
            ),
            rx.el.h1(
                "إنشاء حساب جديد",
                class_name="text-3xl font-bold text-gray-800 text-center",
            ),
            rx.el.p(
                "اختر نوع حسابك واملأ البيانات للتسجيل",
                class_name="text-gray-500 mt-2 mb-10 text-center",
            ),
            registration_form(),
            class_name="w-full max-w-lg flex flex-col items-center",
        ),
        class_name="w-full min-h-screen flex items-center justify-center bg-gray-50 p-4",
    )