from kivy.uix.boxlayout import BoxLayout
from kivy.uix.treeview import TreeView, TreeViewLabel
from kivy.uix.label import Label
import os

class DirectoryStructure(BoxLayout):
    def __init__(self, **kwargs):
        super(DirectoryStructure, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 10
        self.spacing = 10
        self.background_color = (0.1, 0.1, 0.1, 1)

        self.label = Label(text="Directory Structure", size_hint_y=None, height=40, color=(1, 1, 1, 1))
        self.add_widget(self.label)

        self.tree_view = TreeView(hide_root=True)
        self.add_widget(self.tree_view)
        self.populate_tree_view(self.tree_view, os.path.expanduser("~"))

    def populate_tree_view(self, tree_view, path):
        for root, dirs, files in os.walk(path):
            for dir in dirs:
                node = TreeViewLabel(text=f"[DIR] {dir}", color=(0.7, 0.7, 0.7, 1))
                tree_view.add_node(node)
            for file in files:
                node = TreeViewLabel(text=f"[FILE] {file}", color=(0.7, 0.7, 0.7, 1))
                tree_view.add_node(node)
            break
