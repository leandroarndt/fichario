"""
Annotation app
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from views.main import MainView
from views.annotation import AnnotationView, ListAnnotationsView
from views.text import TextView, ListTextsView

class Fichário(toga.App):

    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        main_box = MainView()

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()


def main():
    return Fichário()
