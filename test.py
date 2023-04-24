from kivymd.app import MDApp
from kivymd.uix.bottomnavigation import MDBottomNavigation, MDBottomNavigationItem
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen


class Example(MDApp):
    def build(self):
        screen = MDScreen()
        bottom_navigation = MDBottomNavigation(
            panel_color="#eeeaea",
            selected_color_background="#97ecf8",
            text_color_active="white",
        )

        data = {
            "screen 1": {"text": "Marks", "icon": ""},
            "screen 2": {"text": "Attendance", "icon": ""},
            "screen 3": {"text": "Assignment", "icon": "teacher.jpeg"},
        }
        for key in data.keys():
            text = data[key]["text"]
            navigation_item = MDBottomNavigationItem(
                name=key, text=text, icon=data[key]["icon"]
            )
            navigation_item.add_widget(MDLabel(text=text, halign="center"))
            bottom_navigation.add_widget(navigation_item)

        screen.add_widget(bottom_navigation)
        return screen


Example().run()