"""
Annotation app
"""
# Setup Django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fichario.fichario_django.settings')
import django
django.setup()

# Continue
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW, CENTER
from fichario.display.main import MainView
from fichario.display.annotation import DisplayAnnotation, DisplayAnnotationsList, DisplayAnnotationsEdit
from fichario.display.text import TextView, DisplayTextsList
from fichario.display.welcome import WelcomeView
from fichario.layout.toolbar import create_toolbar
from . import styles

class Fichário(toga.App):
    def show_texts(self, widget):
        pass
    
    def show_annotations(self, widget):
        content = DisplayAnnotation(
            id='annotation',
            style=Pack(
                padding=styles.main_padding,
                alignment=CENTER,
                direction=COLUMN,
                background_color=styles.Colors.background
            ),
        )
        self.main_window.content = content
    
    def show_bookmarks(self, widget):
        pass
    
    def show_preferences(self, widget):
        pass

    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """

        self.main_window = toga.MainWindow(title=self.formal_name)
        create_toolbar(self)
        content = WelcomeView(
            id='welcome',
            style=Pack(
                padding=styles.main_padding,
                alignment=CENTER,
                direction=COLUMN,
                background_color=styles.Colors.background
            ),
        )
        self.main_window.content = content
        self.main_window.show()


def main():
    return Fichário()
