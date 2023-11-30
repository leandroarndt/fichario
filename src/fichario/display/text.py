import toga
from fichario import styles
from . import generic
from django.utils.lorem_ipsum import sentence

class DisplayText(toga.Box):
    pass

class DisplayTextItem(toga.Box):
    def __init__(self, text, *args, **kwargs):
        kwargs['style'] = styles.base_box
        super().__init__(*args, **kwargs)
        
        self.add(
            toga.Label('Arndt, Leandro', style=styles.text),
            toga.Label(sentence(), style=styles.small_title),
            toga.Label('Brasília: 2023', style=styles.text),
        )

class DisplayTextList(generic.ListDisplay):
    def __init__(self, texts, *args, **kwargs):
        elements = []
        for text in texts:
            elements.append(DisplayTextItem(text))
        super().__init__(children=elements, *args, **kwargs)

class DisplayTextEdit(toga.Box):
    pass
