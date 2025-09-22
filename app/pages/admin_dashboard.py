import reflex as rx
from app.states.admin_dashboard_state import AdminDashboardState
from app.components.dashboard_components import (
    admin_header,
    quick_action_card,
    stat_card,
    section_header,
    activity_item,
)


def admin_dashboard_page() -> rx.Component:
    return rx.el.div(
        admin_header(),
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.icon(tag="check_check", class_name="h-8 w-8 text-green-500"),
                    rx.el.div(
                        rx.el.h2(
                            "حالة النظام: نشط",
                            class_name="font-bold text-lg text-gray-800",
                        ),
                        rx.el.p(
                            "كل الخدمات تعمل بشكل طبيعي", class_name="text-gray-500"
                        ),
                    ),
                    class_name="flex items-center gap-4",
                ),
                class_name="p-6 rounded-xl bg-green-50 w-full mb-8 border border-green-200",
            ),
            section_header(title="إجراءات سريعة", link_text=""),
            rx.el.div(
                quick_action_card(
                    icon="users", text="المستخدمون", color="text-blue-500"
                ),
                quick_action_card(icon="box", text="المواد", color="text-orange-500"),
                quick_action_card(
                    icon="file-text", text="التقارير", color="text-purple-500"
                ),
                quick_action_card(
                    icon="archive", text="التخزين", color="text-yellow-500"
                ),
                quick_action_card(
                    icon="settings", text="الإعدادات", color="text-gray-500"
                ),
                quick_action_card(
                    icon="database-backup", text="النسخ الاحتياطي", color="text-red-500"
                ),
                class_name="grid grid-cols-3 sm:grid-cols-3 md:grid-cols-6 gap-4 mb-8",
            ),
            section_header(title="إحصائيات النظام", link_text=""),
            rx.el.div(
                stat_card(
                    icon="users",
                    value=AdminDashboardState.users_count,
                    label="المستخدمون",
                    icon_bg_color="bg-blue-100",
                ),
                stat_card(
                    icon="folder",
                    value=AdminDashboardState.files_count,
                    label="الملفات",
                    icon_bg_color="bg-yellow-100",
                ),
                stat_card(
                    icon="database",
                    value=AdminDashboardState.storage_used,
                    label="المساحة المستخدمة",
                    icon_bg_color="bg-green-100",
                ),
                stat_card(
                    icon="box",
                    value=AdminDashboardState.materials_count,
                    label="المواد",
                    icon_bg_color="bg-orange-100",
                ),
                class_name="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 mb-8",
            ),
            section_header(title="النشاطات الأخيرة", link_text="عرض الكل"),
            rx.el.div(
                activity_item(
                    icon="user-plus",
                    title="تمت إضافة مستخدم جديد",
                    subtitle="أحمد محمد - طالب | منذ 15 دقيقة",
                    icon_bg="bg-blue-100",
                ),
                activity_item(
                    icon="upload",
                    title="تم رفع ملف جديد",
                    subtitle="ملف المحاضرة 5 - د.خالد | منذ ساعة",
                    icon_bg="bg-green-100",
                ),
                class_name="flex flex-col gap-4",
            ),
            class_name="max-w-7xl mx-auto w-full px-4 sm:px-6 lg:px-8",
        ),
        class_name="bg-gray-50 min-h-screen",
    )