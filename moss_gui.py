from gi.repository import Gtk
class MyApp (object):

    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file("moss_gui.glade")
        self.builder.connect_signals(self)

    def run(self):
        self.builder.get_object("window1").show_all()
        Gtk.main()

    def on_window1_destroy(self, *args):
        Gtk.main_quit()


MyApp().run()
