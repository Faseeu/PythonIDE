from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class Menu(BoxLayout):
    def __init__(self, switch_view_callback, **kwargs):
        super(Menu, self).__init__(**kwargs)
        self.orientation = 'horizontal'
        self.size_hint_y = None
        self.height = 50
        self.spacing = 5
        self.padding = 5

        self.switch_view_callback = switch_view_callback

        editor_button = Button(text="Editor", on_press=lambda x: self.switch_view_callback("editor"))
        terminal_button = Button(text="Terminal", on_press=lambda x: self.switch_view_callback("terminal"))
        directory_structure_button = Button(text="Directory Structure", on_press=lambda x: self.switch_view_callback("directory_structure"))

        self.add_widget(editor_button)
        self.add_widget(terminal_button)
        self.add_widget(directory_structure_button)
