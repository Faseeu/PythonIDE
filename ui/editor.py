from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from logic.static_analysis import StaticAnalysis
from logic.linter import Linter
from logic.formatter import Formatter
from logic.autocomplete import AutoComplete

class Editor(BoxLayout):
    def __init__(self, **kwargs):
        super(Editor, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 10
        self.spacing = 10
        self.background_color = (0.1, 0.1, 0.1, 1)

        self.label = Label(text="Editor", size_hint_y=None, height=40, color=(1, 1, 1, 1))
        self.add_widget(self.label)

        self.text_input = TextInput(multiline=True, font_size=16, padding=10, background_color=(0.2, 0.2, 0.2, 1), foreground_color=(1, 1, 1, 1))
        self.text_input.bind(on_text_validate=self.on_text_validate)
        self.add_widget(self.text_input)

        self.result_label = Label(size_hint_y=None, height=40, color=(1, 1, 1, 1))
        self.add_widget(self.result_label)

        self.analysis_button = Button(text="Run Static Analysis", on_press=self.run_static_analysis)
        self.add_widget(self.analysis_button)

        self.lint_button = Button(text="Run Linter", on_press=self.run_linter)
        self.add_widget(self.lint_button)

        self.format_button = Button(text="Format Code", on_press=self.format_code)
        self.add_widget(self.format_button)

    def get_text(self):
        return self.text_input.text

    def set_text(self, text):
        self.text_input.text = text

    def on_text_validate(self, instance):
        text = self.get_text()
        line, column = self.text_input.cursor
        completions = AutoComplete.get_completions(text, line, column)
        self.result_label.text = ', '.join(completions)

    def run_static_analysis(self, instance):
        file_path = "temp_code.py"  # Temporary file for analysis
        with open(file_path, "w") as f:
            f.write(self.get_text())
        result = StaticAnalysis.run_analysis(file_path)
        self.result_label.text = result

    def run_linter(self, instance):
        file_path = "temp_code.py"  # Temporary file for linting
        with open(file_path, "w") as f:
            f.write(self.get_text())
        result = Linter.run_linter(file_path)
        self.result_label.text = result

    def format_code(self, instance):
        file_path = "temp_code.py"  # Temporary file for formatting
        with open(file_path, "w") as f:
            f.write(self.get_text())
        result = Formatter.format_code(file_path)
        self.result_label.text = result
        with open(file_path, "r") as f:
            formatted_code = f.read()
        self.set_text(formatted_code)
