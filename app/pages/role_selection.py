import reflex as rx
from app.states.state import LoginState


def role_card(
    title: str,
    subtitle: str,
    icon: str,
    icon_bg_color: str,
    on_click: rx.event.EventType,
) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.icon(tag=icon, class_name="h-7 w-7"),
                class_name=f"p-3 rounded-lg {icon_bg_color} mr-4",
            ),
            rx.el.div(
                rx.el.h3(title, class_name="font-bold text-lg text-gray-800"),
                rx.el.p(subtitle, class_name="text-gray-500"),
                class_name="flex-grow",
            ),
            rx.icon(tag="chevron-left", class_name="text-gray-400"),
            class_name="flex items-center w-full",
        ),
        on_click=on_click,
        class_name="w-full max-w-md bg-white p-5 rounded-xl border border-gray-200 shadow-sm hover:shadow-md hover:border-gray-300 transition-all cursor-pointer",
    )


def role_selection_page() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h2(
                "تسجيل الدخول",
                class_name="text-3xl font-bold text-gray-800 text-center",
            ),
            rx.el.p(
                "اختر نوع الحساب للدخول إلى النظام",
                class_name="text-gray-500 mt-2 mb-10 text-center",
            ),
            rx.el.div(
                role_card(
                    title="طالب",
                    subtitle="الدخول بحساب الطالب",
                    icon="users",
                    icon_bg_color="bg-blue-100 text-blue-600",
                    on_click=lambda: LoginState.set_login_type("student"),
                ),
                role_card(
                    title="أستاذ",
                    subtitle="الدخول بحساب الأستاذ",
                    icon="book-user",
                    icon_bg_color="bg-purple-100 text-purple-600",
                    on_click=lambda: LoginState.set_login_type("professor"),
                ),
                role_card(
                    title="مشرف",
                    subtitle="الدخول بحساب المشرف",
                    icon="shield",
                    icon_bg_color="bg-green-100 text-green-600",
                    on_click=lambda: LoginState.set_login_type("admin"),
                ),
                class_name="flex flex-col items-center gap-4 w-full",
            ),
            rx.el.p(
                "ليس لديك حساب؟ ",
                rx.el.a(
                    "تواصل مع الإدارة",
                    href="#",
                    class_name="font-semibold text-gray-700 hover:underline",
                ),
                class_name="text-center mt-12 text-gray-500",
            ),
            class_name="w-full max-w-md flex flex-col items-center",
        ),
        class_name="w-full min-h-screen flex items-center justify-center bg-gray-50 p-4",
    )