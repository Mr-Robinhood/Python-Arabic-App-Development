import reflex as rx
from typing import Optional


def header(title: str, subtitle: Optional[str] = None) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.h1(
                    f"Smart Cloud - {title}", class_name="text-2xl font-bold text-white"
                ),
                class_name="flex items-center gap-4",
            ),
            rx.el.div(
                rx.icon(tag="bell", class_name="h-6 w-6 text-white"),
                rx.icon(tag="user", class_name="h-6 w-6 text-white"),
                class_name="flex items-center gap-4",
            ),
            class_name="flex items-center justify-between w-full max-w-7xl mx-auto p-4",
        ),
        rx.cond(
            subtitle,
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        rx.icon(tag="sun", class_name="text-yellow-400"),
                        class_name="p-3 bg-white/20 rounded-lg",
                    ),
                    rx.el.div(
                        rx.el.h2(subtitle, class_name="font-bold text-white"),
                        rx.el.p(
                            "لديك 3 واجبات جديدة للتقييم",
                            class_name="text-white/80 text-sm",
                        ),
                    ),
                    class_name="flex items-center gap-4",
                ),
                class_name="w-full max-w-7xl mx-auto p-4 rounded-xl bg-white/10 mt-4",
            ),
        ),
        class_name="bg-gradient-to-b from-purple-600 to-purple-700 p-4 rounded-b-3xl shadow-lg mb-8",
    )


def admin_header() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.h1(
                    "Smart Cloud - لوحة المشرف",
                    class_name="text-2xl font-bold text-white",
                )
            ),
            rx.el.div(
                rx.icon(tag="bell", class_name="h-6 w-6 text-white"),
                rx.icon(tag="user", class_name="h-6 w-6 text-white"),
                class_name="flex items-center gap-4",
            ),
            class_name="flex items-center justify-between w-full max-w-7xl mx-auto p-4",
        ),
        class_name="bg-gradient-to-b from-green-600 to-green-700 p-4 rounded-b-3xl shadow-lg mb-8",
    )


def quick_action_card(icon: str, text: str, color: str) -> rx.Component:
    return rx.el.div(
        rx.icon(tag=icon, class_name=f"h-6 w-6 {color}"),
        rx.el.p(text, class_name="text-gray-700 font-semibold mt-2 text-sm"),
        class_name="bg-white p-4 rounded-xl shadow-sm flex flex-col items-center justify-center border border-gray-100 hover:shadow-lg transition-shadow cursor-pointer",
    )


def stat_card(icon: str, value: str, label: str, icon_bg_color: str) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon(tag=icon, class_name="text-gray-600"),
            class_name=f"p-3 rounded-lg {icon_bg_color}",
        ),
        rx.el.div(
            rx.el.p(value, class_name="text-2xl font-bold text-gray-800"),
            rx.el.p(label, class_name="text-gray-500 text-sm"),
            class_name="text-right",
        ),
        class_name="flex items-center justify-between p-4 bg-white rounded-xl shadow-sm border border-gray-100",
    )


def section_header(title: str, link_text: str = "عرض الكل") -> rx.Component:
    return rx.el.div(
        rx.el.h3(title, class_name="text-xl font-bold text-gray-800"),
        rx.el.a(link_text, href="#", class_name="text-purple-600 font-semibold"),
        class_name="flex justify-between items-center mb-4",
    )


def activity_item(icon: str, title: str, subtitle: str, icon_bg: str) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon(tag=icon, class_name="h-5 w-5 text-gray-600"),
            class_name=f"p-3 rounded-lg {icon_bg}",
        ),
        rx.el.div(
            rx.el.p(title, class_name="font-semibold text-gray-800"),
            rx.el.p(subtitle, class_name="text-sm text-gray-500"),
            class_name="flex-grow",
        ),
        class_name="flex items-center gap-4 p-4 bg-white rounded-xl shadow-sm border border-gray-100",
    )


def course_card(subject: str, professor: str, progress: int) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h4(subject, class_name="font-bold text-gray-800"),
            rx.el.p(professor, class_name="text-sm text-gray-500"),
            class_name="flex-grow",
        ),
        rx.el.div(
            rx.el.div(
                style={"width": f"{progress}%"},
                class_name="bg-blue-500 h-1.5 rounded-full",
            ),
            class_name="w-full bg-gray-200 rounded-full h-1.5 mt-2",
        ),
        rx.el.p(f"{progress}%", class_name="text-xs text-gray-500 mt-1 text-right"),
        class_name="bg-white p-4 rounded-xl shadow-sm border border-gray-100 flex flex-col gap-2",
    )


def bottom_nav_item(icon: str, text: str, is_active: bool = False) -> rx.Component:
    return rx.el.div(
        rx.icon(
            tag=icon,
            class_name=rx.cond(
                is_active, "text-purple-600 h-6 w-6", "text-gray-500 h-6 w-6"
            ),
        ),
        rx.el.p(
            text,
            class_name=rx.cond(
                is_active, "text-purple-600 text-xs font-bold", "text-gray-500 text-xs"
            ),
        ),
        class_name="flex flex-col items-center gap-1",
    )