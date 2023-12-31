import toga

texts_icon = toga.icons.Icon('resources/UI/book-open-variant.png')
annotations_icon = toga.icons.Icon('resources/UI/pencil-outline.png')
bookmarks_icon = toga.icons.Icon('resources/UI/bookmark-multiple-outline.png')
preferences_icon = toga.icons.Icon('resources/UI/cog-outline.png')

def create_toolbar(app):
    view_group = toga.Group('View')
    texts_command = toga.Command(
        app.show_texts,
        text='Texts',
        tooltip='Show, add or edit text objects',
        icon=texts_icon,
        group=view_group,
        order=0,
    )
    annotations_command = toga.Command(
        app.show_annotations,
        text='Annotations',
        tooltip='Show, add or edit annotations',
        icon=annotations_icon,
        group=view_group,
        order=1,
    )
    bookmarks_command = toga.Command(
        app.show_bookmarks,
        text='Bookmarks',
        tooltip='Show bookmarked annotations',
        icon=bookmarks_icon,
        group=view_group,
        order=2,
    )
    app.main_window.toolbar.add(
        texts_command,
        annotations_command,
        bookmarks_command,
    )
    
    preferences_command = None
    for command in app.commands._commands:
        if command.text == 'Preferences':
            preferences_command = command
            preferences_command.icon = preferences_icon
            preferences_command.enabled = True
            app.main_window.toolbar.add(preferences_command)
