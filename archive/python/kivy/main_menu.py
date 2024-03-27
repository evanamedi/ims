from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen

class MainMenu(Screen):
    def __init__(self, **kwargs):
        super(MainMenu, self).__init__(**kwargs)
        self.add_widget(Button(text="Go to Content Page", on_press=self.change_screen))

    def change_screen(self, instance):
        self.manager.current = "content"