import reflex as rx
from typing import Callable
from app.states.state import LoginState


def login_form(
    icon_name: str,
    icon_bg_color: str,
    welcome_title: str,
    welcome_subtitle: str,
    username_label: str,
    username_placeholder: str,
    username_icon: str,
    button_text: str,
    button_color: str,
    form_handler: Callable,
) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon(tag=icon_name, class_name="h-10 w-10 text-white"),
            class_name=f"p-5 rounded-full {icon_bg_color} mb-8 shadow-md",
        ),
        rx.el.h1(
            welcome_title, class_name="text-3xl font-bold text-gray-800 text-center"
        ),
        rx.el.p(welcome_subtitle, class_name="text-gray-500 mt-2 mb-10 text-center"),
        rx.el.form(
            rx.el.div(
                rx.el.label(
                    username_label,
                    html_for="username",
                    class_name="text-gray-600 font-medium mb-2 block",
                ),
                rx.el.div(
                    rx.el.input(
                        id="username",
                        name="username",
                        placeholder=username_placeholder,
                        type="text",
                        class_name="w-full py-3 pr-4 pl-12 rounded-lg border border-gray-200 focus:outline-none focus:ring-2 focus:ring-gray-300 transition",
                    ),
                    rx.icon(
                        tag=username_icon,
                        class_name="absolute left-4 top-1/2 -translate-y-1/2 text-gray-400",
                    ),
                    class_name="relative",
                ),
                class_name="mb-6",
            ),
            rx.el.div(
                rx.el.label(
                    "كلمة المرور",
                    html_for="password",
                    class_name="text-gray-600 font-medium mb-2 block",
                ),
                rx.el.div(
                    rx.el.input(
                        id="password",
                        name="password",
                        placeholder="••••••••",
                        type="password",
                        class_name="w-full py-3 pr-4 pl-12 rounded-lg border border-gray-200 focus:outline-none focus:ring-2 focus:ring-gray-300 transition",
                    ),
                    rx.icon(
                        tag="lock",
                        class_name="absolute left-4 top-1/2 -translate-y-1/2 text-gray-400",
                    ),
                    class_name="relative",
                ),
                class_name="mb-6",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.input(
                        type="checkbox",
                        id="remember-me",
                        class_name="h-4 w-4 rounded border-gray-300 text-green-600 focus:ring-green-500 ml-2",
                    ),
                    rx.el.label(
                        "تذكرني", html_for="remember-me", class_name="text-gray-600"
                    ),
                    class_name="flex items-center gap-2",
                ),
                rx.el.a(
                    "نسيت كلمة المرور؟",
                    href="#",
                    class_name=f"text-sm {button_color.replace('bg', 'text').replace('-500', '-600')} hover:underline",
                ),
                class_name="flex justify-between items-center mb-8",
            ),
            rx.el.button(
                button_text,
                type="submit",
                class_name=f"w-full {button_color} text-white py-3 rounded-lg font-semibold text-lg hover:opacity-90 transition shadow-md",
            ),
            on_submit=form_handler,
            reset_on_submit=True,
            class_name="w-full",
        ),
        class_name="w-full max-w-md flex flex-col items-center",
    )