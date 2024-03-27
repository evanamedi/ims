from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivy.graphics import Color, Rectangle
from kivy.graphics import RoundedRectangle
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.graphics import Mesh
from kivy.graphics.texture import Texture
import numpy as np

class ContentPage(Screen):
    def __init__(self, **kwargs):
        super(ContentPage, self).__init__(**kwargs)
        self._set_background_color()

        # Create a BoxLayout with a Button and an empty Widget
        box_layout = BoxLayout(orientation='vertical')
        box_layout.add_widget(self._create_back_button())
        box_layout.add_widget(Widget())

        # Add the BoxLayout to the ContentPage
        self.add_widget(box_layout)

    def _set_background_color(self):
        # Create a texture
        texture = Texture.create(size=(2, 2), colorfmt='rgba')

        # Create a 2x2 pixel array, each pixel is an RGBA (4 values from 0 to 255)
        pixels = np.array([
            [0, 255, 255, 255],  # Top left pixel
            [0, 255, 255, 255],  # Top right pixel
            [255, 0, 0, 255],  # Bottom left pixel
            [255, 0, 0, 255]   # Bottom right pixel
        ], dtype=np.uint8)

        # Set the texture pixels
        texture.blit_buffer(pixels.tostring(), colorfmt='rgba', bufferfmt='ubyte')

        with self.canvas.before:
            # Draw a rectangle with the gradient texture
            self.rect = Mesh(vertices=[0, 0, 0, 0, self.width, 0, self.width, self.height, 0, self.height],
                            indices=[0, 1, 2, 3],
                            mode='triangle_fan',
                            texture=texture)
            self.bind(size=self._update_rect, pos=self._update_rect)

    def _create_back_button(self):
        button = Button(
            text="Main Menu",
            size_hint=(None, None),
            size=(100, 50),
            on_press=self.change_screen,
            background_color=(1, 0, 0, 1),  # make button transparent
            color=(1, 1, 1, 1),  # text color
            font_size=14  # adjust as needed
        )

        with button.canvas.before:
            Color(0, 1, 1, 1)  # button color
            rounded_rectangle = RoundedRectangle(radius=[10,])
            button.bind(pos=lambda instance, value: setattr(rounded_rectangle, 'pos', value),
                        size=lambda instance, value: setattr(rounded_rectangle, 'size', value))

        return button

    def change_screen(self, instance):
        self.manager.current = "menu"

    def _update_rect(self, instance, value):
        self.rect.vertices = [instance.x, instance.y, 0, 0,
            instance.right, instance.y, instance.width, 0,
            instance.right, instance.top, instance.width, instance.height,
            instance.x, instance.top, 0, instance.height]