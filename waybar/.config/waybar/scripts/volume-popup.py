#/usr/bin/env python3
# ~/.config/waybar/scripts/volume-popup.py


#!/usr/bin/env python3
import gi
gi.require_version('Gtk', '3.0')
gi.require_version('GtkLayerShell', '0.1')
from gi.repository import Gtk, Gdk, GtkLayerShell
import subprocess

css_provider = Gtk.CssProvider()
css_provider.load_from_path("/home/plum/.config/waybar/scripts/volume-popup.css")
Gtk.StyleContext.add_provider_for_screen(
    Gdk.Screen.get_default(), css_provider,
    Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
)
def get_volume():
    out = subprocess.check_output(
        ["pactl", "get-sink-volume", "@DEFAULT_SINK@"]
    ).decode()
    # crude parse of the % value
    pct = int(out.split("/")[1].strip().replace("%", ""))
    return pct

def set_volume(val):
    subprocess.run(["pactl", "set-sink-volume", "@DEFAULT_SINK@", f"{int(val)}%"])

def toggle_mute(_btn):
    subprocess.run(["pactl", "set-sink-mute", "@DEFAULT_SINK@", "toggle"])

class VolumePopup(Gtk.Window):
    def __init__(self):
        super().__init__(title="volume-popup")
        GtkLayerShell.init_for_window(self)
        GtkLayerShell.set_layer(self, GtkLayerShell.Layer.OVERLAY)
        GtkLayerShell.set_anchor(self, GtkLayerShell.Edge.TOP, True)
        GtkLayerShell.set_anchor(self, GtkLayerShell.Edge.RIGHT, True)
        GtkLayerShell.set_margin(self, GtkLayerShell.Edge.TOP, 40)   # clear waybar height
        GtkLayerShell.set_margin(self, GtkLayerShell.Edge.RIGHT, 12)
        GtkLayerShell.set_keyboard_mode(self, GtkLayerShell.KeyboardMode.ON_DEMAND)

        self.set_default_size(220, 60)
        self.set_decorated(False)
        self.get_style_context().add_class("volume-popup")

        box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=8)
        box.set_border_width(12)

        mute_btn = Gtk.Button(label="🔊")
        mute_btn.connect("clicked", toggle_mute)
        box.pack_start(mute_btn, False, False, 0)

        adj = Gtk.Adjustment(value=get_volume(), lower=0, upper=100,
                              step_increment=1, page_increment=5)
        scale = Gtk.Scale(orientation=Gtk.Orientation.HORIZONTAL, adjustment=adj)
        scale.set_hexpand(True)
        scale.set_digits(0)
        scale.connect("value-changed", lambda s: set_volume(s.get_value()))
        box.pack_start(scale, True, True, 0)

        self.add(box)

        # click-outside / focus-loss closes the popup
        self.connect("focus-out-event", lambda *_: Gtk.main_quit())
        self.connect("key-press-event", self.on_key)

    def on_key(self, _w, event):
        if event.keyval == Gdk.KEY_Escape:
            Gtk.main_quit()

win = VolumePopup()
win.show_all()
Gtk.main()
