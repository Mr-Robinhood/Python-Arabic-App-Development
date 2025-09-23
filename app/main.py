import os

os.environ["KIVY_TEXT"] = "pango"
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
import arabic_reshaper
from bidi.algorithm import get_display

Window.clearcolor = get_color_from_hex("#FFFFFF")


def reshape_arabic(text):
    reshaped_text = arabic_reshaper.reshape(text)
    return get_display(reshaped_text)


class RoleSelectionScreen(Screen):
    def __init__(self, **kwargs):
        super(RoleSelectionScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation="vertical", padding=50, spacing=30)
        logo = Image(
            source="assets/placeholder.svg",
            size_hint=(None, None),
            size=(150, 150),
            allow_stretch=True,
        )
        logo_layout = BoxLayout(size_hint_y=None, height=150, padding=[0, 20, 0, 20])
        logo_layout.add_widget(logo)
        layout.add_widget(logo_layout)
        title_text = reshape_arabic("اختر صفة المستخدم")
        title_label = Label(
            text=title_text,
            font_name="DejaVuSans",
            font_size="32sp",
            color=get_color_from_hex("#000000"),
        )
        layout.add_widget(title_label)
        roles = [("طالب", "student"), ("أستاذ", "professor"), ("مسؤول", "admin")]
        buttons_layout = BoxLayout(
            orientation="vertical", spacing=20, size_hint_y=None, height=210
        )
        for role_text, role_id in roles:
            button_text = reshape_arabic(role_text)
            btn = Button(
                text=button_text,
                font_name="DejaVuSans",
                size_hint_y=None,
                height=60,
                background_color=get_color_from_hex("#3B82F6"),
                background_normal="",
            )
            btn.bind(on_press=self.go_to_login)
            buttons_layout.add_widget(btn)
        layout.add_widget(buttons_layout)
        self.add_widget(layout)

    def go_to_login(self, instance):
        print(f"Login as: {instance.text}")


class SmartCloudApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(RoleSelectionScreen(name="role_selection"))
        return sm


if __name__ == "__main__":
    SmartCloudApp().run()