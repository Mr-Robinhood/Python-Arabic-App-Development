import reflex as rx
from app.states.professor_dashboard_state import ProfessorDashboardState
from app.components.dashboard_components import (
    header,
    stat_card,
    section_header,
    activity_item,
)


def schedule_item(
    time: str, title: str, location: str, icon_color: str
) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon(tag="clock", class_name=f"h-5 w-5 {icon_color}"),
            class_name="p-3 rounded-lg bg-gray-100",
        ),
        rx.el.div(
            rx.el.p(time, class_name="text-sm text-gray-500"),
            rx.el.h4(title, class_name="font-semibold text-gray-800"),
            rx.el.p(location, class_name="text-sm text-gray-500"),
        ),
        class_name="flex items-center gap-4 p-4 bg-white rounded-xl shadow-sm border border-gray-100",
    )


def professor_dashboard_page() -> rx.Component:
    return rx.el.div(
        header(title="لوحة الأستاذ", subtitle="صباح الخير, د.خالد!"),
        rx.el.div(
            section_header(title="إحصائيات سريعة", link_text=""),
            rx.el.div(
                stat_card(
                    icon="users-2",
                    value=ProfessorDashboardState.students_count,
                    label="الطلاب",
                    icon_bg_color="bg-green-100",
                ),
                stat_card(
                    icon="book-open",
                    value=ProfessorDashboardState.materials_count,
                    label="المواد",
                    icon_bg_color="bg-blue-100",
                ),
                stat_card(
                    icon="folder",
                    value=ProfessorDashboardState.files_count,
                    label="الملفات",
                    icon_bg_color="bg-yellow-100",
                ),
                stat_card(
                    icon="file-check",
                    value=ProfessorDashboardState.assignments_count,
                    label="الواجبات",
                    icon_bg_color="bg-orange-100",
                ),
                class_name="grid grid-cols-2 lg:grid-cols-4 gap-4 mb-8",
            ),
            section_header(title="جدول اليوم", link_text="عرض الكل"),
            rx.el.div(
                schedule_item(
                    time="10:00 ص - 11:30 ص",
                    title="نظم التشغيل",
                    location="القاعة 203",
                    icon_color="text-blue-500",
                ),
                schedule_item(
                    time="12:00 م - 1:30 م",
                    title="هياكل البيانات",
                    location="القاعة 105",
                    icon_color="text-purple-500",
                ),
                class_name="flex flex-col gap-4 mb-8",
            ),
            section_header(title="آخر المرفوعات", link_text="عرض الكل"),
            rx.el.div(
                activity_item(
                    icon="upload-cloud",
                    title="ملف المحاضرة 5",
                    subtitle="نظم التشغيل | منذ يومين",
                    icon_bg="bg-green-100",
                ),
                activity_item(
                    icon="upload-cloud",
                    title="تمارين الوحدة 4",
                    subtitle="هياكل البيانات | منذ 3 أيام",
                    icon_bg="bg-orange-100",
                ),
                class_name="flex flex-col gap-4",
            ),
            class_name="max-w-7xl mx-auto w-full px-4 sm:px-6 lg:px-8",
        ),
        class_name="bg-gray-50 min-h-screen pb-8",
    )