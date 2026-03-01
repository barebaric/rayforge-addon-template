"""
Backend entry point for the addon.

This module is loaded in both worker and main processes.
Use it for producers, steps, and other non-UI components.
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
def rayforge_init(context):
    """Called when the application context is fully initialized."""
    print("My Awesome Addon has been loaded!")


@hookimpl
def on_unload():
    """Called when the addon is being disabled or unloaded."""
    print("My Awesome Addon is being unloaded!")


@hookimpl
def register_producers(producer_registry, addon_name):
    """Register custom producers. Called in backend context."""
    # Pass addon_name to register - it's required!
    # from .producers import MyProducer
    # producer_registry.register(MyProducer, addon_name=addon_name)
    pass


@hookimpl
def register_steps(step_registry, addon_name):
    """Register custom steps. Called in backend context."""
    # Pass addon_name to register - it's required!
    # from .steps import MyStep
    # step_registry.register(MyStep, addon_name=addon_name)
    pass


@hookimpl
def register_menu_items(menu_registry, addon_name):
    """Register menu items. Called in main process."""
    # Pass addon_name to register - it's required!
    # menu_registry.register(
    #     item_id="my_addon.my_action",
    #     label=_("My Action"),  # Translatable string
    #     action="win.my_addon_my_action",
    #     menu="Tools",
    #     priority=100,
    #     addon_name=addon_name,
    # )
    pass
