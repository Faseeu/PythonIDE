from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import subprocess

class Terminal(BoxLayout):
    def __init__(self, **kwargs):
        super(Terminal, self).__init__(**kwargs)
        self.orientation = 'vertical'

        self.output = TextInput(readonly=True, font_size=14, size_hint_y=None, height=200)
        self.add_widget(self.output)

        self.input = TextInput(font_size=14, multiline=False, size_hint_y=None, height=40)
        self.input.bind(on_text_validate=self.on_enter)
        self.add_widget(self.input)

    def on_enter(self, instance):
        command = self.input.text
        self.input.text = ''
        self.run_command(command)

    def run_command(self, command):
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()

        if stdout:
            self.output.text += stdout.decode('utf-8') + '\n'
        if stderr:
            self.output.text += stderr.decode('utf-8') + '\n'
