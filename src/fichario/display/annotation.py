import toga, markdown
from fichario.annotations import models

class DisplayAnnotation(toga.Box):
    def on_load(self, *args, **kwargs):
        pass
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.webview = toga.WebView(
            id='annotation_content',
            on_webview_load=self.on_load,
        )
        self.webview.set_content('', markdown.markdown('# Teste\n\nabcd'))
        self.add(self.webview)

class DisplayAnnotationsList(toga.Box):
    pass

class DisplayAnnotationsEdit(toga.Box):
    pass
