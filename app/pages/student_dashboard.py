import reflex as rx
from app.states.student_dashboard_state import StudentDashboardState
from app.components.dashboard_components import (
    header,
    stat_card,
    section_header,
    course_card,
    bottom_nav_item,
)
from app.pages.professor_dashboard import schedule_item


def student_dashboard_page() -> rx.Component:
    return rx.el.div(
        header(title="لوحة الطالب", subtitle="أهلاً بك, أحمد!"),
        rx.el.div(
            section_header(title="نظرة عامة", link_text=""),
            rx.el.div(
                stat_card(
                    icon="book-copy",
                    value=StudentDashboardState.courses_count,
                    label="المواد المسجلة",
                    icon_bg_color="bg-blue-100",
                ),
                stat_card(
                    icon="file-text",
                    value=StudentDashboardState.assignments_due,
                    label="واجبات قادمة",
                    icon_bg_color="bg-orange-100",
                ),
                stat_card(
                    icon="award",
                    value=StudentDashboardState.gpa,
                    label="المعدل التراكمي",
                    icon_bg_color="bg-green-100",
                ),
                stat_card(
                    icon="calendar-clock",
                    value=StudentDashboardState.schedule_today_count,
                    label="محاضرات اليوم",
                    icon_bg_color="bg-purple-100",
                ),
                class_name="grid grid-cols-2 lg:grid-cols-4 gap-4 mb-8",
            ),
            section_header(title="المواد الدراسية", link_text="عرض الكل"),
            rx.el.div(
                course_card(
                    subject="نظم التشغيل", professor="د. خالد الأحمد", progress=75
                ),
                course_card(
                    subject="هياكل البيانات", professor="د. منى الصالح", progress=60
                ),
                class_name="grid grid-cols-1 md:grid-cols-2 gap-4 mb-8",
            ),
            section_header(title="جدولي", link_text="عرض الجدول الكامل"),
            rx.el.div(
                schedule_item(
                    time="10:00 ص - 11:30 ص",
                    title="نظم التشغيل",
                    location="القاعة 203",
                    icon_color="text-blue-500",
                ),
                schedule_item(
                    time="01:00 م - 02:30 م",
                    title="أمن الشبكات",
                    location="القاعة 301",
                    icon_color="text-red-500",
                ),
                class_name="flex flex-col gap-4 mb-8",
            ),
            class_name="max-w-7xl mx-auto w-full px-4 sm:px-6 lg:px-8",
        ),
        rx.el.div(
            rx.el.div(
                bottom_nav_item(icon="layout-grid", text="الرئيسية", is_active=True),
                bottom_nav_item(icon="book-copy", text="المواد"),
                bottom_nav_item(icon="folder-open", text="الملفات"),
                bottom_nav_item(icon="user-circle", text="حسابي"),
                class_name="flex justify-around items-center w-full max-w-md mx-auto",
            ),
            class_name="fixed bottom-0 left-0 right-0 bg-white p-4 border-t border-gray-200 shadow-t-lg",
        ),
        class_name="bg-gray-50 min-h-screen pb-24",
    )