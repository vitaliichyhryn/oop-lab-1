import gi

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")

from gi.repository import Gtk, Gio, Adw

class Window(Adw.ApplicationWindow):
    def __init__(self, **kwargs):
        super().__init__(**kwargs, default_width=600, default_height=600)

        toolbar_view = Adw.ToolbarView()
        self.set_content(toolbar_view)

        header_bar = Adw.HeaderBar()
        toolbar_view.add_top_bar(header_bar)
        
        window_title = Adw.WindowTitle(title="meow")
        header_bar.set_title_widget(window_title)

        menu = Gio.Menu()
        menu.append('Робота1', 'app.action_1')
        menu.append('Робота2', 'app.action_2')

        menu_button = Gtk.MenuButton(
            primary=True,
            icon_name="open-menu-symbolic",
            menu_model=menu)
        header_bar.pack_end(menu_button)

        self.label = Gtk.Label(label='', use_markup=True)
        toolbar_view.set_content(self.label)