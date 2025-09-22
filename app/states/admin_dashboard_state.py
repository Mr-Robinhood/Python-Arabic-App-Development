import reflex as rx


class AdminDashboardState(rx.State):
    users_count: str = "1,245"
    files_count: str = "8,742"
    storage_used: str = "45.2GB"
    materials_count: str = "87"