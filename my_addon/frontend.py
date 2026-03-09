"""
Frontend entry point for the addon.

This module is loaded only in the main process.
Use it for UI widgets and other GTK components.
"""

import gettext
from pathlib import Path

from rayforge.core.hooks import hookimpl

# Addon name - must match the directory name for proper cleanup
ADDON_NAME = "my_addon"

# Set up translations for this addon.
# The locales directory is at the addon root (next to this module's directory).
_localedir = Path(__file__).parent.parent / "locales"
_t = gettext.translation("my_addon", localedir=_localedir, fallback=True)
_ = _t.gettext


@hookimpl
def register_actions(action_registry):
    """Register window actions. Called in frontend context."""
    # Example:
    # from gi.repository import Gio
    # from rayforge.ui_gtk.action_registry import MenuPlacement
    #
    # def on_my_action(action, param):
    #     print("My action triggered!")
    #
    # action = Gio.SimpleAction.new("my_addon_my_action", None)
    # action.connect("activate", on_my_action)
    # action_registry.register(
    #     action_name="my_addon_my_action",
    #     action=action,
    #     addon_name=ADDON_NAME,
    #     label="My Action",
    #     menu=MenuPlacement(menu_id="tools", priority=100),
    # )
    pass


@hookimpl
def step_settings_loaded(dialog, step, producer):
    """Add step settings widgets based on producer type."""
    # Example:
    # from .widgets import MyProducerWidget
    # if producer is None:
    #     return
    # widget_cls = PRODUCER_WIDGETS.get(type(producer))
    # if widget_cls:
    #     dialog.add(widget_cls(
    #         dialog.editor,
    #         step.typelabel,
    #         producer,
    #         dialog,
    #         step
    #     ))
    pass


@hookimpl
def transformer_settings_loaded(dialog, step, transformer):
    """Add transformer settings widgets based on transformer type."""
    # Example:
    # from .widgets import TRANSFORMER_WIDGETS
    # widget_cls = TRANSFORMER_WIDGETS.get(type(transformer))
    # if widget_cls:
    #     dialog.add(widget_cls(
    #         dialog.editor,
    #         transformer.label,
    #         transformer,
    #         dialog,
    #         step
    #     ))
    pass
