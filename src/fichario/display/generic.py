import toga
from fichario import styles

class ListDisplay(toga.Box):
    elements = []
    
    def __init__(self, *args, **kwargs):
        if 'style' not in kwargs.keys():
            kwargs['style'] = styles.base_box
        if 'children' in kwargs:
            children = kwargs['children']
            del kwargs['children']
        else:
            children = []
        super().__init__(*args, **kwargs)
        if children:
            self.update(children)
    
    def divide(self, elements)->list:
        with_dividers = [toga.Divider()] * (len(elements) * 2 - 1)
        with_dividers[0::2] = elements
        return with_dividers
    
    def update(self, elements, *args, **kwargs):
        self.elements = []
        self.clear()
        self.add(elements)
    
    def add(self, *args, **kwargs):
        if self.elements:
            self.add(toga.Divider())
        self.elements += args
        super().add(*self.divide(*args), **kwargs)
