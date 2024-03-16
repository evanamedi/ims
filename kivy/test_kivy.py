from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from main_menu import MainMenu
from content_page import ContentPage

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainMenu(name="menu"))
        sm.add_widget(ContentPage(name="content"))
        return sm

if __name__ == "__main__":
    MyApp().run()