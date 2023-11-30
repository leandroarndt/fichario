# Global style definitions
from copy import copy
from toga.style import Pack
from toga.style.pack import TOP, COLUMN, LEFT, SANS_SERIF, BOLD

# Padding
main_padding = 16
padding = 8

# Sizing
text_size = 14
title_size = text_size * 1.5
big_title_size = text_size * 2
small_text_size = text_size * 0.8

# Colors (based on https://m2.material.io/design/color/the-color-system.html#color-theme-creation)
class Colors(object):
    primary = '#03DAC6'
    primary_variant = '#018786'
    secondary = '#6200EE'
    secondary_variant = '#3700B3'
    background = '#FFFFFF'
    surface = '#FFFFFF'
    error = '#FB0020'
    on_primary = '#000000'
    on_secondary = '#FFFFFF'
    on_background = '#000000'
    on_surface = '#000000'
    on_error = '#FFFFFF'
    
    title = primary_variant
    
    active = primary
    inactive = primary_variant
    grayed = '#AAAAAA'
    on_grayed = '#000000'
    
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Colors, cls).__new__(cls)
        return cls._instance

colors = Colors()

# Styles
box = Pack(
    padding = padding,
    direction = COLUMN,
    alignment = TOP,
    background_color = colors.background,
)

base_box = copy(box)
base_box.update(padding=main_padding)

# Text styles
text = Pack(
    text_align=LEFT,
    color=colors.on_background,
    background_color=colors.background,
    font_family=SANS_SERIF,
    font_size=text_size
)

title = copy(text)
title.update(font_size=title_size, color=colors.primary_variant, font_weight=BOLD)

small_title = copy(title)
small_title.update(font_size=text_size)

big_title = copy(title)
big_title.update(font_size=big_title_size)

tag = copy(text)
tag.update(font_size=small_text_size, color=colors.on_secondary, background_color=colors.secondary)
