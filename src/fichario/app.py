"""
Annotation app
"""
# Setup Django
import os
import sys
print(sys.executable)
os.environ.setdefault('BASE_MODULE', 'fichario.')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'{os.getenv("BASE_MODULE", "")}fichario_django.settings')
import django
django.setup()
from django.conf import settings as django_settings

# Continue
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW, CENTER
from fichario.display.main import MainView
from fichario.display.annotation import DisplayAnnotation, DisplayAnnotationList, DisplayAnnotationEdit
from fichario.display.text import DisplayText, DisplayTextList, DisplayTextEdit
from fichario.display.welcome import WelcomeView
from fichario.layout.toolbar import create_toolbar
from . import styles
import gettext
import pathlib

gettext.install('fichario')

class Fichário(toga.App):
    def test_database(self):
        """Tests and installs Django database."""
        if not pathlib.Path(django_settings.DATABASES['default']['NAME']).is_file():
            print('Creating database…')
            from django.core import management
            from django.core.management.commands import migrate
            management.call_command(migrate, interactive=False)
        else:
            print('Database exists.')
    
    def show_texts(self, widget):
        content = DisplayTextList(texts=[1,2,3], style=styles.base_box)
        self.main_window.content = content
    
    def show_annotations(self, widget):
        content = DisplayAnnotation(style=styles.base_box)
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
        
        # self.test_database()
        
        self.main_window = toga.MainWindow(title=self.formal_name)
        create_toolbar(self)
        content = WelcomeView(
            style=Pack(
                padding=styles.main_padding,
                alignment=CENTER,
                direction=COLUMN,
                background_color=styles.colors.background
            ),
        )
        self.main_window.content = content
        self.main_window.show()


def main():
    return Fichário()
