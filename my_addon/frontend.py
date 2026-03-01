"""
Frontend entry point for the addon.

This module is loaded only in the main process.
Use it for UI widgets and other GTK components.
"""

import gettext
from pathlib import Path

from rayforge.core.hooks import hookimpl

# Set up translations for this addon.
# The locales directory is at the addon root (next to this module's directory).
_localedir = Path(__file__).parent.parent / "locales"
_t = gettext.translation("my_addon", localedir=_localedir, fallback=True)
_ = _t.gettext


@hookimpl
def register_step_widgets(widget_registry, addon_name):
    """Register UI widgets for step types. Called in frontend context."""
    # Pass addon_name to register - it's required!
    # from .widgets import MyStepWidget
    # from .producers import MyProducer
    # widget_registry.register(MyProducer, MyStepWidget, addon_name=addon_name)
    pass


@hookimpl
def register_actions(window):
    """Register window actions. Called in frontend context."""
    # Example:
    # from gi.repository import Gio, GLib
    #
    # def on_my_action(action, param):
    #     print("My action triggered!")
    #
    # action = Gio.SimpleAction.new("my_addon_my_action", None)
    # action.connect("activate", on_my_action)
    # window.add_action(action)
    pass
