import toga
from toga.style import Pack
from toga.style.pack import BOLD, SANS_SERIF, CENTER
from fichario import styles

class WelcomeView(toga.Box):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        welcome_style = Pack(
            alignment=CENTER,
            font_weight=BOLD,
            font_family=SANS_SERIF,
            font_size=36,
            color=styles.Colors.title,
            background_color=styles.Colors.background,
            text_align=CENTER,
        )
        self.add(toga.Box(style=Pack(flex=1)))
        self.add(toga.Label(_('Welcome to Fichário!'), style=welcome_style))
        self.add(toga.Box(style=Pack(flex=1)))
