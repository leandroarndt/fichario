# Global style definitions
import copy
from toga.style import Pack
from toga.style.pack import TOP, COLUMN, LEFT, SANS_SERIF, BOLD

# Padding
main_padding = 16
padding = 8

# Sizing
text_size = 14
title_size = text_size * 1.5
big_title_size = text_size * 2

# Colors (based on https://m2.material.io/design/color/the-color-system.html#color-theme-creation)
class Colors:
    primary = '#6200EE'
    primary_variant = '#3700B3'
    secondary = '#03DAC6'
    secondary_variant='#018786'
    background = '#FFFFFF'
    surface = '#FFFFFF'
    error = '#FB0020'
    on_primary = '#FFFFFF'
    on_secondary = '#000000'
    on_background = '#000000'
    on_surface = '#000000'
    on_error = '#FFFFFF'
    
    title = secondary_variant
    
    active = secondary
    inactive = secondary_variant
    grayed = '#AAAAAA'
    on_grayed = '#000000'

# Styles
base_box = Pack(
    padding = main_padding,
    direction = COLUMN,
    alignment = TOP,
    background_color = Colors.background
)

# Text styles
text = Pack(
    text_align=LEFT,
    color=Colors.on_background,
    background_color=Colors.background,
    font_family=SANS_SERIF,
    font_size=text_size
)

title = copy.copy(text)
title.update(font_size=title_size, color=Colors.secondary_variant, font_weight=BOLD)

big_title = copy.copy(title)
big_title.update(font_size=big_title_size)
