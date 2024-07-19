from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from ui.editor import Editor
from ui.terminal import Terminal
from ui.directory_structure import DirectoryStructure
from ui.menu import Menu
from data.settings import Settings
from extensions import ExtensionManager

class MobileIDE(App):
    def build(self):
        self.settings = Settings()
        self.extension_manager = ExtensionManager()
        self.extension_manager.load_extensions()

        self.layout = BoxLayout(orientation='vertical')
        self.main_content = BoxLayout(orientation='vertical')
        
        self.editor = Editor()
        self.terminal = Terminal()
        self.directory_structure = DirectoryStructure()

        self.menu = Menu(switch_view_callback=self.switch_view)
        
        self.layout.add_widget(self.menu)
        self.layout.add_widget(self.main_content)
        
        self.switch_view(self.settings.get('last_view', 'editor'))

        return self.layout

    def switch_view(self, view_name):
        self.settings.set('last_view', view_name)
        self.main_content.clear_widgets()
        if view_name == "editor":
            self.main_content.add_widget(self.editor)
        elif view_name == "terminal":
            self.main_content.add_widget(self.terminal)
        elif view_name == "directory_structure":
            self.main_content.add_widget(self.directory_structure)

    def execute_extension(self, extension_name, *args, **kwargs):
        return self.extension_manager.execute_extension(extension_name, *args, **kwargs)

if __name__ == '__main__':
    MobileIDE().run()
