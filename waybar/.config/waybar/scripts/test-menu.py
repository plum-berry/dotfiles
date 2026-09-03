import gi
gi.require_version('Gtk', '3.0')

try:
    gi.require_version('GtkLayerShell', '0.1')
except ValueError:
    import sys
    raise RuntimeError('\n\n' +
        'If you haven\'t installed GTK Layer Shell, you need to point Python to the\n' +
        'library by setting GI_TYPELIB_PATH and LD_LIBRARY_PATH to <build-dir>/src/.\n' +
        'For example you might need to run:\n\n' +
        'GI_TYPELIB_PATH=build/src LD_LIBRARY_PATH=build/src python3 ' + ' '.join(sys.argv))

from gi.repository import Gtk, GtkLayerShell

window = Gtk.Window()
label = Gtk.Label(label='GTK Layer Shell with Python!')
window.add(label)

GtkLayerShell.init_for_window(window)

# Layer
GtkLayerShell.set_layer(window, GtkLayerShell.Layer.TOP)
# Setting up margins for the window
GtkLayerShell.set_margin(window, GtkLayerShell.Edge.TOP, 10)
GtkLayerShell.set_margin(window, GtkLayerShell.Edge.BOTTOM, 10)
GtkLayerShell.set_margin(window, GtkLayerShell.Edge.LEFT, 10)
GtkLayerShell.set_margin(window, GtkLayerShell.Edge.RIGHT, 10)

# Alignment of the window
GtkLayerShell.set_anchor(window, GtkLayerShell.Edge.TOP, 1)
GtkLayerShell.set_anchor(window, GtkLayerShell.Edge.RIGHT, 1)

window.set_size_request(300, 200)
window.show_all()
window.connect('destroy', Gtk.main_quit)
Gtk.main()

